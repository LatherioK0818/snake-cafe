class SnakesCafe:
    def __init__(self):
        self.menu = {
            "Appetizers": ["Wings", "Cookies", "Spring Rolls"],
            "Entrees": ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"],
            "Desserts": ["Ice Cream", "Cake", "Pie"],
            "Drinks": ["Coffee", "Tea", "Unicorn Tears"]
        }
        self.order = {}

    def print_welcome_message(self):
        welcome_message = (
            "**************************************\n"
            "**    Welcome to the Snakes Cafe!   **\n"
            "**    Please see our menu below.    **\n"
            "**                                  **\n"
            "** To quit at any time, type 'quit' **\n"
            "**************************************"
        )
        print(welcome_message)

    def print_menu(self):
        for category, items in self.menu.items():
            print(f"\n{category}\n" + "-" * len(category))
            for item in items:
                print(item)
        print("\n***********************************")
        print("** What would you like to order? **")
        print("***********************************")

    def add_to_order(self, item):
        item = item.capitalize()
        if item in sum(self.menu.values(), []):  # Flatten the menu list
            self.order[item] = self.order.get(item, 0) + 1
            print(f"** {self.order[item]} order(s) of {item} has been added to your meal **")
        else:
            print("** This item is not on the menu. Please try again **")
        return True

    def start_ordering(self):
        self.print_welcome_message()
        self.print_menu()
        while True:
            user_input = input("> ").strip()
            if user_input.lower() == 'quit':
                print("Exiting")
                break
            self.add_to_order(user_input)

if __name__ == "__main__":
    restaurant = SnakesCafe()
    restaurant.start_ordering()
