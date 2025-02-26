#Write a Python program that prompts the user to enter two numbers and finds the maximum of the two.

num1 = int(input("Enter number:"))
num2 = int(input("Enter another:"))

if num1 > num2:
    print(num1)
else:
    print(num2)
#OR
nums  = [23,45,91,1,12,73,23]
maximum = max(nums)
print(maximum)