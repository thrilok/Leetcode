-- # Write your MySQL query statement below
SELECT class FROM courses GROUP BY class HAVING COUNT(student)>=5;

-- Runtime: 469 ms, faster than 34.02% of MySQL online submissions for Classes More Than 5 Students.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Classes More Than 5 Students.