select 
    date_format(combined.sales_date, '%Y-%m-%d') sales_date,
    combined.product_id,
    combined.user_id,
    combined.sales_amount
from (
    select 
        sales_date,
        product_id,
        user_id,
        sales_amount from online_sale
    union all
    select 
        sales_date, 
        product_id,
        NULL,
        sales_amount from offline_sale
) as combined
where combined.sales_date like '2022-03%'
order by sales_date, product_id, user_id;