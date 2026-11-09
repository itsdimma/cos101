number = int(input("Enter a positive number: "))

if number < 1:
    print("Error: Enter a positive number.")
else:
    while number >= 1:
        print(number)
        number = number - 1

    print("Countdown completed.")
