import streamlit as st
from src.utils import load_catalog_and_users
from src.recommender import RecommendationEngine

# Page Config
st.set_page_config(page_title="Intelligent RecSys Dashboard", page_icon="🛍️", layout="wide")

# Inject Custom Beautiful CSS styling
st.markdown("""
<style>
    .stApp { background-color: #F8F9FA; }
    .product-card {
        background: white; border-radius: 16px; padding: 20px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); border: 1px solid #E9ECEF;
        transition: transform 0.3s ease, box-shadow 0.3s ease; margin-bottom: 20px;
    }
    .product-card:hover { transform: translateY(-5px); box-shadow: 0 12px 30px rgba(0, 0, 0, 0.1); }
    .img-placeholder {
        width: 100%; height: 140px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center; font-size: 40px; margin-bottom: 15px;
    }
    .badge-cat { background-color: #E3F2FD; color: #0D47A1; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 20px; }
    .badge-tag { background-color: #FFF3E0; color: #E65100; font-size: 11px; font-weight: bold; padding: 4px 10px; border-radius: 20px; float: right; }
    .price-tag { font-size: 22px; font-weight: 800; color: #2B2D42; margin: 10px 0 2px 0; }
    .score-tag { font-size: 12px; color: #6C757D; font-weight: 500; }
    .buy-btn { width: 100%; background: linear-gradient(135deg, #1E88E5, #1565C0); color: white; border: none; padding: 8px; border-radius: 8px; font-weight: bold; font-size: 13px; cursor: pointer; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# Initialize Engine with Data Files
@st.cache_resource
def init_system():
    catalog, users = load_catalog_and_users("data/products.json", "data/users.json")
    return RecommendationEngine(catalog, users)

engine = init_system()

# UI Layout Design
st.markdown("<h1 style='text-align: center; color: #1E88E5; font-weight: 800; margin-bottom: 0;'>🛍️ Personalization Feature Store & RecSys Engine</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #6C757D; font-size: 16px;'>Production-ready modular codebase utilizing dynamic Heaps</p>", unsafe_allow_html=True)
st.write("---")

# Sidebar Configuration Controls
st.sidebar.markdown("### 🛠️ Configuration Controls")
user_options = list(engine.user_profiles.keys()) + ["New User (Cold Start)"]
selected_user = st.sidebar.selectbox("👤 Simulation Profile:", user_options)
recommendation_count = st.sidebar.slider("🎯 Recommendation Target (N):", 1, 5, 3)

st.sidebar.write("---")
st.sidebar.markdown("### 📊 Live Client Footprints")
if selected_user in engine.user_profiles:
    u = engine.user_profiles[selected_user]
    st.sidebar.markdown(f"**Keywords Searched:**\n`{list(u.search_history)}`")
    st.sidebar.markdown(f"**Items Active in Basket:**\n`{list(u.cart_items)}`")
    st.sidebar.markdown(f"**Past Conversions:**\n`{list(u.purchased_items) if u.purchased_items else 'None'}`")
else:
    st.sidebar.info("Anonymous session mapped. Firing popularity rules.")

# Execute Logic
recs, strategy = engine.get_recommendations(selected_user, n=recommendation_count)

st.markdown(f"### 🎯 Strategy Engine Output: <span style='color:#1565C0;'>{strategy}</span>", unsafe_allow_html=True)

# Display Grid Layout
cols = st.columns(recommendation_count)
for index, col in enumerate(cols):
    if index < len(recs):
        prod, score, status = recs[index]
        with col:
            st.markdown(f"""
            <div class="product-card">
                <div class="img-placeholder" style="background: {prod.bg};">{prod.icon}</div>
                <div>
                    <span class="badge-cat">{prod.category}</span>
                    <span class="badge-tag">{status}</span>
                </div>
                <h3 style="margin: 12px 0 4px 0; font-size: 18px; font-weight: 700; color:#212529;">{prod.title}</h3>
                <p style="margin: 0; font-size: 12px; color: #ADB5BD;">ID: {prod.product_id}</p>
                <div class="price-tag">₹{prod.price:,}</div>
                <div class="score-tag">⚡ Pipeline Score Priority: <b>{score}</b></div>
                <button class="buy-btn">⚡ Express Checkout</button>
            </div>
            """, unsafe_allow_html=True)

# Dataframe Section
st.write("---")
st.markdown("### 📦 System Inventory Memory Dump (`Hash Store Map`)")
catalog_df = [{
    "ID": p.product_id, "Product Label": p.title, "Market Category": p.category, 
    "Unit Valuation": f"₹{p.price:,}", "Internal Rating Store": p.rating, "Metadata Vectors": ", ".join(p.tags)
} for p in engine.product_catalog.values()]
st.dataframe(catalog_df, use_container_width=True)