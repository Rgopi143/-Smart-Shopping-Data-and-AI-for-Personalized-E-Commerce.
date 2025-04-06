class RecommenderAgent:
    def recommend(self, customer_id, behavior, products):
        browsed_ids = set(behavior.get("browsed", []))
        purchased_ids = set(behavior.get("purchased", []))

        recommended = []
        for product in products:
            if product["id"] not in browsed_ids and product["id"] not in purchased_ids:
                recommended.append(product)

        return recommended[:3]  # return top 3
