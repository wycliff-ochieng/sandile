#Write a Python program that prompts the user to enter a number and prints its multiplication table up to a specified range.

num = int(input("Enter a number:"))

for i in range(10):
    print(num,"X",i ,"=",num*i)

