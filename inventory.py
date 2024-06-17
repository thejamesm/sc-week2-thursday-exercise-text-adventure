from item import Item

class Inventory:
    def __init__(self):
        self.__items = []

    def add_item(self, new_item):
        if isinstance(new_item, Item):
            if new_item not in self.__items:
                self.__items.append(new_item)
            else:
                raise ValueError(f"{new_item.name} already in Inventory")
        else:
            raise TypeError("Inventory can only contain Items")

    def remove_item(self, dropped_item):
        if isinstance(dropped_item, Item):
            if dropped_item in self.__items:
                self.__items.remove(dropped_item)
            else:
                raise ValueError(f"{dropped_item.name} not in Inventory")
        else:
            raise TypeError("Can only remove Items from Inventory")

    def is_empty(self):
        return len(self.__items) == 0

    def list_inventory(self):
        print()
        print("The contents of your pockets")
        print("----------------------------")
        if not self.is_empty():
            for n, item in enumerate(self.__items):
                print(f"{n}: {item.name}")
        else:
            print("Nothing")

    def choose_item(self):
        if not self.is_empty():
            while True:
                print("C: Cancel")
                print()
                print("Choose an item")
                user_choice = input("> ").upper()
                if user_choice == "C":
                    return False
                try:
                    return self.__items[int(user_choice)]
                except (IndexError, ValueError):
                    print()
                    print("Invalid choice")
                    print()
                    continue
        else:
            print("Your pockets are empty")
            return False