-- CREATE

CREATE OR REPLACE FUNCTION public.CalculateAnnualBonus(
	p_salary NUMERIC,
	p_employee_id INT
)
RETURNS DECIMAL
AS $$
DECLARE
	v_bonus DECIMAL;
BEGIN
	v_bonus := p_salary * 0.10;
RETURN v_bonus;
END;
$$
LANGUAGE plpgSQL;

-- SHOW BONUS

SELECT
    firstname,
    CalculateAnnualBonus(e.salary, e.employeeid) AS bonus
FROM employees e;

-- CREATE VIEW

CREATE VIEW IT_Department_View
AS
	SELECT
		employeeid,
		firstname,
		lastname,
		salary
	FROM
		employees e
	WHERE
		e.department = 'Senior IT' IT_Department_View

-- SELECT from VIEW

SELECT *
FROM IT_Department_View
