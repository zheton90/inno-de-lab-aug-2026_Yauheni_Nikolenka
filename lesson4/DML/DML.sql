-- INSERT

INSERT INTO Employees (FirstName, LastName, Department, Salary) VALUES
('Ivan', 'Ivanov', 'Sales', 50000.00),
('Petr', 'Petrov', 'Finance', 65000.00);

-- SELECT

SELECT *
FROM employees

-- SELECT IT

SELECT
	firstname, lastname
FROM
	employees e
WHERE
	e.department = 'IT'

-- UPDATE

UPDATE
	employees e
SET
	salary = 65000
WHERE
	employeeid = 1

-- DELETE

DELETE FROM employees
WHERE
	employeeid = 5

-- SELECT

SELECT *
FROM employees