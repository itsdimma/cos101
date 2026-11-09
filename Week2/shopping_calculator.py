# Purchase Summary

item_name = input("Enter the item name: ")
quantity = int(input("Enter the quantity: "))
unit_price = float(input("Enter the unit price: "))

total_cost = quantity * unit_price

print()
print("PURCHASE SUMMARY")
print("================")
print("Item name:", item_name)
print("Quantity:", quantity)
print("Unit price: NGN", unit_price)
print("Total cost: NGN", total_cost)
