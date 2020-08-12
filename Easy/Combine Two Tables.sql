-- Write your MySQL query statement below
SELECT P.FirstName, P.LastName, A.City, A.State FROM Person P LEFT JOIN Address A ON P.PersonId = A.PersonId;

-- Runtime: 345 ms, faster than 88.92% of MySQL online submissions for Combine Two Tables.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Combine Two Tables.