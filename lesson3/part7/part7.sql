SELECT
	c.first_name || ' ' || c.last_name AS full_name,
	c.country ,
	SUM(o.amount) total_amount,
	count(*) total_orders
FROM
	 customers c
INNER JOIN orders o
     ON c.customer_id = o.customer_id
WHERE EXISTS (
	SELECT
	FROM shippings s
	WHERE c.customer_id = s.customer
	   AND s.status = 'Delivered'
)
GROUP BY  c.customer_id
HAVING count(*) > 1