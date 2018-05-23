from py2neo import Graph
from random import randint

graph = Graph(bolt=True, host="localhost", http_port=7687, user='neo4j', password='pasta')

def random_persons():
    # Random number generator for User ID since we can't 'login' as a User.
    user_id = randint(0, 206210)
    return user_id

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_purchases(self):
        query = '''
        MATCH (u:User {id: {userID}})-[b:BOUGHT]->(product:Product)
        WITH AVG(b.order_total) AS average_orders, b, product
        WHERE b.order_total >= average_orders
        RETURN DISTINCT product, b
        ORDER BY b.order_total DESC
        LIMIT 10
        '''

        return graph.run(query, userID=self.user_id)

    def get_recommendationsA(self):
        # Pearson + KNN recommendations.
        query = '''
        MATCH (u1:User {id: {userID}})-[b:BOUGHT]->(rec:Product)
        WITH u1, avg(b.order_total) AS u1_mean

        MATCH (u1)-[b1:BOUGHT]->(rec:Product)<-[b2:BOUGHT]-(u2)
        WITH u1, u1_mean, u2, COLLECT({b1: b1, b2: b2}) AS totalorders WHERE size(totalorders) > 2

        MATCH (u2)-[b:BOUGHT]->(rec:Product)
        WITH u1, u1_mean, u2, avg(b.order_total) AS u2_mean, totalorders

        UNWIND totalorders AS r

        WITH sum( (r.b1.order_total - u1_mean) * (r.b2.order_total - u2_mean) ) AS nom,
            sqrt( sum( (r.b1.order_total - u1_mean)^2) * sum( (r.b2.order_total - u2_mean) ^2)) AS denom,
            u1, u2 WHERE denom <> 0

        WITH u1, u2, nom/denom AS pearson
        ORDER BY pearson DESC LIMIT 10

        MATCH (u2)-[b:BOUGHT]->(rec:Product) WHERE NOT EXISTS( (u1)-[:BOUGHT]->(rec) )

        RETURN rec, SUM(pearson * b.order_total) AS score
        ORDER BY score DESC 
        LIMIT 5'''

        return graph.run(query, userID=self.user_id)

    def get_recommendationsB(self):
        # Novelty recommendations.
        query = '''
        MATCH (user:User {id: {userID}})-[:BOUGHT]->(product)-[:FOUND_IN]->(a:Aisle)-[:IN_CLUSTER]->(cluster)
        WITH user, cluster, COUNT(*) AS times
        ORDER BY times DESC
        LIMIT 1
        WITH cluster
        MATCH (cluster)<-[:IN_CLUSTER]-(a)<-[:FOUND_IN]-(p)
        WITH cluster, a.name AS aisleName, COUNT(p) as numberOfProducts
        ORDER BY numberOfProducts DESC
        LIMIT 1
        WITH aisleName AS x
        MATCH (Aisle {name: x})<-[:FOUND_IN]-(otherProducts)<-[b:BOUGHT]-()
        WHERE b.order_total > 10
        RETURN DISTINCT otherProducts, MAX(b.order_total) AS maxOrders
        ORDER BY maxOrders DESC
        LIMIT 5'''

        return graph.run(query, userID=self.user_id)
    
    def get_novelty(self):
        # Novelty recommendations.
        query = '''
        MATCH (user:User {id: {userID}})-[:BOUGHT]->(product)-[:FOUND_IN]->(a:Aisle)-[:IN_CLUSTER]->(cluster)
        WITH user, cluster, COUNT(*) AS times
        ORDER BY times ASC
        LIMIT 1
        WITH cluster
        MATCH (cluster)<-[:IN_CLUSTER]-(a)<-[:FOUND_IN]-(p)
        WITH cluster, a.name AS aisleName, COUNT(p) as numberOfProducts
        ORDER BY numberOfProducts DESC
        LIMIT 1
        WITH aisleName AS x
        MATCH (Aisle {name: x})<-[:FOUND_IN]-(otherProducts)<-[b:BOUGHT]-()
        WHERE b.order_total > 10
        RETURN DISTINCT otherProducts, MAX(b.order_total) AS maxOrders
        ORDER BY maxOrders DESC
        LIMIT 2'''

        return graph.run(query, userID=self.user_id)

    def get_recipes(self, product_list):
        # Get the recipe recommendations
        query = '''
        MATCH (c:Category)<-[:TAGGED_AS]-(recipe:Recipe)-[:TAGGED_AS]->(other:Category)
        WHERE c.name IN {product_list} AND recipe.rating >= 3.0
        WITH recipe, COLLECT(other.name) AS categories, COUNT(*) AS commonCategories
        RETURN recipe, categories, commonCategories
        ORDER BY commonCategories DESC 
        LIMIT 5
        '''

        return graph.run(query, product_list=product_list)
