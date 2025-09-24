## Events

**Description:** User activity events on the website (browsing, cart actions, purchases).  
**Primary Key:** `event_id`  
**Relationships:**  
- `events.user_id` → `users.id`  
- `events.product_id` → `products.id`

| Column | Type | Description |
|--------|------|-------------|
| event_id | STRING/INT | Unique event identifier |
| user_id | STRING/INT | FK to `users.id` |
| product_id | STRING/INT | FK to `products.id` |
| sequence_number | INT | Event sequence in session |
| event_type | STRING | Type of event (view, add_to_cart, purchase, etc.) |
| created_at | TIMESTAMP | Timestamp of event |
| traffic_source | STRING | Source channel |
| user_agent | STRING | Browser/user agent |