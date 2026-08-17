-- SELECT Bob Johnson projects > 150

SELECT p.projectname
FROM projects p
INNER JOIN employeeprojects e2
	ON p.projectid  = e2.projectid
INNER JOIN employees e
	ON e.employeeid = e2.employeeid
WHERE e.firstname = 'Bob'
AND e.lastname = 'Johnson'
AND e2.hoursworked > 150

-- BUDGET UP

UPDATE projects p
SET budget = p.budget * 1.1
WHERE EXISTS (
    SELECT 1
    FROM employees e
    INNER JOIN employeeprojects e2 ON e2.employeeid = e.employeeid
    WHERE e.department = 'Senior IT'
    AND e2.projectid = p.projectid
);

-- add end of project

UPDATE projects p
SET enddate = p.startdate + INTERVAL '1 year'
WHERE p.enddate IS NULL

-- add new employee to project Website Redesign

BEGIN;

WITH insert_employee AS(
	INSERT INTO employees (firstname, lastname, department, salary, email)
	VALUES ('Sid', 'Sidorov', 'TESTING', 42000, 'SidSidorov@gmail.com')
	RETURNING employeeid
)
INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
SELECT
	insert_employee.employeeid,
	(
	SELECT
		projectid
	FROM
		projects p
	WHERE
		projectname = 'Website Redesign'
	),
	80
FROM insert_employee;

COMMIT;