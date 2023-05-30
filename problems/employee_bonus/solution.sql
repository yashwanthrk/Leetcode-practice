# Write your MySQL query statement below
select E.name, B.bonus from Employee as E left join Bonus as B
ON E.empId = B.empId where bonus is null or bonus < 1000 