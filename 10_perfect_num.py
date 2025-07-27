'''A Number that can be represented as the sum of all the factors of the number is known as a Perfect Number.
Number = 28
28 = 1 + 2 + 14 + 4 + 7
as the number 28 has factors 1, 2, 4, 7 and 14.
We sum them up and check whether they match the original number. '''


num =int(input("Enter the number:"))
sum = 0


for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print("The given number is a Perfect number")
else:
    print("The given number is not a Perfect number")