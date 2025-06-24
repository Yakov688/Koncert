drop index customer_id_idx
-- Был удален так как не использовался в select запросе к таблице orders, запрос шел через sequence scan.