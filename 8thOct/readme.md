# SQL and DBMS Learning Notes

## 1. Introduction to SQL

<p>I studied the basics of <b>SQL (Structured Query Language)</b>, including its syntax and how it is used to create, retrieve, modify, and manage data stored in relational databases.</p>

<p>I also learned about the different categories of SQL commands:</p>

<ul>
<li><b>DDL (Data Definition Language):</b> CREATE, ALTER, DROP, TRUNCATE.</li>
<li><b>DML (Data Manipulation Language):</b> INSERT, UPDATE, DELETE.</li>
<li><b>DQL (Data Query Language):</b> SELECT.</li>
<li><b>DCL (Data Control Language):</b> GRANT, REVOKE.</li>
<li><b>TCL (Transaction Control Language):</b> COMMIT, ROLLBACK, SAVEPOINT.</li>
</ul>

<p>I also studied the basic syntax of SQL statements and practiced writing queries to perform database operations.</p>

## 2. CRUD Operations

<p>I learned about CRUD operations: Create, Read, Update, and Delete. I practiced these operations using SQL queries.</p>

<b>CREATE (INSERT)</b>

```sql
INSERT INTO Employees (id, name, salary)
VALUES (1, 'Aqsa', 30000);
```

<b>READ (SELECT)</b>

```sql
SELECT * FROM Employees;

SELECT name, salary
FROM Employees
WHERE salary > 20000;
```

<b>UPDATE</b>

```sql
UPDATE Employees
SET salary = 35000
WHERE id = 1;
```

<b>DELETE</b>

```sql
DELETE FROM Employees
WHERE id = 1;
```

## 3. SQL Constraints

<p>I studied SQL constraints, including their syntax and how to apply them when creating database tables.</p>

<ul>
<li><b>NOT NULL</b></li>
<li><b>UNIQUE</b></li>
<li><b>PRIMARY KEY</b></li>
<li><b>FOREIGN KEY</b></li>
<li><b>CHECK</b></li>
<li><b>DEFAULT</b></li>
</ul>

<b>Example:</b>

```sql
CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    salary DECIMAL(10, 2) DEFAULT 0
);
```

<b>Foreign Key Example:</b>

```sql
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
);
```

## 4. Database Anomalies

<p>I studied the three types of database anomalies that can occur in poorly structured or redundant databases.</p>

<ul>
<li><b>Insertion Anomaly</b></li>
<li><b>Update Anomaly</b></li>
<li><b>Deletion Anomaly</b></li>
</ul>

<p>I also learned how database normalization helps reduce data redundancy and prevent these anomalies.</p>

## 5. ER Diagrams

<p>I studied Entity-Relationship (ER) diagrams and practiced identifying entities, attributes, relationships, and cardinality.</p>

<p>I learned two ER diagram notations:</p>

<ul>
<li><b>Chen Notation:</b> Entities are represented by rectangles, attributes by ovals, and relationships by diamonds.</li>
<li><b>Crow's Foot Notation:</b> Entities are represented using table-like boxes, while relationship lines and their end symbols indicate cardinality and optionality.</li>
</ul>

<b>Important Symbols in Chen Notation</b>

<ul>
<li>Rectangle — Entity</li>
<li>Oval — Attribute</li>
<li>Diamond — Relationship</li>
<li>Double Oval — Multivalued Attribute</li>
<li>Dashed Oval — Derived Attribute</li>
<li>Underlined Attribute — Key Attribute</li>
</ul>

<b>Important Symbols in Crow's Foot Notation</b>

<ul>
<li>Vertical line — One</li>
<li>Crow's foot — Many</li>
<li>Circle — Optional participation (zero)</li>
<li>Circle with a crow's foot — Zero or many</li>
<li>Vertical line with a crow's foot — One or many</li>
</ul>

## 6. SQL Joins

<p>I studied different types of SQL joins and practiced writing queries to retrieve data from multiple tables.</p>

<b>Sample Tables:</b>

```sql
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100)
);

CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT
);
```

<b>INNER JOIN</b> — Returns matching records from both tables.

```sql
SELECT Employees.name, Departments.department_name
FROM Employees
INNER JOIN Departments
ON Employees.department_id = Departments.department_id;
```

<b>LEFT JOIN</b> — Returns all records from the left table and matching records from the right table.

```sql
SELECT Employees.name, Departments.department_name
FROM Employees
LEFT JOIN Departments
ON Employees.department_id = Departments.department_id;
```

<b>RIGHT JOIN</b> — Returns all records from the right table and matching records from the left table.

```sql
SELECT Employees.name, Departments.department_name
FROM Employees
RIGHT JOIN Departments
ON Employees.department_id = Departments.department_id;
```

<b>FULL OUTER JOIN</b> — Returns matching and non-matching records from both tables.

```sql
SELECT Employees.name, Departments.department_name
FROM Employees
FULL OUTER JOIN Departments
ON Employees.department_id = Departments.department_id;
```

<b>CROSS JOIN</b> — Returns every possible combination of rows from both tables.

```sql
SELECT Employees.name, Departments.department_name
FROM Employees
CROSS JOIN Departments;
```

<b>SELF JOIN</b> — Joins a table with itself.

```sql
SELECT A.name AS Employee, B.name AS Colleague
FROM Employees A
JOIN Employees B
ON A.department_id = B.department_id
WHERE A.id <> B.id;
```

## 7. SQL Data Types

<p>I studied the different SQL data types used when defining table columns.</p>

<ul>
<li><b>Integer Types:</b> INT, SMALLINT, BIGINT, TINYINT.</li>
<li><b>Decimal Types:</b> DECIMAL, NUMERIC, FLOAT, REAL, DOUBLE.</li>
<li><b>String Types:</b> CHAR, VARCHAR, TEXT.</li>
<li><b>Date and Time Types:</b> DATE, TIME, DATETIME, TIMESTAMP.</li>
<li><b>Boolean Type:</b> BOOLEAN or BIT, depending on the database system.</li>
<li><b>Binary Types:</b> BINARY, VARBINARY, BLOB.</li>
</ul>

<b>Example:</b>

```sql
CREATE TABLE Students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    percentage DECIMAL(5, 2),
    admission_date DATE,
    is_active BOOLEAN
);
```

## 8. Aggregate Functions

<p>I studied SQL aggregate functions and practiced using them to calculate summaries from table data.</p>

<ul>
<li><b>COUNT()</b></li>
<li><b>SUM()</b></li>
<li><b>AVG()</b></li>
<li><b>MIN()</b></li>
<li><b>MAX()</b></li>
</ul>

<b>Examples:</b>

```sql
SELECT COUNT(*) FROM Employees;

SELECT SUM(salary) FROM Employees;

SELECT AVG(salary) FROM Employees;

SELECT MIN(salary) FROM Employees;

SELECT MAX(salary) FROM Employees;
```

<p>I also practiced using aggregate functions with <b>GROUP BY</b> and <b>HAVING</b>.</p>

```sql
SELECT department_id, AVG(salary) AS average_salary
FROM Employees
GROUP BY department_id
HAVING AVG(salary) > 25000;
```

## 9. SQL String Functions

<p>I studied SQL string functions and practiced using them to manipulate and retrieve text data.</p>

<ul>
<li><b>UPPER()</b> — Converts text to uppercase.</li>
<li><b>LOWER()</b> — Converts text to lowercase.</li>
<li><b>LENGTH()</b> — Returns the length of a string in supported database systems.</li>
<li><b>CONCAT()</b> — Combines strings.</li>
<li><b>SUBSTRING()</b> — Extracts part of a string.</li>
<li><b>TRIM()</b> — Removes leading and trailing spaces.</li>
<li><b>REPLACE()</b> — Replaces part of a string.</li>
<li><b>LEFT()</b> and <b>RIGHT()</b> — Extract characters from the beginning or end of a string in supported systems.</li>
</ul>

<b>Examples:</b>

```sql
SELECT UPPER(name) FROM Employees;

SELECT LOWER(name) FROM Employees;

SELECT CONCAT(name, ' - Employee')
FROM Employees;

SELECT SUBSTRING(name, 1, 3)
FROM Employees;

SELECT TRIM('  SQL Learning  ');

SELECT REPLACE('Hello SQL', 'SQL', 'World');
```

<p><b>Note:</b> String function names and syntax can vary between MySQL, PostgreSQL, SQL Server, and other database systems. For example, PostgreSQL commonly uses <code>LENGTH()</code>, while SQL Server uses <code>LEN()</code> for string length.</p>

## 10. SQL Triggers

<p>I studied SQL triggers, including their syntax and an example of automatically executing an action in response to a database event.</p>

<b>Example: MySQL Trigger</b>

```sql
CREATE TABLE Employee_Audit (
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

```sql
DELIMITER //

CREATE TRIGGER after_employee_insert
AFTER INSERT ON Employees
FOR EACH ROW
BEGIN
    INSERT INTO Employee_Audit (message)
    VALUES (
        CONCAT('New employee added: ', NEW.name)
    );
END //

DELIMITER ;
```

<p>This example uses MySQL syntax. The trigger inserts an audit message after a new employee record is added.</p>

## 11. Additional SQL Topics

<p>Along with the topics above, I studied and practiced the following SQL concepts:</p>

<ul>
<li><b>WHERE</b> — Filtering records.</li>
<li><b>ORDER BY</b> — Sorting records.</li>
<li><b>GROUP BY</b> — Grouping records.</li>
<li><b>HAVING</b> — Filtering grouped results.</li>
<li><b>DISTINCT</b> — Retrieving unique values.</li>
<li><b>LIKE</b> — Pattern matching.</li>
<li><b>IN</b> — Matching values from a list.</li>
<li><b>BETWEEN</b> — Filtering within a range.</li>
<li><b>IS NULL</b> — Checking for NULL values.</li>
<li><b>Subqueries</b> — Queries nested inside other queries.</li>
<li><b>Normalization</b> — Organizing data to reduce redundancy.</li>
<li><b>Primary and Foreign Keys</b> — Defining relationships between tables.</li>
</ul>
