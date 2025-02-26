#Write a Python program that prints the Fibonacci series up to a specified number of terms.
num_terms = int(input("Enter numer of terms:"))

first_term = 0
second_term = 1

print("Finobacci series")
for i in range(num_terms):
    print(first_term,end='')
    next_term = first_term + second_term
    first_term = second_term
    second_term = next_term