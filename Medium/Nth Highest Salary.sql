CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        
        select distinct a.salary 
        from (Select salary,DENSE_RANK() OVER ( ORDER BY Salary desc) as row_num
         from Employee) a
   where a.row_num = @N
        );
END

-- Runtime: 1433 ms, faster than 22.33% of MS SQL Server online submissions for Nth Highest Salary.
-- Memory Usage: 0B, less than 100.00% of MS SQL Server online submissions for Nth Highest Salary.