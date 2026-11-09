answer = "yes"

while answer == "yes":
    number = int(input("Enter a number: "))

    for i in range(1, 13):
        print(number, "x", i, "=", number * i)

    answer = input("Do you want another table? Enter yes or no: ")

print("Program ended.")
