
ALTER TABLE student
ADD CONSTRAINT fk_student_department
FOREIGN KEY (id)
REFERENCES teacher (id);

UPDATE student
SET id = CASE
    WHEN roll = '13' THEN 1
    WHEN roll = '15' THEN 2
    WHEN roll = '45' THEN 3
    WHEN roll = '16' THEN 4
END
WHERE roll IN ('13', '15', '45', '16');

SELECT student.id AS std_id, teacher.id AS tech_id
FROM teacher
INNER JOIN student ON teacher.id = student.id;

SELECT student.id AS std_id, teacher.id AS teach_id
FROM student
LEFT JOIN teacher ON teacher.id = student.id;

SELECT *
FROM student
LEFT JOIN teacher ON teacher.id = student.id;

INSERT INTO student
VALUES ('shiv', '89', 8, 5);

SELECT *
FROM teacher
LEFT JOIN student ON teacher.id = student.id;

SELECT student.id AS std_id, teacher.id AS teach_id
FROM teacher
RIGHT JOIN student ON teacher.id = student.id;

SELECT *
FROM teacher
CROSS JOIN student;

INSERT INTO student
VALUES ('lila', '8', 6, 10);

SELECT *
FROM student;

SELECT A.id AS A_id, B.id AS B_id, A.name
FROM teacher A, teacher B
WHERE A.id <> B.id
AND A.name = B.name
ORDER BY A.name;

SELECT teacher.name, teacher.salary, teacher.age
FROM teacher
WHERE salary > 20000;

SELECT teacher.name, teacher.salary, teacher.age
FROM teacher
WHERE name LIKE 'l%';

SELECT teacher.name
FROM teacher
WHERE age IN (21, 26, 29);

SELECT sem, AVG(teacher.id) AS countt
FROM teacher
GROUP BY sem
ORDER BY AVG(teacher.id) DESC;

SELECT teacher.age, teacher.name, AVG(salary) AS average
FROM teacher
GROUP BY teacher.age, teacher.name
ORDER BY AVG(salary) ASC;

CREATE INDEX in_name ON teacher(name);

DROP INDEX in_name;

SELECT name
FROM teacher
WHERE name = 'lo';

SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
ORDER BY tablename, indexname;

CREATE VIEW age_Salary AS
SELECT age, salary, name
FROM teacher
WHERE age > 25;

SELECT *
FROM age_salary;

CREATE INDEX idx_hash
ON student USING HASH (roll);

SELECT studentname
FROM student
WHERE roll = '10';

CREATE TRIGGER ins_
BEFORE INSERT ON student
FOR EACH ROW
EXECUTE FUNCTION ins_();

UPDATE teacher
SET salary = salary + (SELECT AVG(salary) FROM teacher)
WHERE id = 2
RETURNING *;

SELECT *
FROM teacher;
