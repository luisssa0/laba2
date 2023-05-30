class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print("Ресторан открыт!")


newRestaurant = Restaurant("Мой ресторан", "Итальянская")
print("Название ресторана:", newRestaurant.restaurant_name)
print("Тип кухни:", newRestaurant.cuisine_type, "\n")

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()