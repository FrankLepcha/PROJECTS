-- ORDER BY

-- SELECT *
-- FROM customers
-- order by state DESC , first_name asc

-- select first_name, last_name
-- from customers
-- order by birth_date

-- exercise

-- select order_id, product_id, quantity, unit_price
-- from order_items
-- where order_id = 2
-- order by quantity * unit_price DESC

-- Limits - limit is always at the end
-- Get the top three loyal customers
-- select *
-- from customers
-- order by points desc
-- limit 3

-- Inner join 
-- select *
-- From orders
-- Inner Join customers 
-- on orders.customer_id = customers.customer_id

-- select order_id,o.customer_id, first_name, last_name
-- From orders o
-- Inner Join customers c
-- on o.customer_id = c.customer_id

-- select *
-- From order_items o 
-- inner join products p
-- on o.product_id = p.product_id

-- joining multiple tables
-- Use sql_store;
-- from orders o
-- join customers c
	-- on o.customer_id = c.customer_id
-- join order_statuses os
	-- on o.status = os.order_status_id
    

-- USE sql_invoicing;

-- select p.date, c.name as client, p.amount, pm.name

-- from payments p
-- join clients c
	-- on p.client_id = c.client_id
-- join payment_methods pm
	-- on p.payment_method = pm.payment_method_id
    

-- join outer tables with multiple collums


    

