SELECT
	item,
	count(*),
	AVG(o.amount) avg_mount
FROM
	 orders o
GROUP BY item