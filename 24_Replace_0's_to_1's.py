'''process: find the digits of the integer. Compare each digit with 0 if the digit is equal to 0 then replace it with 1. 
Construct the new integer with the replaced digits.'''

num = int(input("Enter an integer: "))
new_num = int(str(num).replace('0', '1'))
print("Updated integer:", new_num)
