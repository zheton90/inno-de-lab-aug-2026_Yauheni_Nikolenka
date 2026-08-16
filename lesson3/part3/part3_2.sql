SELECT
	item,
	count(*),
	AVG(o.amount) avg_amount
FROM
	 orders o
GROUP BY item