coursework = float(input("Enter coursework score (0-30): "))
examination = float(input("Enter examination score (0-70): "))

if coursework < 0 or coursework > 30:
    print("Invalid coursework score.")

elif examination < 0 or examination > 70:
    print("Invalid examination score.")

else:
    total = coursework + examination

    if total >= 70:
        grade = "A"
    elif total >= 60:
        grade = "B"
    elif total >= 50:
        grade = "C"
    elif total >= 45:
        grade = "D"
    elif total >= 40:
        grade = "E"
    else:
        grade = "F"

    if total >= 50:
        decision = "Pass"
    else:
        decision = "Resit required"

    print()
    print("STUDENT RESULT SUMMARY")
    print("======================")
    print("Name:", student_name)
    print(f"Coursework: {coursework:.2f} / 30")
    print(f"Examination: {examination:.2f} / 70")
    print(f"Total: {total:.2f} / 100")
    print("Grade:", grade)
    print("Decision:", decision)
