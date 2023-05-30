import tkinter as tk

class IceCreamStand:
    def __init__(self, flavors):
        self.flavors = flavors

    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def remove_flavor(self, flavor):
        if flavor in self.flavors:
            self.flavors.remove(flavor)


ice_cream_stand = IceCreamStand(["Ваниль", "Шоколад", "Клубника", "Карамель"])


root = tk.Tk()
root.title("Кафе мороженого")


def show_flavors():
    flavor_list.delete(0, tk.END)
    for flavor in ice_cream_stand.flavors:
        flavor_list.insert(tk.END, flavor)


def add_flavor():
    flavor = flavor_entry.get()
    ice_cream_stand.add_flavor(flavor)
    flavor_list.insert(tk.END, flavor)
    flavor_entry.delete(0, tk.END)


def remove_flavor():
    selected_flavors = flavor_list.curselection()
    for index in reversed(selected_flavors):
        flavor_list.delete(index)
        flavor = ice_cream_stand.flavors[index]
        ice_cream_stand.remove_flavor(flavor)


flavor_label = tk.Label(root, text="Сорта мороженого")
flavor_label.pack()

flavor_list = tk.Listbox(root)
flavor_list.pack()

flavor_entry = tk.Entry(root)
flavor_entry.pack()

show_button = tk.Button(root, text="Показать сорта", command=show_flavors)
show_button.pack()

add_button = tk.Button(root, text="Добавить сорт", command=add_flavor)
add_button.pack()

remove_button = tk.Button(root, text="Удалить сорт", command=remove_flavor)
remove_button.pack()

root.mainloop()
