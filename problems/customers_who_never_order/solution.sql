# Write your MySQL query statement below
select name as Customers  from Customers as C 
 LEFT JOIN  Orders as O ON 
 C.id = O.customerId 
 where O.customerId  is  NULL


# select name as 'Customers' from customers
# where customers.id not 
# in  (select customerid from orders);