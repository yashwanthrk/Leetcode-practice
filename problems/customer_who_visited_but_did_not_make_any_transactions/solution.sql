# Write your MySQL query statement below
select customer_id, count(Visits.visit_id) as count_no_trans from Visits
LEFT JOIN Transactions on Visits.visit_id = Transactions.visit_id
where transaction_id IS NULL
GROUP BY customer_id
