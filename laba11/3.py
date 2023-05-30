class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print("Ресторан открыт!")



restaurant = Restaurant("Мой ресторан", "Итальянская", 4.5)


restaurant.describe_restaurant()


new_rating = float(input("Введите новый рейтинг ресторана: "))
restaurant.update_rating(new_rating)


restaurant.describe_restaurant()
