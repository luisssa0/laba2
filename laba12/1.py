class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Ресторан: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print("Ресторан открыт!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, rating, flavors):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)



ice_cream_stand = IceCreamStand("Мое кафе-мороженное", "Кафе", 4.2, ["Ваниль", "Шоколад", "Клубника", "Карамель"])


ice_cream_stand.display_flavors()
