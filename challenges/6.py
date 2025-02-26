#Write a Python program that prompts the user to enter a string and counts the number of vowels (a, e, i, o, u) in thatstring.

name = 'Ochorkodi'

count = 0
for x in name:
    count+=1
print(count)

total = 0
for y in name:
    if y.lower() in 'aeiou':
        total+=1
print(total)