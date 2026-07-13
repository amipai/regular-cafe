# ==========================================
# PYTHON CAFE - MENU BUILDER
# ==========================================

# Menu stored in a list

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


# Display the menu
def display_menu():
    print("========== MENU ==========")

    for item in menu:
        print("-", item)

    print()


# Add an item to the menu
def add_item(item):
    menu.append(item)


# Remove an item from the menu
def remove_item(item):
    if item in menu:
        menu.remove(item)


# Daily Special
daily_special = "matcha"


def show_special():
    print("Today's Special:", daily_special)