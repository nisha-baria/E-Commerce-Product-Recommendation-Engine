# 🛒 E-Commerce Product Recommendation Engine

An industry-grade, highly optimized Intelligent Product Recommendation Dashboard built using **Python**, **Streamlit**, and core **Data Structures & Algorithms (DSA)**. 

This project simulates how top-tier e-commerce platforms like Amazon, Flipkart, and Myntra rank and suggest products dynamically to maximize CTR (Click-Through Rate) and user engagement.

## 🛠️ DSA Concepts & Architecture Internals

To bypass slow $O(P \log P)$ full-catalog sorting, this engine models a production-level split architecture:

*   **Optimized HashMaps (`dict`):** Achieves $O(1)$ time complexity for pulling live product catalogs and tracing complex user interaction footprints (Cart items, Search tokens).
*   **Priority Queues / Min-Heaps (`heapq`):** Bounds memory to maintain only the Top-$N$ high-scoring items. Reduces overall ranking latency to an efficient **$O(P \log N)$** operations.
*   **Mathematical Vector Logic (Set Intersections):** Utilizes dynamic text mining with Jaccard Similarity coefficients to calculate real-time intent maps between user searches and product tags.

### 🔄 Recommendation Pipeline Workflow
$$\text{User Interaction Fingerprint} \longrightarrow \text{Jaccard Token Similarity} \longrightarrow \text{Category Boost Vector} \longrightarrow \text{Heap Rank Filtering} \longrightarrow \text{Top-N Served UI Cards}$$

## 📁 Repository Folder Structure

```text
E-Commerce-Product-Recommendation-Engine/
│
├── data/
│   ├── products.json          # Complete Inventory Datastore Map
│   └── users.json             # Implicit User Sessions & Conversion Records
│
├── src/
│   ├── __init__.py            # Packaging Module Root
│   ├── models.py              # DSA Class Objects (Product & User Blueprints)
│   ├── utils.py               # Vector Scoring & File Ingestion Pipelines
│   └── recommender.py         # Custom Heap-based Core Ranking Engine
│
├── requirements.txt           # Package Metadata Signatures
├── .gitignore                 # Production Tracking Filter rules
└── main.py                    # Streamlit High-Fidelity UI Interface Front

## 🚀 Installation & Local Deployment Guide
Follow these simple steps to spin up the high-fidelity web dashboard on your machine:

1. Clone the Repository
git clone [https://github.com/YOUR_USERNAME/E-Commerce-Product-Recommendation-Engine.git](https://github.com/YOUR_USERNAME/E-Commerce-Product-Recommendation-Engine.git)
cd E-Commerce-Product-Recommendation-Engine

2. Install Project Dependencies
pip install -r requirements.txt

3. Run the Streamlit Web Application
streamlit run main.py

## 📊 Sample Visual Metrics Output

| Strategy Applied | Targeted User | Triggered DSA Logic Pipeline | Served Recommendations |
| :--- | :--- | :--- | :--- |
| **Personalized Intent Scoring** | `U001` (Searched Audio) | Jaccard Similarity Match + Heap Filters | Sony WH-1000XM4, Boat Earphones |
| **Cold-Start Rule Fallback** | `New User` (No History) | Global Rating Sorting via Heap Arrays | iPhone 15 Pro Max (Trending #1) |

## 💡 Learning Outcomes
Mastered splitting monolithic codebases into standard professional Modular Architectures.

Implemented memory-bounded constraints to optimize CPU cycles using Heaps vs Sort algorithms.

Gained experience in converting abstract algorithms into beautiful, interactive Web Dashboard Frontends.
