# Data Discovery & Dictionary — `thelook_ecommerce`

*Dataset:* `bigquery-public-data.thelook_ecommerce`  
*Purpose:* Synthetic e-commerce dataset modeling users, purchases, inventory, product catalog, and web events. :contentReference[oaicite:0]{index=0}

---

## 🧭 Overview & Business Context

This dataset simulates an e-commerce fashion retailer. It captures customer behavior from site events through orders and inventory. It can be used to explore typical analytics and data science problems: sales performance, churn, product recommendations, funnel analysis, customer segmentation, returns analysis, etc. :contentReference[oaicite:1]{index=1}

Below is a high-level conceptual flow:
users → events → orders → order_items → inventory / products → (distribution_centers)


Customers browse (events), place orders, order items link to products/inventory, and distribution centers / logistics help model delivery and returns.  

---

## 📦 Tables & Key Entities

Below is a listing of the main tables, a description, and example key columns. Use `INFORMATION_SCHEMA.COLUMNS` or BigQuery console to confirm full schemas.

| Table | Description | Key Columns / Relationships | Notes / Use Cases |
|---|---|---|---|
| **users** | Customer profile data | `id` (PK), `first_name`, `last_name`, `email`, `gender`, `age`, `country`, `city`, `created_at`, `traffic_source`, `latitude`, `longitude` | Use this as **dimension** for customer segmentation, demographics, geospatial joins |
| **products** | Product catalog | `id` (PK), `name`, `brand`, `category`, `price`, `cost`, `created_at`, `updated_at` | Product attributes, for joining in sales, recommendation, margin analysis |
| **orders** | Order-level metadata | `order_id` (PK), `user_id` (FK → users.id), `status`, `created_at`, `shipped_at`, `delivered_at`, `num_items` | Use for order funnels, order lifecycle, cancellations/returns |
| **order_items** | Line items per order | `order_item_id` (PK), `order_id` (FK → orders), `product_id` (FK → products), `sale_price`, `quantity`, `status`, `inventory_item_id` | Useful for aggregations (revenue, units sold), linking to inventory, returns, order splits |
| **inventory_items** | Inventory / stock of product across warehouses | `id` (PK), `product_id` (FK → products), `warehouse_id`, `created_at`, `sold_at`, `distribution_center_id` | To track when inventory enters, is sold (for latency or turnover analysis) |
| **distribution_centers** | Locations of logistics / warehouses | `id` (PK), `name`, `latitude`, `longitude` | Useful for spatial analysis: distance to user, delivery modeling, logistics cost |
| **events** | Web / site user events (browse, add-to-cart, purchase) | `event_id` (PK), `user_id` (FK → users), `sequence_number`, `event_type` (view, add_to_cart, purchase, etc.), `product_id`, `created_at`, `traffic_source`, `user_agent` | For funnel analysis, attribution, user behavior flow |

---

## 🔍 Column-Level Dictionary (Example for `users`)

Below is a sample of how you might document one table in detail. Do the same for others in your repo.

| Column | Type | Description | Nullable / Constraints | Business Use |
|---|---|---|---|---|
| `id` | STRING / INT | Unique identifier for user | Not null | Key to join with orders, events |
| `first_name` | STRING | User’s first name | Nullable | Personalization, auditing |
| `last_name` | STRING | User’s last name | Nullable | — |
| `email` | STRING | User’s email address | Nullable | Communication, segmentation |
| `gender` | STRING | Gender of user (e.g. “Male”, “Female”, “Other”) | Nullable | Demographic segmentation |
| `age` | INT | Age in years | Nullable | Age group segmentation |
| `country` | STRING | Country of user | Nullable | Regional analysis |
| `city` | STRING | City name | Nullable | Geospatial / city-level reports |
| `created_at` | TIMESTAMP | When user account was created | Not null | Lifetime, cohort analysis |
| `traffic_source` | STRING | Channel/source by which user arrived | Nullable | Attribution / marketing channel analysis |
| `latitude` | FLOAT | Geographic latitude of user | Nullable | Mapping, distance calculations |
| `longitude` | FLOAT | Geographic longitude of user | Nullable | — |

You should replicate a similar table for **each BigQuery table**.

---

## 🔗 Entity Relationships & ERD

- **users.id** → **orders.user_id**
- **orders.order_id** → **order_items.order_id**
- **order_items.product_id** → **products.id**
- **order_items.inventory_item_id** → **inventory_items.id**
- **inventory_items.product_id** → **products.id**
- **inventory_items.distribution_center_id** → **distribution_centers.id**
- **events.user_id** → **users.id**
- **events.product_id** → **products.id** (for action linking)

You may generate an ERD diagram (e.g. via QuickDBD, draw.io, or graph tools using INFORMATION_SCHEMA queries) to visualize these relationships. :contentReference[oaicite:2]{index=2}

---

## 📊 Derived Metrics / Business Concepts

Here are some core metrics or dimensions you can derive from this dataset:

- **Revenue** = sum of `sale_price` in `order_items` for non-cancelled orders  
- **Units Sold** = sum of `quantity` in `order_items`  
- **Average Order Value (AOV)** = total revenue / number of orders  
- **Repeat Purchase Rate** = percentage of users with >1 order  
- **Customer Lifetime Value (CLV)** = sum of future revenue from user (if model)  
- **Churn / Inactivity** = users who haven’t purchased in last **X** days  
- **Product category performance**: revenue, units by `products.category`  
- **Geographic performance** by `country`, `city`, or distance to distribution center  
- **Funnel metrics**: view → add_to_cart → purchase via `events`  
- **Return rate**: proportion of order_items or orders marked “Returned” (if status exists)  

---

## ⚠️ Limitations & Assumptions

- The data is **synthetic / fictitious**, with no real user identities or personally identifiable data. Use it only for learning, prototyping, and portfolio work. :contentReference[oaicite:3]{index=3}  
- Some timestamps may have **inconsistencies or anomalies** (e.g., negative durations) as noted in explorations. :contentReference[oaicite:4]{index=4}  
- Some columns may have null or missing values (e.g. city, lat/long).  
- The dataset is **static** – it is not continuously updated; thus it serves best for historical analysis, tests, or modeling, not real-time production.  
- Joins are presumed to be many-to-one or one-to-many; be careful with cardinality especially in events or order_items.  
- Be cautious with performance: querying large joins can consume many bytes, so filter early, pick columns, and use query cost estimates in BigQuery.

---

## 🛠️ How to Probe the Schema in BigQuery

You can use the following queries to inspect structure and metadata:

```sql
-- List all tables in dataset
SELECT table_name
FROM `bigquery-public-data.thelook_ecommerce.INFORMATION_SCHEMA.TABLES`
WHERE table_type = 'BASE TABLE';

-- List columns and types for a table, e.g. users
SELECT column_name, data_type, is_nullable
FROM `bigquery-public-data.thelook_ecommerce.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'users'
ORDER BY ordinal_position;

-- Get DDL (creation statement) for all tables
SELECT table_name, ddl
FROM `bigquery-public-data.thelook_ecommerce.INFORMATION_SCHEMA.TABLES`
WHERE table_type = 'BASE TABLE';
