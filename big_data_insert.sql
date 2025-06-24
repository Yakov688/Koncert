-- Заполнение таблицы customers
DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..10000 LOOP  -- Создаем 10,000 клиентов
        INSERT INTO customers (name, email)
        VALUES (
            'Customer ' || i,
            'customer' || i || '@example.com'
        );
    END LOOP;
END $$;

-- Заполнение таблицы orders
DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..10000 LOOP  -- Создаем 10,000 заказов для клиентов
        INSERT INTO orders (customer_id, order_date)
        VALUES (
            (SELECT customer_id FROM customers ORDER BY RANDOM() LIMIT 1),  -- Случайный клиент
            CURRENT_DATE - (RANDOM() * 365)::int  -- Случайная дата в прошлом году
        );
    END LOOP;
END $$;

-- Заполнение таблицы order_items
DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..1000000 LOOP  -- Создаем 1,000,000 записей в order_items
        INSERT INTO order_items (order_id, product_name, quantity, price)
        VALUES (
            (SELECT order_id FROM orders ORDER BY RANDOM() LIMIT 1),  -- Случайный заказ
            'Product ' || (i % 1000),  -- Название продукта (1000 уникальных продуктов)
            (RANDOM() * 10)::int,  -- Случайное количество от 0 до 10
            (RANDOM() * (100000 - 100) + 100)  -- Случайная цена от 100 до 100000
        );
    END LOOP;
END $$;


