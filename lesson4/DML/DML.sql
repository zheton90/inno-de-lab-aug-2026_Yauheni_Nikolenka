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
	firstname = 'Alice'
    AND lastname = 'Smith'

-- DELETE

DELETE FROM employees
WHERE
	firstname = 'Eve'
    AND lastname = 'Davis'

-- SELECT

SELECT *
FROM employees