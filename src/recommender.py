import heapq
from src.utils import calculate_jaccard_similarity

class RecommendationEngine:
    def __init__(self, product_catalog, user_profiles):
        self.product_catalog = product_catalog
        self.user_profiles = user_profiles

    def get_recommendations(self, user_id, n=3):
        # Cold Start Rule Base Strategy
        if user_id not in self.user_profiles or user_id == "New User (Cold Start)":
            top_items = heapq.nlargest(n, self.product_catalog.values(), key=lambda x: x.rating)
            return [(item, item.rating, "⭐ Trending") for item in top_items], "Global Hits (Cold Start Mode)"

        user = self.user_profiles[user_id]
        user_keywords = set(user.search_history)
        heap = []

        for p_id, product in self.product_catalog.items():
            if p_id in user.purchased_items: 
                continue  # Exclude already purchased items

            similarity = calculate_jaccard_similarity(user_keywords, product.tags)
            
            # Category Boost Score Vector matching
            category_boost = 3.0 if any(self.product_catalog[cid].category == product.category for cid in user.cart_items if cid in self.product_catalog) else 0.0
            
            final_score = (similarity * 5.0) + category_boost + product.rating
            
            heapq.heappush(heap, (final_score, product))
            if len(heap) > n: 
                heapq.heappop(heap)

        recs = []
        while heap:
            score, prod = heapq.heappop(heap)
            recs.append((prod, round(score, 2), "🔥 Match"))
            
        return recs[::-1], "Personalized Intent Scoring"