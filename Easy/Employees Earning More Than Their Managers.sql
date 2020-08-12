-- # Write your MySQL query statement below
SELECT A.NAME AS Employee FROM Employee As A, Employee As B WHERE A.ManagerId  = B.Id AND A.Salary > B.Salary;

-- Runtime: 745 ms, faster than 22.12% of MySQL online submissions for Employees Earning More Than Their Managers.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.

-- # Write your MySQL query statement below
SELECT a.Name AS Employee FROM Employee a JOIN Employee b ON a.ManagerId = b.Id WHERE a.Salary > b.Salary;

-- Runtime: 398 ms, faster than 64.83% of MySQL online submissions for Employees Earning More Than Their Managers.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Employees Earning More Than Their Managers.