SELECT COUNT(*) AS total_teachers
FROM teacher;

SELECT COUNT(name) AS teachers_with_names
FROM teacher;

SELECT COUNT(DISTINCT name) AS unique_teacher_names
FROM teacher;

SELECT SUM(salary) AS total_salary
FROM teacher;

SELECT AVG(salary) AS average_salary
FROM teacher;

SELECT MIN(salary) AS lowest_salary, MAX(salary) AS highest_salary
FROM teacher;

SELECT STDDEV(salary) AS salary_standard_deviation,
       VARIANCE(salary) AS salary_variance
FROM teacher;

SELECT STDDEV_POP(salary) AS population_standard_deviation,
       VAR_POP(salary) AS population_variance
FROM teacher;

SELECT PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY salary) AS median_salary
FROM teacher;

SELECT STRING_AGG(name, ', ' ORDER BY name) AS teacher_names
FROM teacher;

SELECT ARRAY_AGG(name ORDER BY name) AS teacher_names_array
FROM teacher;

SELECT JSON_AGG(JSON_BUILD_OBJECT('id', id, 'name', name, 'salary', salary)) AS teacher_records
FROM teacher;

SELECT age,
       COUNT(*) AS teacher_count,
       SUM(salary) AS total_salary,
       AVG(salary) AS average_salary,
       MIN(salary) AS lowest_salary,
       MAX(salary) AS highest_salary
FROM teacher
GROUP BY age
ORDER BY age;

SELECT age, AVG(salary) AS average_salary
FROM teacher
GROUP BY age
HAVING AVG(salary) > 30000
ORDER BY average_salary DESC;

SELECT COUNT(*) FILTER (WHERE salary > 50000) AS salary_above_50000,
       COUNT(*) FILTER (WHERE salary <= 50000) AS salary_at_or_below_50000
FROM teacher;

SELECT name, salary,
       CASE
           WHEN salary >= 100000 THEN 'High Salary'
           WHEN salary >= 50000 THEN 'Medium Salary'
           ELSE 'Lower Salary'
       END AS salary_category
FROM teacher;

SELECT name, age,
       CASE age
           WHEN 25 THEN 'Age 25'
           WHEN 35 THEN 'Age 35'
           WHEN 45 THEN 'Age 45'
           ELSE 'Other Age'
       END AS age_category
FROM teacher;

SELECT SUM(CASE WHEN salary >= 50000 THEN salary ELSE 0 END) AS salary_total_50000_and_above
FROM teacher;

SELECT COUNT(CASE WHEN age >= 30 THEN 1 END) AS teachers_age_30_and_above
FROM teacher;

SELECT name, age, salary
FROM teacher
ORDER BY CASE
             WHEN salary >= 100000 THEN 1
             WHEN salary >= 50000 THEN 2
             ELSE 3
         END, name;

SELECT name, UPPER(name) AS uppercase_name
FROM teacher;

SELECT name, LOWER(name) AS lowercase_name
FROM teacher;

SELECT name, INITCAP(name) AS formatted_name