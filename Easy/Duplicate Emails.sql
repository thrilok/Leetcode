SELECT Email
FROM Person
GROUP BY Email
Having count(Email)>1

-- Runtime: 425 ms, faster than 42.11% of MySQL online submissions for Duplicate Emails.
-- Memory Usage: 0B, less than 100.00% of MySQL online submissions for Duplicate Emails.

