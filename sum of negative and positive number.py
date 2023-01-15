num = 0
positive = 0
negative = 0

while num != -1:
    num = int(input("Enter positive or negative number (-1 for stop) : "))
    if num >= 0:
        positive = positive + num
    elif num < -1:
        negative = negative + num

print("Sum of positive number = ",positive)
print("Sum of negative number = ",negative)