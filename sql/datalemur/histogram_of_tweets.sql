-- Histogram of Tweets Twitter SQL Interview Question

-- Assume you're given a table Twitter tweet data, write a query to obtain a histogram of tweets posted per user in 2022. 
-- Output the tweet count per user as the bucket and the number of Twitter users who fall into that bucket.
-- In other words, group the users by the number of tweets they posted in 2022 and count the number of users in each group.


-- Note ⚠️:
-- You have to visit the task URL to fully understand what the task needs if you want to add a solution or test your solution!

-- Task URL: https://datalemur.com/questions/sql-histogram-tweets


-- Solution:

SELECT tweet_count AS tweet_bucket, COUNT(*) AS users_num

FROM (
    SELECT user_id, COUNT(*) AS tweet_count
    FROM tweets
    WHERE EXTRACT(YEAR FROM tweet_date) = 2022
    GROUP BY user_id
) AS tweet_counts

GROUP BY tweet_count
ORDER BY tweet_count;, tweet_date) BETWEEN 2021 AND 2022
GROUP BY user_id; 
