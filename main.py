from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from database.db import setup_database
from database.data_loader import insert_sample_data

def main():
    print("🔄 Starting Smart Shopping AI System...")

    # Setup database and insert initial data
    setup_database()
    insert_sample_data()

    # Initialize agents
    customer_agent = CustomerAgent()
    product_agent = ProductAgent()
    recommender_agent = RecommenderAgent()

    # Simulate for user with ID 1
    user_id = 1
    browsing_data = customer_agent.get_behavior(user_id)
    product_data = product_agent.get_products()

    # Get recommendations
    recommendations = recommender_agent.recommend(user_id, browsing_data, product_data)

    # Display results
    print(f"🎯 Recommendations for User {user_id}:")
    for item in recommendations:
        print(f"- {item['name']} ({item['category']})")

if __name__ == "__main__":
    main()
