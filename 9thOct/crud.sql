CREATE TABLE teacher (
    id SERIAL PRIMARY KEY ,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    age INT CHECK (age >= 18),
    salary DECIMAL(10, 2) DEFAULT 0
)
INSERT INTO teacher VALUES (3,'pqr','xy@gmail.com', 35, 57000),(4,'op','xyz@gmail.com', 45, 157000),(5,'lo','lo@gmail.com', 25, 25000);

SELECT Distinct(SUM(salary)) FROM teacher;
SELECT SUM(salary) FROM teacher;
SELECT Distinct(AVG(salary)) FROM teacher;

CREATE TABLE Orders (
    OrderID int PRIMARY KEY,
    OrderNumber int NOT NULL,
    PersonID int,
    CONSTRAINT fk_Person
    FOREIGN KEY (PersonID)
    REFERENCES Persons(PersonID)
);
ALTER TABLE student
ADD CONSTRAINT 
FOREIGN KEY (studentname)
REFERENCES student(id);
