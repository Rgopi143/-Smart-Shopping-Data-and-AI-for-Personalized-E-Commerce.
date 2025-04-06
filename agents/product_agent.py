from database.db import get_connection

class ProductAgent:
    def get_products(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, category FROM products")
        rows = cursor.fetchall()

        products = [{"id": row[0], "name": row[1], "category": row[2]} for row in rows]

        conn.close()
        return products
