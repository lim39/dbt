SELECT customer_id, customer_name, signup_date
FROM snowflake_raw.customers
WHERE is_active = TRUE
