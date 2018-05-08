`groceries` (32,434,489 rows):
* `user_id`: Discrete(integer), Customer identifier (unique integers) 
* `product_id`: Discrete(integer), Product identifier (unique integers) 
* `product_name`: Object(String), Name of the product (contains groceries and non-groceries items)

| Column Name   | Dtype             | Description                                                      |
| ------------- | ----------------- | ---------------------------------------------------------------- |
| user_id       | Discrete(integer) | Customer identifier (unique integers)                            |
| product_id    | Discrete(integer) | Product identifier (unique integers)                             |
| product_name  | Object(String)    | Name of the product (contains groceries and non-groceries items) |


#### FROM ORIGINAL FILES ####

`orders` (3.4m rows, 206k users):
* `order_id`: order identifier
* `user_id`: customer identifier
* `eval_set`: which evaluation set this order belongs in (see `SET` described below)
* `order_number`: the order sequence number for this user (1 = first, n = nth) # POTENTIALLY IMPORTANT
* `order_dow`: the day of the week the order was placed on # POTENTIALLY IMPORTANT
* `order_hour_of_day`: the hour of the day the order was placed on  # POTENTIALLY IMPORTANT
* `days_since_prior`: days since the last order, capped at 30 (with NAs for `order_number` = 1)

`products` (50k rows):
* `product_id`: product identifier
* `product_name`: name of the product
* `aisle_id`: foreign key
* `department_id`: foreign key

`aisles` (134 rows):
* `aisle_id`: aisle identifier
* `aisle`: the name of the aisle

`deptartments` (21 rows):
* `department_id`: department identifier
* `department`: the name of the department

`order_products__SET` (30m+ rows): 
* `order_id`: foreign key
* `product_id`: foreign key
* `add_to_cart_order`: order in which each product was added to cart # POTENTIALLY IMPORTANT
* `reordered`: 1 if this product has been ordered by this user in the past, 0 otherwise

where `SET` is one of the four following evaluation sets (`eval_set` in `orders`):
* `"prior"`: orders prior to that users most recent order (~3.2m orders)
* `"train"`: training data supplied to participants (~131k orders)
* `"test"`: test data reserved for machine learning competitions (~75k orders)



