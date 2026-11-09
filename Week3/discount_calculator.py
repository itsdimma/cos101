# Discount Calculator

amount = float(input("Enter the purchase amount: "))

if amount < 0:
    print("Invalid amount. Amount cannot be negative.")

else:
    if amount >= 50000:
        discount_rate = 10
    elif amount >= 10000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount = (amount * discount_rate) / 100

    final_amount = amount - discount

    print()
    print("PURCHASE SUMMARY")
    print("================")
    print(f"Original amount: NGN {amount:.2f}")
    print(f"Discount amount: NGN {discount:.2f}")
    print(f"Final amount payable: NGN {final_amount:.2f}")
