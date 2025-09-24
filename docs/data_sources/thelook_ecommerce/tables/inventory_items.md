## Inventory_Items

**Description:** Tracks product inventory across warehouses and lifecycle of stock.  
**Primary Key:** `id`  
**Relationships:**  
- `inventory_items.product_id` → `products.id`  
- `inventory_items.distribution_center_id` → `distribution_centers.id`  
- `order_items.inventory_item_id` → `inventory_items.id`

| Column | Type | Description |
|--------|------|-------------|
| id | STRING/INT | Unique inventory item identifier |
| product_id | STRING/INT | FK to `products.id` |
| warehouse_id | STRING/INT | Warehouse reference |
| distribution_center_id | STRING/INT | FK to `distribution_centers.id` |
| created_at | TIMESTAMP | Stock creation timestamp |
| sold_at | TIMESTAMP | When the item was sold |