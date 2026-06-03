class Product:
    def __init__(self, product_id, title, category, tags, rating, price, icon, bg):
        self.product_id = product_id
        self.title = title
        self.category = category
        self.tags = set(tags)  # Used Set for O(1) tracking
        self.rating = rating
        self.price = price
        self.icon = icon
        self.bg = bg

    def __lt__(self, other):
        return self.rating < other.rating


class User:
    def __init__(self, user_id, search_history, cart_items, purchased_items):
        self.user_id = user_id
        self.search_history = search_history
        self.cart_items = set(cart_items)
        self.purchased_items = set(purchased_items)