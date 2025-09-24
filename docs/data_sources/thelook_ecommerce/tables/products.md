## Products

**Description:** Product catalog with metadata and pricing.  
**Primary Key:** `id`  
**Relationships:**  
- `products.id` → `order_items.product_id`  
- `products.id` → `inventory_items.product_id`

| Column | Type | Description |
|--------|------|-------------|
| id | STRING/INT | Unique product identifier |
| name | STRING | Product name |
| brand | STRING | Brand name |
| category | STRING | Product category |
| price | FLOAT | Retail price |
| cost | FLOAT | Internal cost |
| created_at | TIMESTAMP | When product was added |
| updated_at | TIMESTAMP | Last update |