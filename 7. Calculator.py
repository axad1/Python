a = float(input("Enter first number: "))
op = input("Enter operator: ")
b = float(input("Enter second number: "))

if op == "+":
    print(a+b)
elif op == "-":
    print(a-b)
elif op == "*":
    print(a*b)
elif op == "/":
    if not b==0:
        print(a/b)
    else:
        print("division by zero")
else:
    print("invalid operator")