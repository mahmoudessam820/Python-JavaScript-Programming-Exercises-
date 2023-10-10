-- Laptop Vs Mobile Viewership New York Times SQL Interview Question

-- Assume you're given the table on user viewership categorised by device type where the three types are laptop, tablet, and phone.

-- Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership.

-- Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.


-- Note ⚠️:
-- You have to visit the task URL to fully understand what the task needs if you want to add a solution or test your solution!

-- Task URL: https://datalemur.com/questions/laptop-mobile-viewership 


-- Solution:

SELECT 

  SUM(CASE WHEN device_type = 'laptop' THEN 1 ELSE 0 END) AS laptop_views,
  SUM(CASE WHEN device_type IN ('phone', 'tablet') THEN 1 ELSE 0 END) AS mobile_views
  
FROM viewership;