<h2>Topics Learned and Practised in PostgreSQL</h2>

<p>In this practical session, I implemented several SQL concepts in PostgreSQL, including foreign key constraints, UPDATE statements, joins, filtering, aggregate functions, GROUP BY, indexes, views, triggers, and updating records using subqueries. This helped me understand how these concepts work when executing queries against a database.</p>

<h3>1. Foreign Key Constraints</h3>

<p>I used ALTER TABLE to add a foreign key constraint to the existing <code>student</code> table.</p>

<pre><code>ALTER TABLE student
ADD CONSTRAINT fk_student_department
FOREIGN KEY (id)
REFERENCES teacher (id);</code></pre>

<p>A foreign key establishes a relationship between tables and maintains referential integrity by ensuring that referenced values exist in the related table.</p>

<p>In this example, <code>student.id</code> references <code>teacher.id</code>. The constraint is named <code>fk_student_department</code>. Although the constraint name includes "department", the actual relationship is between the student and teacher tables.</p>

<h3>2. Updating Records Using CASE</h3>

<p>I used UPDATE with CASE to assign different ID values to students based on their roll numbers.</p>

<pre><code>UPDATE student
SET id = CASE
    WHEN roll = '13' THEN 1
    WHEN roll = '15' THEN 2
    WHEN roll = '45' THEN 3
    WHEN roll = '16' THEN 4
END
WHERE roll IN ('13', '15', '45', '16');</code></pre>

<p>The CASE expression applies different values according to specified conditions, while the WHERE clause limits the update to the selected roll numbers.</p>

<p>This query changes existing IDs rather than creating new records. Because <code>id</code> is also used as a foreign key in the previous statement, the new values must satisfy that constraint. If the foreign key is already active, PostgreSQL may reject an update that produces a reference to a nonexistent teacher ID.</p>

<h3>3. SQL Joins</h3>

<p>I practised different types of joins to combine records from the <code>student</code> and <code>teacher</code> tables using their ID columns.</p>

<ul>
<li><b>INNER JOIN:</b> Returns only records with matching IDs in both tables.</li>
<li><b>LEFT JOIN:</b> Returns all records from the left table and matching records from the right table. Unmatched right-side columns contain NULL.</li>
<li><b>RIGHT JOIN:</b> Returns all records from the right table and matching records from the left table. Unmatched left-side columns contain NULL.</li>
<li><b>CROSS JOIN:</b> Returns every possible combination of rows from the two tables. If one table has 3 rows and the other has 4, the result contains 12 combinations.</li>
</ul>

<p>I also used table aliases and column aliases to make query results easier to understand.</p>

<pre><code>SELECT student.id AS std_id,
       teacher.id AS tech_id
FROM teacher
INNER JOIN student
ON teacher.id = student.id;</code></pre>

<p>Here, <code>std_id</code> and <code>tech_id</code> are aliases for the selected columns. The ON clause specifies the condition used to match rows.</p>

<p>I also used SELECT * with joins to retrieve all columns from both tables and inspect the combined results.</p>

<h3>4. Inserting Records</h3>

<p>I practised inserting new student records using INSERT INTO.</p>

<pre><code>INSERT INTO student
VALUES ('shiv', '89', 8, 5);</code></pre>

<p>This inserts a row by supplying values in the table's column order. I also inserted another student record to practise adding data and then retrieved the records using SELECT.</p>

<p>For more reliable SQL, it is generally better to specify column names explicitly. The supplied values must also match the table's column count, data types, and constraints.</p>

<h3>5. Self Join</h3>

<p>I used the same <code>teacher</code> table twice in one query, assigning it the aliases <code>A</code> and <code>B</code>.</p>

<pre><code>SELECT A.id AS A_id, B.id AS B_id, A.name
FROM teacher A, teacher B
WHERE A.id <> B.id
AND A.name = B.name
ORDER BY A.name;</code></pre>

<p>This is a self join, which compares rows within the same table. The conditions select pairs of different teacher IDs that have the same name, and ORDER BY sorts the results by name.</p>

<h3>6. Filtering Data with WHERE</h3>

<p>I used the WHERE clause to retrieve records that satisfy particular conditions.</p>

<p><b>Comparison operator:</b> Retrieved teachers whose salary is greater than 20,000.</p>

<pre><code>SELECT teacher.name, teacher.salary, teacher.age
FROM teacher
WHERE salary > 20000;</code></pre>

<p><b>LIKE operator:</b> Retrieved teachers whose names start with the letter 'l'.</p>

<pre><code>SELECT teacher.name, teacher.salary, teacher.age
FROM teacher
WHERE name LIKE 'l%';</code></pre>

<p>The percent sign (<code>%</code>) matches zero or more characters. The underscore (<code>_</code>) matches exactly one character. In PostgreSQL, LIKE is case-sensitive, so this pattern matches lowercase 'l'.</p>

<p><b>IN operator:</b> Retrieved teacher names for records whose ages match one of the specified values.</p>

<pre><code>SELECT teacher.name
FROM teacher
WHERE age IN (21, 26, 29);</code></pre>

<p>The IN operator checks whether a value matches any value in a specified list.</p>

<h3>7. Aggregate Functions and GROUP BY</h3>

<p>I practised using aggregate functions with GROUP BY and ORDER BY to calculate summaries and sort grouped results.</p>

<p><b>Grouping by semester:</b></p>

<pre><code>SELECT sem, AVG(teacher.id) AS countt
FROM teacher
GROUP BY sem
ORDER BY AVG(teacher.id) DESC;</code></pre>

<p>This groups teacher records by semester, calculates the average ID for each group, and sorts the groups by that average in descending order.</p>

<p><b>Grouping by age and name:</b></p>

<pre><code>SELECT teacher.age, teacher.name, AVG(salary) AS average
FROM teacher
GROUP BY teacher.age, teacher.name
ORDER BY AVG(salary) ASC;</code></pre>

<p>This groups records by the combination of age and name, calculates the average salary for each group, and sorts the results in ascending order of average salary.</p>

<p>Although the first query uses the alias <code>countt</code>, AVG calculates an average, not a count. COUNT() should be used when the objective is to count records.</p>

<h3>8. Indexes in PostgreSQL</h3>

<p>I learned how to create and drop indexes and inspect existing indexes using PostgreSQL's system catalog view.</p>

<p><b>Creating an index:</b></p>

<pre><code>CREATE INDEX in_name ON teacher(name);</code></pre>

<p>This creates a B-tree index by default on the teacher name column. An index can help PostgreSQL find matching records more efficiently, depending on the query and data.</p>

<p><b>Dropping an index:</b></p>

<pre><code>DROP INDEX in_name;</code></pre>

<p>This removes the index named <code>in_name</code>.</p>

<p><b>Viewing indexes:</b></p>

<pre><code>SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
ORDER BY tablename, indexname;</code></pre>

<p>The <code>pg_indexes</code> view provides information about indexes in accessible database schemas, including their names, associated tables, and definitions.</p>

<p><b>Hash index:</b></p>

<pre><code>CREATE INDEX idx_hash
ON student USING HASH (roll);</code></pre>

<p>I also explored hash indexes, which are designed for equality comparisons such as <code>roll = '13'</code>. Unlike B-tree indexes, hash indexes are not suitable for range conditions such as greater-than comparisons or BETWEEN.</p>

<h3>9. Views in PostgreSQL</h3>

<p>I created a view named <code>age_Salary</code> to retrieve selected teacher details for teachers older than 25.</p>

<pre><code>CREATE VIEW age_Salary AS
SELECT age, salary, name
FROM teacher
WHERE age > 25;</code></pre>

<p>I then queried the view using SELECT.</p>

<pre><code>SELECT * FROM age_salary;</code></pre>

<p>A view is a named query that presents data from underlying tables. A regular PostgreSQL view stores its definition in the database system catalogs rather than storing a separate copy of the query's result rows. Its definition is represented through catalog information, including <code>pg_class</code> and <code>pg_rewrite</code>.</p>

<h3>10. Triggers and Trigger Functions</h3>

<p>I explored the implementation of a trigger on the <code>student</code> table. A trigger automatically executes a specified function when a particular event occurs, such as inserting, updating, or deleting a record.</p>

<pre><code>CREATE TRIGGER ins_
BEFORE INSERT ON student
FOR EACH ROW
EXECUTE FUNCTION ins_();</code></pre>

<p>This statement creates a BEFORE INSERT trigger that calls the <code>ins_()</code> trigger function for each row