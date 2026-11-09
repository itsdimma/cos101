# Student Score Summary

students = int(input("How many students? "))

if students <= 0:
    print("Error: Number of students must be greater than zero.")

else:
    total_score = 0
    pass_count = 0
    fail_count = 0

    for i in range(1, students + 1):
        score = float(input("Enter score for student " + str(i) + ": "))

        while score < 0 or score > 100:
            print("Invalid score. Enter a value from 0 to 100.")
            score = float(input("Enter score for student " + str(i) + ": "))

        total_score = total_score + score

        if score >= 50:
            pass_count = pass_count + 1
        else:
            fail_count = fail_count + 1

    average_score = total_score / students

    print("\nCLASS RESULT SUMMARY")
    print("====================")
    print("Number of students:", students)
    print("Total score: {:.2f}".format(total_score))
    print("Average score: {:.2f}".format(average_score))
    print("Number of passes:", pass_count)
    print("Number of failures:", fail_count)
