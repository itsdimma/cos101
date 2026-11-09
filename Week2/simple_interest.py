# Calculate simple interest

print("SIMPLE INTEREST CALCULATOR")
print("==========================")

principal = float(input("Enter the principal in naira: "))
rate = float(input("Enter the annual rate (%): "))
time = float(input("Enter the time in years: "))

interest = (principal * rate * time) / 100

final_amount = principal + interest

print()
print("Principal:", principal)
print("Annual rate:", rate, "%")
print("Time:", time, "years")
print("Simple interest:", interest, "naira")
print("Final amount:", final_amount, "naira")
