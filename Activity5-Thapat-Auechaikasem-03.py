num1 = int(input("Input num1: "))
num2 = int(input("Input num2: "))
total = num1 + num2

# if
if total % 2 == 0:
    print("Total is even")
# if - else
if total % 2 == 0:
    print("Total is even")
else:
    print("Total is odd")
# if - elif - else
if total % 2 == 0:
    print("Total is even")
elif total % 2 != 0:
    print("Total is odd")
else:
    print("Total is neither even nor odd")
