# ==========================================
# PYTHON CAFE
# COMPLETE PROGRAM
# ==========================================

# -----------------------------
# MENU BUILDER
# -----------------------------

menu = [
    "espresso",
    "frappuccino",
    "americano",
    "latte",
    "cold brew",
    "matcha",
    "croissant",
    "cake pop",
    "ham sandwich",
    "bacon sandwich"
]


def display_menu():
    print("========== MENU ==========")

    for item in menu:
        print("-", item)

    print()


daily_special = "matcha"


def show_special():
    print("Today's Special:", daily_special)
    print()


# -----------------------------
# PRICE MANAGER
# -----------------------------

prices = {
    "espresso": 3.25,
    "frappuccino": 6.45,
    "americano": 3.95,
    "latte": 5.25,
    "cold brew": 4.95,
    "matcha": 5.75,
    "croissant": 3.95,
    "cake pop": 3.25,
    "ham sandwich": 7.45,
    "bacon sandwich": 7.95
}


def get_price(item):
    return prices.get(item)


# -----------------------------
# INFO KEEPER
# -----------------------------

menu_info = {
    "espresso": ("Coffee", "4 oz"),
    "frappuccino": ("Coffee", "12 oz"),
    "americano": ("Coffee", "8 oz"),
    "latte": ("Coffee", "12 oz"),
    "cold brew": ("Coffee", "12 oz"),
    "matcha": ("Tea", "12 oz"),
    "croissant": ("Food", "N/A"),
    "cake pop": ("Food", "N/A"),
    "ham sandwich": ("Food", "N/A"),
    "bacon sandwich": ("Food", "N/A")
}


# -----------------------------
# ORDER TAKER
# -----------------------------

def take_order():

    order = []

    display_menu()
    show_special()

    print("Type 'done' when finished.\n")

    while True:

        item = input("Enter an item: ").lower()

        if item == "done":
            break

        if item in menu:

            order.append(item)

            print(item, "added.\n")

        else:

            print("Sorry, that item is not on the menu.\n")

    return order


def calculate_total(order):

    total = 0

    for item in order:

        total += get_price(item)

    return total


def print_receipt(order, total):

    print("\n========== RECEIPT ==========")

    for item in order:

        category, size = menu_info[item]

        print(f"{item:<20} ${get_price(item):.2f}")

    print("-----------------------------")

    print(f"Total:               ${total:.2f}")

    print("=============================")


# -----------------------------
# MAIN PROGRAM
# -----------------------------

customer_order = take_order()

total_cost = calculate_total(customer_order)

print_receipt(customer_order, total_cost)