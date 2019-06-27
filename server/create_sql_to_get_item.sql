SELECT stores.store_name, stores.markup * item.wsp 
FROM stores 
JOIN item 
ON item.item_id = stores.item_id
