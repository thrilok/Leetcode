-- # Write your MySQL query statement below
SELECT Name as Customers FROM Customers LEFT OUTER JOIN Orders ON Customers.Id = Orders.CustomerId WHERE Orders.CustomerId IS NULL;

-- Runtime: 571 ms, faster than 53.26% of MySQL online submissions for Customers Who Never Order.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Customers Who Never Order.