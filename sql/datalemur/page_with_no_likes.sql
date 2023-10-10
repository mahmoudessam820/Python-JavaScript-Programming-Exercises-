-- Page With No Likes Facebook SQL Interview Question

-- Assume you're given two tables containing data about Facebook Pages and their respective likes (as in "Like a Facebook Page").
-- Write a query to return the IDs of the Facebook pages that have zero likes. 
-- The output should be sorted in ascending order based on the page IDs.

-- Note ⚠️:
-- You have to visit the task URL to fully understand what the task needs if you want to add a solution or test your solution!

-- Task URL: https://datalemur.com/questions/sql-page-with-no-likes


-- Solution:

SELECT 
    p.page_id 
FROM
    pages p 
LEFT JOIN 
    page_likes l
ON
    p.page_id = l.page_id
GROUP BY 
    p.page_id
HAVING
    COUNT(l.page_id) = 0;