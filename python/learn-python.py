from ast import If


name = input("Name: ")
print(f"Hello, {name} nice to meet you!")

n = int(input("Number: "))

if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

