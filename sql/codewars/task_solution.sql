SELECT * FROM department;
SELECT * FROM employee;

SELECT 
    DISTINCT dept_id, -- Select the unique ID in each row.
    COUNT(*), -- Count the rows for each unique ID.
    SUM(salary) as sum_of_salary -- Sum all salary filds for each unique ID. 
FROM employee
GROUP BY dept_id -- Group all groups by unique ID. 
ORDER BY dept_id;

