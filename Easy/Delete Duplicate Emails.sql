-- # Write your MySQL query statement below
DELETE b FROM Person AS a, Person AS b WHERE a.Email = b.Email AND a.Id< b.Id

-- Runtime: 2559 ms, faster than 13.82% of MySQL online submissions for Delete Duplicate Emails.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Delete Duplicate Emails.