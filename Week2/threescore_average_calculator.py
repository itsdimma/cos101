# Calculate Total and Average Scores

score1 = float(input("Enter the first score: "))
score2 = float(input("Enter the second score: "))
score3 = float(input("Enter the third score: "))

total = score1 + score2 + score3

average = total / 3

print("Total score:", format(total, ".2f"))
print("Average score:", format(average, ".2f"))
