-- UPDATE salary for HR

UPDATE employees e
SET salary = e.salary * 1.1
WHERE department = 'HR'

-- UPDATE department

UPDATE employees e
SET department = 'Senior IT'
WHERE salary > 70000

-- DELETE

DELETE FROM employees e1
WHERE NOT EXISTS (
SELECT 1
FROM employeeprojects e2
WHERE e1.employeeid = e2.employeeid
)



BEGIN;

WITH inserted_project AS (
    INSERT INTO projects (projectName, budget, startdate, enddate)
    VALUES ('XXX', 140000, '2026-09-01', '2027-04-15')
    RETURNING projectid
)
INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
SELECT employee_list.emp_id, inserted_project.projectid, employee_list.hours
FROM inserted_project,
     (VALUES
        (1, 40),
        (2, 60)
     ) AS employee_list(emp_id, hours);

COMMIT;

-- BEGIN;
--
-- INSERT INTO projects (projectid, projectName, budget, startdate, enddate)
--     VALUES (5, 'Server Upgrade', 110000, '2024-06-10', '2025-01-20');
--
-- INSERT INTO employeeprojects (employeeid, projectid, hoursworked)
-- VALUES
--     (1, 5, 50),
--     (2, 5, 70);
--
-- COMMIT;