<h2>Topics Learned</h2>


<h3> Establishing a PostgreSQL Connection Using Python</h3>

<p>Learned how to connect a Python application to a PostgreSQL database using <b>psycopg2</b>, a Python adapter that allows Python programs to communicate with PostgreSQL databases and execute SQL queries.</p>

<h3> Understanding the Database Connection Code</h3>

<ul>
<li><b>Importing psycopg2:</b> Imported the library required to establish a connection between Python and PostgreSQL.</li>
<li><b>Creating a Connection Function:</b> Created a <code>get_connection()</code> function to connect to the <code>information_db</code> database using the database name, username, password, host, and port.</li>
<li><b>Exception Handling:</b> Used <code>try</code> and <code>except</code> to handle connection errors. The function returns <code>False</code> if the connection fails.</li>
<li><b>Checking Connection Status:</b> Checked whether the connection was established successfully and displayed an appropriate message.</li>
<li><b>Creating a Cursor:</b> Used <code>conn.cursor()</code> to create a cursor object, which allows SQL commands to be executed through the database connection.</li>
<li><b>Executing SQL Queries:</b> Used <code>curr.execute()</code> to execute SQL statements, including a <code>SELECT</code> query to retrieve records from the <code>student</code> table.</li>
<li><b>Fetching Records:</b> Used <code>curr.fetchall()</code> to retrieve all rows returned by the query.</li>
<li><b>Displaying Results:</b> Iterated through the fetched records using a <code>for</code> loop and printed each row.</li>
<li><b>Closing the Connection:</b> Used <code>conn.close()</code> to close the database connection after completing the operations.</li>
</ul>

<h3> SQL Query Execution and Data Retrieval</h3>

<p>Practised retrieving data from a PostgreSQL table using SQL queries from Python. Learned how Python executes a query, fetches the results, and displays the returned records.</p>

<h3> Key Concepts Learned</h3>

<ul>
<li>PostgreSQL installation and database creation.</li>
<li>Connecting Python to PostgreSQL using psycopg2.</li>
<li>Database connection parameters, including database name, user, password, host, and port.</li>
<li>Cursor creation and SQL query execution.</li>
<li>Fetching and displaying database records.</li>
<li>Basic exception handling and connection management.</li>
</ul>