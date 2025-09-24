
## 🚚 Distribution_Centers

**Description:** Warehouse and logistics hubs.  
**Primary Key:** `id`  
**Relationships:**  
- `distribution_centers.id` → `inventory_items.distribution_center_id`

| Column | Type | Description |
|--------|------|-------------|
| id | STRING/INT | Unique distribution center identifier |
| name | STRING | Name of the center |
| latitude | FLOAT | Latitude |
| longitude | FLOAT | Longitude |
