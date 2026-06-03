import json
from src.models import Product, User

def calculate_jaccard_similarity(set1, set2):
    if not set1 or not set2: 
        return 0.0
    return len(set1.intersection(set2)) / len(set1.union(set2))

def load_catalog_and_users(products_path, users_path):
    product_catalog = {}
    user_profiles = {}

    with open(products_path, 'r') as pf:
        products_data = json.load(pf)
        for p in products_data:
            product_catalog[p["id"]] = Product(p["id"], p["title"], p["category"], p["tags"], p["rating"], p["price"], p["icon"], p["bg"])

    with open(users_path, 'r') as uf:
        users_data = json.load(uf)
        for u in users_data:
            user_profiles[u["id"]] = User(u["id"], u["search_history"], u["cart_items"], u["purchased_items"])

    return product_catalog, user_profiles