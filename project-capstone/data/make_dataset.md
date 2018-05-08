CREATE CONSTRAINT ON (p:Product) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT ON (a:Aisle) ASSERT a.id IS UNIQUE;
CREATE CONSTRAINT ON (d:Department) ASSERT d.id IS UNIQUE;

// Explore dataset
LOAD CSV WITH HEADERS FROM "file:///products.csv" AS line WITH line
RETURN line
LIMIT 5;

// Committing it
USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///products_clean.csv" AS line WITH line
CREATE (product:Product {id: toInteger(line.product_id), name: line.product_name})
MERGE (aisle:Aisle {id: toInteger(line.aisle_id), name: line.aisle})
MERGE (department:Department {id: toInteger(line.department_id),name: line.department})
CREATE (product)-[:FOUND_IN]->(aisle)
CREATE (product)-[:TYPE_OF]->(department);

// Added 36791 labels, created 36791 nodes, set 73582 properties, created 73350 relationships, completed after 2690 ms (3082 ms).

// Adding the users
// Create constraints
CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;

// Committing it
USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///users_orders.csv" AS line WITH line
MATCH (product:Product {id: toInteger(line.product_id)})
MERGE (user:User {id: toInteger(line.user_id)})
CREATE (user)-[b:BOUGHT]->(product)
SET b.order_total = toInteger(line.total_orders);

//Added 205847 labels, created 205847 nodes, set 6183525 properties, created 2988839 relationships, completed after 82490 ms.

// Adding the recipes
// Using APOC to load json files
// Create constraint on the categories and recipes
CREATE CONSTRAINT ON (c:Category) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (r:Recipe) ASSERT r.name is UNIQUE;

CALL apoc.load.json("file:///epi_recipe_json_cleaned.json")
YIELD value AS line
CREATE (recipe:Recipe {name: line.title, rating: toInteger(line.rating), ingredients: line.ingredients, directions: line.directions})
WITH recipe, line.categories AS categories
UNWIND categories AS cat
MERGE (c:Category {name:cat})
CREATE (recipe)-[:TAGGED_AS]->(c)

//Added 18449 labels, created 18449 nodes, set 71764 properties, created 219434 relationships, completed after 2705 ms.
