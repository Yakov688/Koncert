create table customers
(
	customer_id int generated always as identity primary key,
	name varchar(30) not null,
	email char(100) not null unique
);

create table orders
(
	order_id int generated always as identity primary key,
	customer_id int references customers(customer_id),
	order_date date
);

create table order_items
(
	order_items_id int generated always as identity primary key,
	order_id int references orders(order_id),
	product_name char(100) not null,
	quantity int check(quantity >= 0),
	price real check(price >= 0)
);