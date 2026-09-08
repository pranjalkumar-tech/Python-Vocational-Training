products = {
    "Rice": 60,
    "Sugar": 45,
    "Milk": 30,
    "Bread": 40,
    "Oil": 150
}

cart = {}
grand_total = 0

while True:
    print("\n----- Product List -----")

    for item in products:
        print(item, "- ₹", products[item])

    product = input("\nEnter Product Name: ").title()

    if product in products:
        qty = int(input("Enter Quantity: "))

        if qty > 0:
            total = products[product] * qty
            grand_total = grand_total + total

            cart[product] = cart.get(product, 0) + qty  # Adds quantity if product already exists

            print(product, "added to cart.")
        else:
            print("Quantity must be greater than 0.")

    else:
        print("Product not found!")

    choice = input("Do you want to buy more? (yes/no): ").lower()

    if choice == "no":
        break

print("\n========== BILL ==========")

for item in cart:
    price = products[item]
    qty = cart[item]
    total = price * qty

    print(f"{item}\tPrice: ₹{price}\tQty: {qty}\tTotal: ₹{total}")

discount_price = 0

if grand_total >= 5000:
    discount_price = grand_total * (20 / 100)  # Calculates 20% discount

print("-------------------------")
print("Grand Total: ₹", grand_total)
print("Discount (20%): ₹", discount_price)
print("Final Amount: ₹", grand_total - discount_price)
print("Thank You! Visit Again.")