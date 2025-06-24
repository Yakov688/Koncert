select customer_id, order_date
from customers
join orders using(customer_id)
where customers.name = 'Ivan Ivanov';

select product_name, quantity, price
from order_items
join orders using(order_id)
where order_id = 1
order by price desc;


select customers.name, sum(quantity * price) as total_spent
from customers
join orders using(customer_id)
join order_items using(order_id)
group by customers.name
having sum(quantity * price) > 5000;