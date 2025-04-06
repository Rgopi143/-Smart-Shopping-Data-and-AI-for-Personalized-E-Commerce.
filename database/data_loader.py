from database.db import get_connection

def insert_sample_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT OR IGNORE INTO customers (id, name) VALUES (?, ?)", (1, "Alice"))

    products = [
        (101, "Shoes", "Footwear"),
        (102, "T-shirt", "Apparel"),
        (103, "Socks", "Footwear"),
        (104, "Watch", "Accessories")
    ]
    cursor.executemany("INSERT OR IGNORE INTO products (id, name, category) VALUES (?, ?, ?)", products)

    behaviors = [
        (1, "browsed", 101),
        (1, "browsed", 102),
        (1, "purchased", 103)
    ]
    cursor.executemany("INSERT INTO behaviors (customer_id, action, product_id) VALUES (?, ?, ?)", behaviors)

    conn.commit()
    conn.close()
