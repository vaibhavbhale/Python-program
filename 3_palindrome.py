n = (int(input("Enter the number: ")))
temp = n
rev = 0

while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10  

if n == rev:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")

    
'''num = (input("Enter the number: "))

rev = num[::-1]

if num == rev:
    print("Number is palindrome")
else:
    print("Number is not palindrome")'''
