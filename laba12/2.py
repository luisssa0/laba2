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
    def __init__(self, restaurant_name, cuisine_type, rating, flavors, location, working_hours):
        super().__init__(restaurant_name, cuisine_type, rating)
        self.flavors = flavors
        self.location = location
        self.working_hours = working_hours

    def display_flavors(self):
        print("Список сортов мороженого:")
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)
        print(f"Сорт мороженого '{flavor}' добавлен.")

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)
            print(f"Сорт мороженого '{flavor}' удален.")
        else:
            print(f"Сорт мороженого '{flavor}' не найден.")

    def check_flavor(self, flavor):
        if flavor in self.flavors:
            print(f"Сорт мороженого '{flavor}' доступен.")
        else:
            print(f"Сорт мороженого '{flavor}' недоступен.")


class PopsicleIceCream(IceCreamStand):
    def __init__(self, restaurant_name, rating, flavors, location, working_hours):
        super().__init__(restaurant_name, "Мороженое на палочке", rating, flavors, location, working_hours)

    def eat_popsicle(self):
        print("Вы съели мороженое на палочке.")


class SoftIceCream(IceCreamStand):
    def __init__(self, restaurant_name, rating, flavors, location, working_hours):
        super().__init__(restaurant_name, "Мягкое мороженое", rating, flavors, location, working_hours)

    def eat_soft_ice_cream(self):
        print("Вы съели мягкое мороженое.")



ice_cream_stand = IceCreamStand("Мое кафе-мороженое", "Кафе", 4.2, ["Ваниль", "Шоколад", "Клубника", "Карамель"],
                                "Центральная площадь", "10:00 - 20:00")


ice_cream_stand.display_flavors()


ice_cream_stand.add_flavor("Банан")
ice_cream_stand.display_flavors()


ice_cream_stand.remove_flavor("Клубника")
ice_cream_stand.display_flavors()


ice_cream_stand.check_flavor("Ваниль")
ice_cream_stand.check_flavor("Манго")


popsicle_stand = PopsicleIceCream("Мое кафе-мороженое на палочке", 4.5, ["Клубника", "Вишня"], "Парк", "12:00 - 18:00")
popsicle_stand.display_flavors()
popsicle_stand.eat_popsicle()


soft_stand = SoftIceCream("Мое мягкое мороженое", 4.8, ["Шоколад", "Ваниль", "Карамель"], "Пляж", "11:00 - 21:00")
soft_stand.display_flavors()
soft_stand.eat_soft_ice_cream()
