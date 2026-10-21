<h2>PostgreSQL Practice</h2>

<p>Today, I practised different PostgreSQL aggregate functions, CASE expressions, and string manipulation functions using the existing teacher table.</p>

<h3>1. Aggregate Functions</h3>

<p>I practised aggregate functions to calculate summary information from table records.</p>

<ul>
<li><b>COUNT():</b> Counts the number of records.</li>
<li><b>SUM():</b> Calculates the total salary.</li>
<li><b>AVG():</b> Calculates the average salary.</li>
<li><b>MIN() and MAX():</b> Find the minimum and maximum values.</li>
<li><b>STDDEV() and VARIANCE():</b> Calculate standard deviation and variance.</li>
<li><b>STDDEV_POP() and VAR_POP():</b> Calculate population standard deviation and variance.</li>
<li><b>PERCENTILE_CONT():</b> Calculates percentiles, including the median.</li>
<li><b>STRING_AGG():</b> Combines multiple values into a single string.</li>
<li><b>ARRAY_AGG():</b> Collects values into an array.</li>
<li><b>JSON_AGG():</b> Combines records into a JSON array.</li>
</ul>

<h3>2. GROUP BY and HAVING</h3>

<p>I practised grouping records using <code>GROUP BY</code> and filtering grouped results using <code>HAVING</code>. I also used conditional aggregation with <code>FILTER</code> to count records that satisfy specific conditions.</p>

<h3>3. CASE Expressions</h3>

<p>I learned how to use CASE expressions to return different results based on conditions. I practised classifying salaries into categories, checking specific age values, calculating conditional totals and counts, and applying custom sorting.</p>

<h3>4. Uppercase and Lowercase Functions</h3>

<ul>
<li><b>UPPER():</b> Converts text into uppercase.</li>
<li><b>LOWER():</b> Converts text into lowercase.</li>
<li><b>INITCAP():</b> Capitalizes the first letter of each word.</li>
</ul>

<p>I also used these functions with filtering conditions to search for names without depending on their original letter case.</p>

<h3>5. String and Character Functions</h3>

<ul>
<li><b>CONCAT():</b> Combines multiple values into a string.</li>
<li><b>CONCAT_WS():</b> Combines values using a specified separator.</li>
<li><b>SUBSTRING():</b> Extracts a part of a string.</li>
<li><b>LENGTH() and CHAR_LENGTH():</b> Calculate the number of characters in a string.</li>
<li><b>LPAD() and RPAD():</b> Add padding characters to the left or right of a string.</li>
<li><b>TRIM():</b> Removes surrounding spaces.</li>
<li><b>REPLACE():</b> Replaces specified characters or text.</li>
<li><b>POSITION():</b> Finds the position of a character or substring.</li>
<li><b>REVERSE():</b> Reverses a string.</li>
<li><b>LEFT() and RIGHT():</b> Extract characters from the beginning or end of a string.</li>
</ul>

<h3>6. Practical Implementation</h3>

<p>I combined aggregate functions, CASE expressions, string functions, filtering conditions, grouping, and sorting in SQL queries. These exercises helped me understand how to calculate summaries, categorize records, manipulate text, and display database information in different formats.</p>