from models.review import Review


class ReviewController:
    reviews: list[Review] = [Review(100, "Wonderful jumpsuit!", "Absolutely perfect for summer. I love the color and "
                                                                "pattern - the adjustable straps are great!", 10),
                             Review(101, "My new fav pair of jeans!", "I really love these jeans - they feel really "
                                                                      "soft and comfortable but also pretty "
                                                                      "sturdy.", 8),
                             Review(102, "Bad quality!!!!", "REALLY DISAPPOINTED - CAN'T GET MY FOOT PAST THE "
                                                            "ANKLE. I don't have a high instep and have narrow "
                                                            "feet, but it was impossible to get them on properly", 5),
                             Review(103, "Absolutely love this blazer!", "Very good quality and lovely fit!", 6),
                             Review(104, "Very trendy satin skirt", "Very stretchy, nice quality and color!", 9)]

    def __init__(self):
        pass

    def view_reviews(self, product_id):
        product_reviews = [review for review in self.reviews if review.product_id == product_id]
        return product_reviews

    def add_review(self, product_id, review_summary, review_text):
        review_id_list = [review.review_id for review in self.reviews]
        review_id = max(review_id_list, default=0) + 1
        self.reviews.append(Review(review_id, review_summary, review_text, product_id))