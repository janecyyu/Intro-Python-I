# Program to check if a number is prime or not

# To take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1:
    # loop range from 2 to input number
    # if the input can been divided by previous numbers, not prime
    # else, is prime
    for i in range(2, num):
        if num % i == 0:
            print(f'{num} is not a prime number')
            break
    print(f'{num} is a prime number')

# if input equals or less than 1, not prime:
elif num <= 1:
    print(f'{num} is not a prime number')
