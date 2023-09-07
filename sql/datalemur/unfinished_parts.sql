-- Unfinished Parts Tesla SQL Interview Question

-- Tesla is investigating production bottlenecks and they need your help to extract the relevant data. 
-- Write a query to determine which parts have begun the assembly process but are not yet finished.

-- Assumptions:
	
	-- parts_assembly table contains all parts currently in production, each at varying stages of the assembly process.
	-- An unfinished part is one that lacks a finish_date.

-- Note ⚠️:
-- You have to visit the task URL to fully understand what the task needs if you want to add a solution or test your solution!

-- Task URL: https://datalemur.com/questions/tesla-unfinished-parts 


-- Solution:

SELECT 
  part, 
  assembly_step
FROM 
  parts_assembly
WHERE 
  finish_date IS NULL;