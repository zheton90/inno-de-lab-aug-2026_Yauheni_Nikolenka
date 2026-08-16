SELECT
	country,
	count(*)
FROM
	customers c
GROUP BY country