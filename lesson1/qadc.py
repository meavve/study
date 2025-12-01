a = int(input())
b = int(input())
operation = input()
if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif b == 0:
    print("На ноль делить нельзя!")
elif operation == "/":
    print(a/b)
else:
    print("Неверная операция")

