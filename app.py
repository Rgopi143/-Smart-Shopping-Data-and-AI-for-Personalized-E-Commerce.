import streamlit as st
from agents.customer_agent import CustomerAgent
from agents.product_agent import ProductAgent
from agents.recommender_agent import RecommenderAgent
from database.db import setup_database
from database.data_loader import insert_sample_data

# Setup DB and load data
setup_database()
insert_sample_data()

# Create agents
customer_agent = CustomerAgent()
product_agent = ProductAgent()
recommender_agent = RecommenderAgent()

# Streamlit UI
st.set_page_config(page_title="Smart Shopping AI", page_icon="🛍️")
st.title("🛍️ Smart Shopping AI Recommender")
st.markdown("Get product recommendations based on browsing and purchase behavior.")

user_id = st.number_input("Enter Customer ID", min_value=1, value=1, step=1)

if st.button("Generate Recommendations"):
    with st.spinner("Analyzing behavior..."):
        behavior = customer_agent.get_behavior(user_id)
        products = product_agent.get_products()
        recommendations = recommender_agent.recommend(user_id, behavior, products)

        if recommendations:
            st.success(f"🎯 Top Recommendations for Customer {user_id}:")
            for p in recommendations:
                st.write(f"• **{p['name']}** ({p['category']})")
        else:
            st.warning("No recommendations found for this user.")
