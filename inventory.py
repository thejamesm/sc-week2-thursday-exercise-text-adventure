from item import Item

class Inventory:
    def __init__(self) -> None:
        self.__items = []

    def add_item(self, new_item: Item) -> None:
        if isinstance(new_item, Item):
            if new_item not in self.__items:
                self.__items.append(new_item)
            else:
                raise ValueError(f"{new_item.name} already in Inventory")
        else:
            raise TypeError("Inventory can only contain Items")

    def remove_item(self, dropped_item: Item) -> None:
        if isinstance(dropped_item, Item):
            if dropped_item in self.__items:
                self.__items.remove(dropped_item)
            else:
                raise ValueError(f"{dropped_item.name} not in Inventory")
        else:
            raise TypeError("Can only remove Items from Inventory")

    def is_empty(self) -> bool:
        return len(self.__items) == 0

    def list_inventory(self) -> None:
        print()
        print("The contents of your pockets")
        print("----------------------------")
        if not self.is_empty():
            for n, item in enumerate(self.__items, 1):
                print(f"{n}: {item.name}")
        else:
            print("Nothing")

    def choose_item(self) -> Item | None:
        if not self.is_empty():
            while True:
                self.list_inventory()
                print("C: Cancel")
                print()
                user_choice = input("Choose an item > ").upper()
                if user_choice == "C":
                    return None
                try:
                    item_index = int(user_choice) - 1
                    assert item_index >= 0
                    return self.__items[item_index]
                except (IndexError, ValueError, AssertionError):
                    print()
                    print("Invalid choice")
                    continue
        else:
            print("Your pockets are empty")
            return None