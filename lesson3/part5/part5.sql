SELECT
	c.first_name,
	c.last_name,
	o.amount
FROM
	 customers c
INNER JOIN orders o
     ON c.customer_id = o.customer_id
WHERE o.amount = (
	SELECT MAX(amount)
	FROM orders
)