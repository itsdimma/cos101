# Registration and Attendance Checker

registration_status = input("Registration complete? Enter yes or no: ")

attendance = float(input("Enter attendance percentage: "))

if registration_status != "yes" and registration_status != "no":
    print("Invalid registration response.")

elif attendance < 0 or attendance > 100:
    print("Invalid attendance percentage.")

elif registration_status == "yes" and attendance >= 75:
    print("You are eligible for the practical assessment.")

else:
    print("You are not eligible for the practical assessment.")
