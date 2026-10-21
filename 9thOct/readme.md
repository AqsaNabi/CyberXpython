<h2>Topics Learned and Practised</h2>

<h3>1. Practical Implementation of SQL in PostgreSQL</h3>

<p>Practised writing and executing SQL queries in PostgreSQL after learning the theoretical concepts of SQL, including table creation, constraints, aggregate functions, and modifying table structures. This helped me understand how SQL commands work in an actual database environment.</p>

<h3>2. Creating Tables and Applying Constraints</h3>

<p>Created a <code>teacher</code> table in PostgreSQL and applied different constraints to maintain data integrity and define rules for the columns.</p>

<pre><code>CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    salary DECIMAL(10, 2) DEFAULT 0
);</code></pre>

<p><b>Concepts implemented:</b></p>

<ul>
<li><b>SERIAL:</b> Automatically generates sequential integer values for the ID column.</li>
<li><b>PRIMARY KEY:</b> Ensures that every teacher has a unique, non-null identifier.</li>
<li><b>NOT NULL:</b> Ensures that the teacher's name cannot be left empty as a NULL value.</li>
<li><b>UNIQUE:</b> Prevents duplicate non-NULL email values.</li>
<li><b>CHECK:</b> Ensures that the teacher's age is at least 18.</li>
<li><b>DEFAULT:</b> Assigns a salary of 0 when a salary value is not provided during insertion.</li>
<li><b>VARCHAR(100):</b> Stores variable-length character data up to 100 characters.</li>
<li><b>DECIMAL(10, 2):</b> Stores exact numeric values with up to 10 total digits, including 2 digits after the decimal point.</li>
</ul>

<h3>3. Inserting Multiple Records</h3>

<p>Practised inserting multiple records into the <code>teacher</code> table using a single INSERT statement.</p>

<pre><code>INSERT INTO teacher
VALUES
    (3, 'pqr', 'xy@gmail.com', 35, 57000),
    (4, 'op', 'xyz@gmail.com', 45, 157000),
    (5, 'lo', 'lo@gmail.com', 25, 25000);</code></pre>

<p>This helped me understand how to insert multiple rows in one query and provide values for the columns in the correct order.</p>

<h3>4. Aggregate Functions in SQL</h3>

<p>Implemented aggregate functions to calculate summary information from the teacher records, particularly the total and average salary.</p>

<p><b>SUM():</b> Calculates the total salary of all teachers.</p>

<pre><code>SELECT SUM(salary)
FROM teacher;</code></pre>

<p><b>AVG():</b> Calculates the average salary of all teachers.</p>

<pre><code>SELECT AVG(salary)
FROM teacher;</code></pre>

<p><b>DISTINCT with Aggregate Functions:</b> Also experimented with using DISTINCT inside aggregate functions.</p>

<pre><code>SELECT DISTINCT SUM(salary)
FROM teacher;

SELECT DISTINCT AVG(salary)
FROM teacher;</code></pre>

<p>Learned that DISTINCT removes duplicate values from a result set. However, because SUM() and AVG() each return a single aggregate result without GROUP BY, adding DISTINCT to the final result generally does not change the output. To calculate the sum or average of distinct salary values, the correct syntax is <code>SUM(DISTINCT salary)</code> or <code>AVG(DISTINCT salary)</code>.</p>

<h3>5. Creating Tables with Primary and Foreign Keys</h3>

<p>Practised defining relationships between database tables by creating an <code>Orders</code> table with a primary key and a foreign key constraint.</p>

<pre><code>CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    OrderNumber INT NOT NULL,
    PersonID INT,
    CONSTRAINT fk_Person
        FOREIGN KEY (PersonID)
        REFERENCES Persons(PersonID)
);</code></pre>

<p><b>Concepts implemented:</b></p>

<ul>
<li><b>Primary Key:</b> Used <code>OrderID</code> to uniquely identify each order.</li>
<li><b>NOT NULL:</b> Ensured that every order has an order number.</li>
<li><b>Foreign Key:</b> Connected <code>Orders.PersonID</code> to <code>Persons.PersonID</code>, helping maintain referential integrity.</li>
<li><b>Named Constraint:</b> Used <code>fk_Person</code> to give the foreign key constraint a descriptive name.</li>
</ul>

<p>The referenced <code>Persons</code> table must already exist, and <code>PersonID</code> must be a primary key or have a suitable unique constraint.</p>

<h3>6. Altering Tables and Adding Constraints</h3>

<p>Practised modifying an existing table using ALTER TABLE and explored how constraints can be added after a table has been created.</p>

<pre><code>ALTER TABLE student
ADD CONSTRAINT
FOREIGN KEY (studentname)
REFERENCES student(id);</code></pre>

<p>This exercise introduced the process of adding a foreign key to an existing table. However, this particular statement needs correction before it can run successfully: the constraint requires a name in this position, and the referencing and referenced columns must have compatible data types. A self-referencing foreign key is valid only when the intended relationship and existing data satisfy the constraint.</p>

<p>For example, if the intention is to reference the same table's <code>id</code> column from a <code>parent_id</code> column, the table would need a compatible <code>parent_id</code> column:</p>

<pre><code>ALTER TABLE student
ADD CONSTRAINT fk_student_parent
FOREIGN KEY (parent_id)
REFERENCES student(id);</code></pre>

<h3>7. Summary of Practical Learning</h3>

<p>During this session, I applied previously studied SQL concepts in PostgreSQL through practical exercises. I created tables, inserted multiple records, implemented constraints, used aggregate functions, established primary key and foreign key relationships, and explored altering existing tables to add constraints.</p>

<p>This practice helped me connect SQL theory with actual database operations and understand how constraints support data integrity and relationships within a relational database.</p>