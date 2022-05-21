# using pow function
pow(2, 3)

# using ** method
print(2**3)

# using for loop
def power(base, power):
    ans = 1
    for i in range(power):
        ans *= base
    print(ans)
# calling power
power(2,4)