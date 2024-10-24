# if
num1 = int(input("Input num1: "))
num2 = int(input("Input num2: "))
total = num1 + num2
if total > 5:
    print("ผลรวมมากกว่า 5")
if total < 5:
    print("ผลรวมน้อยกว่า 5")

# if - else
if total == 6:
    print("เป็นเลข 6")
else:
    print("ไม่เป็นเลข 6")

# if - elif - else
if total == 6:
    print("เป็นเลข 6")
elif total != 6:
    print("ไม่เป็นเลข 6")
else:
    print("เป็นเลขอื่นๆ")
