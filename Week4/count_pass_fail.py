# Count Passes and Failures

students = int(input("Enter the number of students: "))

if students <= 0:
    print("Invalid number of students.")

else:
    passes = 0
    failures = 0

    for number in range(1, students + 1):
        score = float(input("Enter student score: "))

        if score >= 50:
            passes += 1
        else:
            failures += 1

    print()
    print("Number of students:", students)
    print("Number of passes:", passes)
    print("Number of failures:", failures)
