create index customer_id_idx on orders(customer_id);
create index order_id_price_idx on order_items(order_id, price);
create index product_name_idx on order_items(product_name);