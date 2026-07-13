# ==========================================
# ORDER TAKER
# ==========================================

# Import every price.
from price_manager import get_price, show_prices

# Pseudocode
# 1. Show the menu.
# 2. Ask the customer for items.
# 3. Save items in a list.
# 4. Stop when customer types "done".
# 5. Calculate the total.
# 6. Print the receipt.

def take_order():

    order = []

    show_prices()

    print("\nType 'done' when finished.\n")

    while True:

        item = input("Enter an item: ").lower()

        if item == "done":
            break

        if get_price(item) is not None:
            order.append(item)
            print(item + " added.\n")

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
        print(f"{item:<20} ${get_price(item):.2f}")

    print("-----------------------------")
    print(f"Total:               ${total:.2f}")
    print("=============================")


customer_order = take_order()
total_cost = calculate_total(customer_order)
print_receipt(customer_order, total_cost)