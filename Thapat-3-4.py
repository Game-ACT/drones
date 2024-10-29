import math

while True:
    answer = int(input("Enter number: "))
    if answer < 0:
        break
    else:
        print(math.pow(answer, 2))