## Order_Items

**Description:** Individual items per order.  
**Primary Key:** `order_item_id`  
**Relationships:**  
- `order_items.order_id` → `orders.order_id`  
- `order_items.product_id` → `products.id`  
- `order_items.inventory_item_id` → `inventory_items.id`

| Column | Type | Description |
|--------|------|-------------|
| order_item_id | STRING/INT | Unique line-item identifier |
| order_id | STRING/INT | FK to `orders.order_id` |
| product_id | STRING/INT | FK to `products.id` |
| inventory_item_id | STRING/INT | FK to `inventory_items.id` |
| sale_price | FLOAT | Sale price at purchase |
| quantity | INT | Number of units |
| status | STRING | Item status (e.g., Sold, Returned) |