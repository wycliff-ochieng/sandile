#Write a Python program that prompts the user to enter a number and checks if it's a prime number.

num = int(input("Enter a number:"))

if num % 1 == 0 and num % num == 0:
    print("prime number")
