# Write your MySQL query statement below
select product_name, year, price from Product 
inner join Sales where Product.product_id = Sales.product_id