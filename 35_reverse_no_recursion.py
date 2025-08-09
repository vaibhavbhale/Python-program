def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        last_digit = num % 10 #extract the last  digit
        rev = rev * 10 + last_digit # build the rev no. by appending it in rev
        remaining_num = num // 10 # return the last digit
        return reverse_number(remaining_num, rev)
    
num = int(input("Enter a number: "))
reversed_num = reverse_number(num)
print("Reversed number is:", reversed_num)