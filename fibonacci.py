# using recursion to define the Fibonacci sequence
def fib(m):
    if m <= 1:
        return m
    else:
        return fib(m - 1) + fib(m - 2)


# taking input from the user
terms = int(input("How many terms would you like: "))
# check if the input the user gave is valid
if terms <= 0:
    print("Please enter a positive value")
else:
    print("Fibonacci sequence: ")
for n in range(terms):
    print((fib(n)))
