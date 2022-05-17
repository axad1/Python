# greater number

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a>b and a>c:
    print("a is greater")
elif a>b and not a>c:
    print("c is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")