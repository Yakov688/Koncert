BEGIN;
	insert into orders (customer_id, order_date)
	values (87, '2025-01-15');

  	insert into order_items (order_id, product_name, quantity, price)
	values
	(53, 'Productxccv', 2, 44),
	(54, 'Productxcv', 2, 344),
	(55, null, 5, 12344),
	(56, 'Productxcacv', 2, 2344),
	(57, 'Productxccbv', 2, 1344);
	ROLLBACK;
COMMIT;

select * from orders where customer_id = 87 and order_date = '2025-01-15'