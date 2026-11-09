# Daily Sales Summary

days = int(input("How many days? "))

if days <= 0:
    print("Error: Number of days must be greater than zero.")

else:
    total_sales = 0
    high_sales = 0
    low_sales = 0

    for i in range(1, days + 1):
        sales = float(input("Enter sales for day " + str(i) + ": "))

        while sales < 0:
            print("Invalid amount. Sales cannot be negative.")
            sales = float(input("Enter sales for day " + str(i) + ": "))

        total_sales = total_sales + sales

        if sales >= 10000:
            high_sales = high_sales + 1
        else:
            low_sales = low_sales + 1

    average_sales = total_sales / days

    print("\nDAILY SALES SUMMARY")
    print("===================")
    print("Total sales: NGN {:.2f}".format(total_sales))
    print("Average daily sales: NGN {:.2f}".format(average_sales))
    print("Days with sales of at least NGN 10,000:", high_sales)
    print("Days with sales below NGN 10,000:", low_sales)
