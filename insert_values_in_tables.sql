insert into customers (name, email)
values
('Ivan Ivanov', 'IvanIvanov@mail.ru'),
('Dima Gavrilov', 'DimaGavrilov@mail.ru'),
('Anna Cramling', 'AnnaCramling@mail.ru');

insert into orders (customer_id, order_date)
values
(1, '2024-06-21'),
(1, '2024-06-22'),
(2, '2025-05-13');

insert into order_items(order_id, product_name, quantity, price)
values
(1, 'Lays', 2, 200),
(1, 'Pepsi', 3, 450),
(2, 'Airpods', 1, 11000),
(2, 'MacBook', 1, 23000),
(3, 'War_and_Peace', 1, 20);