##  Introduction to DBMS

<p>I studied the fundamentals of <b>DBMS (Database Management System)</b>, including its basic concepts, architecture, schemas, database models, and the advantages of using a DBMS over traditional file systems.</p>

### Database Schema

<p>I learned about a database schema and its different types:</p>

<ul>
<li><b>Physical Schema:</b> Describes how data is physically stored.</li>
<li><b>Logical Schema:</b> Describes the structure of tables, attributes, relationships, and constraints.</li>
<li><b>External Schema:</b> Describes the specific views of the database available to different users.</li>
</ul>

### Basic DBMS Architecture

<p>I studied the three-schema architecture of DBMS:</p>

<ul>
<li><b>External Level:</b> User-specific views of the database.</li>
<li><b>Conceptual Level:</b> The overall logical structure of the database.</li>
<li><b>Internal Level:</b> The physical storage of database data.</li>
</ul>

<p>I also learned about <b>one-tier, two-tier, and three-tier architectures</b>, which describe how the database, application, and user interface are organized.</p>

### Why We Use DBMS Instead of Traditional File Systems

<p>I studied the advantages of using a DBMS over traditional file systems, including:</p>

<ul>
<li>Reduced data redundancy and inconsistency.</li>
<li>Improved data security and access control.</li>
<li>Data integrity through constraints.</li>
<li>Concurrent access by multiple users.</li>
<li>Backup and recovery facilities.</li>
<li>Transaction management and data consistency.</li>
<li>Efficient querying and data retrieval.</li>
</ul>

### Basic DBMS Terminology

<p>I learned the following fundamental database terms:</p>

<ul>
<li><b>Database:</b> An organized collection of data.</li>
<li><b>Table:</b> Data organized into rows and columns.</li>
<li><b>Tuple:</b> A row in a relational table.</li>
<li><b>Attribute:</b> A column in a relational table.</li>
<li><b>Domain:</b> The permitted set of values for an attribute.</li>
<li><b>Primary Key:</b> Uniquely identifies each row.</li>
<li><b>Foreign Key:</b> Establishes a relationship between tables.</li>
<li><b>Candidate Key:</b> A minimal set of attributes that uniquely identifies a row.</li>
<li><b>Super Key:</b> A set of attributes that uniquely identifies a row.</li>
<li><b>Composite Key:</b> A key consisting of two or more attributes.</li>
<li><b>NULL:</b> Represents a missing or unknown value.</li>
<li><b>Transaction:</b> A logical unit of database operations.</li>
</ul>

## 13. Functional Dependencies

<p>I studied <b>functional dependencies</b> and their different types, including their notation and examples.</p>

<p>Notation: <code>A → B</code> means that attribute A functionally determines attribute B.</p>

<ul>
<li><b>Trivial Functional Dependency:</b> The right-hand side is a subset of the left-hand side. Example: <code>{StudentID, Name} → Name</code>.</li>
<li><b>Non-Trivial Functional Dependency:</b> The right-hand side is not a subset of the left-hand side. Example: <code>StudentID → Name</code>.</li>
<li><b>Full Functional Dependency:</b> An attribute depends on the entire composite determinant. Example: <code>{StudentID, CourseID} → Grade</code>, assuming neither attribute alone determines Grade.</li>
<li><b>Partial Dependency:</b> An attribute depends on only part of a composite key. Example: <code>{StudentID, CourseID} → StudentName</code>, where <code>StudentID → StudentName</code>.</li>
<li><b>Transitive Dependency:</b> One attribute determines another through an intermediate attribute. Example: <code>StudentID → DepartmentID</code> and <code>DepartmentID → DepartmentName</code>.</li>
</ul>

## 14. Database Normalization

<p>I studied database normalization up to <b>Third Normal Form (3NF)</b> and also learned the basic concept of <b>Boyce-Codd Normal Form (BCNF)</b>.</p>

### First Normal Form (1NF)

<p>I learned to organize tables so that each cell contains a single atomic value and repeating groups are removed.</p>

<b>Before 1NF</b>

| StudentID | Name | Subjects |
|---|---|---|
| 1 | Aqsa | SQL, Python |

<b>After 1NF</b>

| StudentID | Name | Subject |
|---|---|---|
| 1 | Aqsa | SQL |
| 1 | Aqsa | Python |

### Second Normal Form (2NF)

<p>I learned that a table must be in 1NF and have no partial dependencies of non-key attributes on a candidate key.</p>

<b>Before 2NF</b>

| StudentID | CourseID | StudentName | Grade |
|---|---|---|---|
| 1 | C101 | Aqsa | A |
| 1 | C102 | Aqsa | B |

<p>Here, the composite key is <code>(StudentID, CourseID)</code>, but <code>StudentName</code> depends only on <code>StudentID</code>.</p>

<b>After 2NF</b>

<p><b>Students</b></p>

| StudentID | StudentName |
|---|---|
| 1 | Aqsa |

<p><b>Enrollments</b></p>

| StudentID | CourseID | Grade |
|---|---|---|
| 1 | C101 | A |
| 1 | C102 | B |

### Third Normal Form (3NF)

<p>I learned that a table must be in 2NF and have no transitive dependencies of non-key attributes on candidate keys.</p>

<b>Before 3NF</b>

| StudentID | DepartmentID | DepartmentName |
|---|---|---|
| 1 | D01 | Computer Science |
| 2 | D02 | Mathematics |

<p>Here, <code>StudentID → DepartmentID</code> and <code>DepartmentID → DepartmentName</code>.</p>

<b>After 3NF</b>

<p><b>Students</b></p>

| StudentID | DepartmentID |
|---|---|
| 1 | D01 |
| 2 | D02 |

<p><b>Departments</b></p>

| DepartmentID | DepartmentName |
|---|---|
| D01 | Computer Science |
| D02 | Mathematics |

### Boyce-Codd Normal Form (BCNF)

<p>I also studied BCNF, which requires every determinant in a non-trivial functional dependency to be a super key.</p>

<p>Example: In a table <code>Student(StudentID, Advisor, Office)</code>, if <code>Advisor → Office</code> and Advisor is not a super key, the relation violates BCNF. We can decompose it into <code>AdvisorOffice(Advisor, Office)</code> and <code>StudentAdvisor(StudentID, Advisor)</code>, assuming the stated dependency holds.</p>

## 15. Functional Dependency Rules

<p>I studied the basic inference rules and derived rules used to identify functional dependencies.</p>

<ul>
<li><b>Reflexivity:</b> If B is a subset of A, then A determines B. Example: <code>{StudentID, Name} → Name</code>.</li>
<li><b>Augmentation:</b> If <code>A → B</code>, then <code>AC → BC</code>. Example: If <code>StudentID → Name</code>, then <code>(StudentID, CourseID) → (Name, CourseID)</code>.</li>
<li><b>Transitivity:</b> If <code>A → B</code> and <code>B → C</code>, then <code>A → C</code>. Example: <code>StudentID → DepartmentID</code> and <code>DepartmentID → DepartmentName</code> imply <code>StudentID → DepartmentName</code>.</li>
<li><b>Union:</b> If <code>A → B</code> and <code>A → C</code>, then <code>A → BC</code>. Example: <code>StudentID → Name</code> and <code>StudentID → Age</code> imply <code>StudentID → {Name, Age}</code>.</li>
<li><b>Decomposition:</b> If <code>A → BC</code>, then <code>A → B</code> and <code>A → C</code>. Example: <code>StudentID → {Name, Age}</code> implies <code>StudentID → Name</code> and <code>StudentID → Age</code>.</li>
<li><b>Pseudotransitivity:</b> If <code>A → B</code> and <code>BC → D</code>, then <code>AC → D</code>. Example: <code>StudentID → DepartmentID</code> and <code>(DepartmentID, CourseID) → Instructor</code> imply <code>(StudentID, CourseID) → Instructor</code>.</li>
<li><b>Composition:</b> If <code>A → B</code> and <code>C → D</code>, then <code>AC → BD</code>. Example: <code>StudentID → Name</code> and <code>CourseID → CourseName</code> imply <code>(StudentID, CourseID) → (Name, CourseName)</code>.</li>
</ul>

## 16. Types of Databases

<p>I studied different types of databases, their names, and their basic characteristics.</p>

<ul>
<li><b>Relational Database:</b> Organizes data into tables with rows and columns.</li>
<li><b>NoSQL Database:</b> Supports non-relational data models.</li>
<li><b>Document Database:</b> Stores data as documents, often JSON-like structures.</li>
<li><b>Key-Value Database:</b> Stores data as key-value pairs.</li>
<li><b>Redis:</b> An in-memory data store commonly used for caching and key-value operations.</li>
<li><b>Column-Family Database:</b> Organizes data into rows and column families.</li>
<li><b>Graph Database:</b> Stores entities and their relationships as nodes and edges.</li>
<li><b>Time-Series Database:</b> Optimized for timestamped data.</li>
<li><b>Object-Oriented Database:</b> Stores data as objects.</li>
<li><b>Hierarchical Database:</b> Organizes records in a tree-like structure.</li>
<li><b>Network Database:</b> Organizes records using interconnected relationships.</li>
<li><b>In-Memory Database:</b> Stores and processes data primarily in main memory.</li>
<li><b>Distributed Database:</b> Stores data across multiple interconnected locations or machines.</li>
<li><b>Cloud Database:</b> Hosted on cloud infrastructure.</li>
<li><b>Multi-Tier Database Architecture:</b> Separates the user interface, application logic, and data layer into different tiers.</li>
</ul>

<p><b>Note:</b> These categories overlap. Redis is a specific data store rather than a separate database model, and NoSQL is an umbrella category that includes document, key-value, column-family, and graph databases. Multi-tier describes an architecture rather than a database type.</p>

Transactions and ACID Properties

<p>I studied <b>database transactions</b>, their basic operations, and the <b>ACID properties</b> that help maintain data consistency and reliability during database operations.</p>

Database Transactions

<p>I learned about transaction commands such as <b>BEGIN</b>, <b>COMMIT</b>, <b>ROLLBACK</b>, and <b>SAVEPOINT</b>.</p>

<ul>
<li><b>BEGIN:</b> Starts a transaction.</li>
<li><b>COMMIT:</b> Saves the changes made during a transaction.</li>
<li><b>ROLLBACK:</b> Undoes uncommitted changes.</li>
<li><b>SAVEPOINT:</b> Creates a point within a transaction to which we can roll back.</li>
</ul>

<b>Example:</b>

START TRANSACTION;

UPDATE Accounts
SET balance = balance - 1000
WHERE account_id = 1;

UPDATE Accounts
SET balance = balance + 1000
WHERE account_id = 2;

COMMIT;

<p>This example transfers 1000 from one account to another and commits the changes as a transaction.</p>

<b>Example using ROLLBACK:</b>

START TRANSACTION;

UPDATE Accounts
SET balance = balance - 1000
WHERE account_id = 1;

ROLLBACK;

<p>The uncommitted update is undone when the rollback succeeds.</p>

ACID Properties

<p>I studied the four ACID properties of database transactions:</p>

<ul>
<li><b>Atomicity:</b> A transaction is completed entirely or not at all.</li>
<li><b>Consistency:</b> A transaction preserves database rules and integrity constraints.</li>
<li><b>Isolation:</b> Concurrent transactions are controlled so they do not interfere improperly with one another.</li>
<li><b>Durability:</b> Once a transaction is committed, its changes are designed to persist even after a system failure.</li>
</ul>

<b>Example:</b>

<p>During a bank transfer, money should be deducted from one account and added to another. If the operation fails before completion, the transaction should be rolled back to prevent an incomplete transfer.</p>