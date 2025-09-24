## Users

**Description:** Contains customer profile data.  
**Primary Key:** `id`  
**Relationships:**  
- `users.id` → `orders.user_id`  
- `users.id` → `events.user_id`

| Column | Type | Description |
|--------|------|-------------|
| id | STRING/INT | Unique user identifier |
| first_name | STRING | First name |
| last_name | STRING | Last name |
| email | STRING | Email address |
| gender | STRING | Gender (e.g., Male, Female, Other) |
| age | INT | Age in years |
| country | STRING | Country |
| city | STRING | City |
| created_at | TIMESTAMP | Account creation timestamp |
| traffic_source | STRING | Acquisition channel (e.g., Search, Ad, Organic) |
| latitude | FLOAT | Latitude (geo) |
| longitude | FLOAT | Longitude (geo) |
