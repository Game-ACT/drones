score = []
n = int(input("Input number of students: "))
for i in range(n):
    score.append(float(input("Input score student " + str(i + 1) + " : ")))
print("\n")

average = sum(score) / len(score)

print("Average score is " + str(average))
