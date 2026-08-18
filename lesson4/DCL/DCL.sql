-- CREATE USER

CREATE USER hr_user WITH PASSWORD 'hr_user123'

-- GRANT

GRANT SELECT ON employees TO hr_user

-- SELECT for hr_user

SELECT *
FROM employees

-- INSERT for hr_user

INSERT INTO employees (FirstName, LastName, Department, Salary, email) VALUES
('Vasy', 'Vasilev', 'HR', 34000.00, 'VasyVasilev@gmail.com');

-- GRANT INSERT, UPDATE

GRANT INSERT, UPDATE ON employees TO hr_user

-- INSERT for hr_user

INSERT INTO employees (FirstName, LastName, Department, Salary, email) VALUES
('Vasy', 'Vasilev', 'HR', 34000.00, 'VasyVasilev@gmail.com');

-- UPDATE for hr_user

UPDATE employees
SET department = 'Sales'
WHERE employeeid = 8