select cart_id
from 
(
    select distinct cart_id, name
    from cart_products
    where name = "Yogurt" or name = "Milk"
) as b
group by b.cart_id
having count(b.cart_id) >= 2
order by cart_id