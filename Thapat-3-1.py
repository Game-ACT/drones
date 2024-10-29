score = []
for i in range(10):
    score.append(float(input("Input score student " + str(i + 1) + " : ")))
print("\n")
for i in score:
    print("Student " + str(score.index(i) + 1) + " score is " + str(i))
