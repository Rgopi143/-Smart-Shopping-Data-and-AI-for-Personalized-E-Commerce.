from database.db import get_connection

class CustomerAgent:
    def get_behavior(self, customer_id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT action, product_id FROM behaviors WHERE customer_id = ?", (customer_id,))
        rows = cursor.fetchall()

        behavior = {"browsed": [], "purchased": []}
        for action, product_id in rows:
            behavior[action].append(product_id)

        conn.close()
        return behavior
