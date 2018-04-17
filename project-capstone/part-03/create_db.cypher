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
MERGE (aisle:Aisle {id: toInteger(line.aisle_id),name: line.aisle})
MERGE (department:Department {id: toInteger(line.department_id),name: line.department})
CREATE (product)-[:FOUND_IN]->(aisle)
CREATE (product)-[:TYPE_OF]->(department);

// Added 36791 labels, created 36791 nodes, set 73582 properties, created 73350 relationships, completed after 2690 ms.








// Committing it
USING PERIODIC COMMIT 
LOAD CSV WITH HEADERS FROM "file:///products.csv" AS line WITH line
MERGE (p:Product {id: toInteger(line.product_id), name: toString(line.product_name), aisle: toInteger(line.aisle_id), department: toInteger(line.department_id)});


// Explore dataset with APOC
CALL apoc.load.csv("file:///products.csv", {sep:",", header:true,results:['map','list','strings','stringMap']})
YIELD list AS line
RETURN line
LIMIT 10;