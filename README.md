# -Smart-Shopping-Data-and-AI-for-Personalized-E-Commerce.
Hack the Future: A Gen AI Sprint Powered by Data
# Smart Shopping: Data and AI for Personalized E-Commerce

## 🚀 Overview
This project is a multi-agent AI system designed to deliver **hyper-personalized product recommendations** for an e-commerce platform. It uses autonomous agents and an SQLite database to dynamically tailor product suggestions based on customer behavior and preferences.

## 🧠 Architecture

### Agents
- **Customer Agent**: Captures user activity (browsing, purchases, demographics).
- **Product Agent**: Manages product information and updates metadata.
- **Recommender Agent**: Analyzes behavior and product data to generate real-time recommendations.

### 🗃️ Database
- **SQLite** is used as long-term memory for storing:
  - Customer profiles
  - Browsing and purchase history
  - Product metadata

## 🛠️ Tech Stack
- Python
- SQLite
- Pandas
- Scikit-learn (optional for ML-based recommendations)

## 🔁 Workflow

```text
[Customer Agent] → Sends behavior info → [Recommender Agent]
[Product Agent] → Sends product info → [Recommender Agent]
[Recommender Agent] → Returns personalized products
