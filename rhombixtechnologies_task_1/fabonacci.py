# Fibonacci Generator Program

def fibonacci_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Taking input from user
num = int(input("Enter how many Fibonacci numbers you want: "))

print("Fibonacci Sequence:")
for value in fibonacci_generator(num):
    print(value, end=" ")
    
