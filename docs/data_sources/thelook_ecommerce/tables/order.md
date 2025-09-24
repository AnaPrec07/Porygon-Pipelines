## Orders

**Description:** Order-level data containing lifecycle and customer association.  
**Primary Key:** `order_id`  
**Relationships:**  
- `orders.order_id` → `order_items.order_id`  
- `orders.user_id` → `users.id`

| Column | Type | Description |
|--------|------|-------------|
| order_id | STRING/INT | Unique order identifier |
| user_id | STRING/INT | FK to `users.id` |
| status | STRING | Order status (Completed, Returned, Cancelled, etc.) |
| created_at | TIMESTAMP | When order was created |
| shipped_at | TIMESTAMP | Shipment timestamp |
| delivered_at | TIMESTAMP | Delivery timestamp |
| num_items | INT | Number of items in the order |