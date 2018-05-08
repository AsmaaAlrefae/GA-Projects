# Cypher Commands

These are the commands to create the database on Neo4j. You can use either py2neo package or run each of these lines in Neo4j using the Neo4j browser.

**Note:** `//` denotes the comment symbol in Cypher.

```
// Create the constraints items that must be unique
//
// For the products
CREATE CONSTRAINT ON (p:Product) ASSERT p.id IS UNIQUE;
CREATE CONSTRAINT ON (a:Aisle) ASSERT a.id IS UNIQUE;
CREATE CONSTRAINT ON (d:Department) ASSERT d.id IS UNIQUE;
// For the users
CREATE CONSTRAINT ON (u:User) ASSERT u.id IS UNIQUE;
//For the recipes
CREATE CONSTRAINT ON (c:Category) ASSERT c.name IS UNIQUE;
CREATE CONSTRAINT ON (r:Recipe) ASSERT r.name is UNIQUE;

// Make sure the files are in the /import folder in Neo4j
// Uploading the products_clean.csv file
USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///products_clean.csv" AS line WITH line
CREATE (product:Product {id: toInteger(line.product_id), name: line.product_name})
MERGE (aisle:Aisle {id: toInteger(line.aisle_id), name: line.aisle})
MERGE (department:Department {id: toInteger(line.department_id), name: line.department})
CREATE (product)-[:FOUND_IN]->(aisle)
CREATE (product)-[:TYPE_OF]->(department);

// Upload the users_orders.csv file
USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///users_orders.csv" AS line WITH line
MATCH (product:Product {id: toInteger(line.product_id)})
MERGE (user:User {id: toInteger(line.user_id)})
CREATE (user)-[b:BOUGHT]->(product)
SET b.order_total = toInteger(line.total_orders);

// Using APOC (community extensions) to load cleaned recipe file (in JSON)
CALL apoc.load.json("file:///epi_recipe_json_cleaned.json")
YIELD value AS line
CREATE (recipe:Recipe {name: line.title, rating: toInteger(line.rating), ingredients: line.ingredients, directions: line.directions})
WITH recipe, line.categories AS categories
UNWIND categories AS cat
MERGE (c:Category {name:cat})
CREATE (recipe)-[:TAGGED_AS]->(c);
```

There's quite a number of things to do before APOC is enabled and up and running for Neo4j. I would have to refer you to the documentation or to Google for the steps since they might change by the time you attempt this.