num=int(input("Enter the number:"))
sum=0
order=len(str(num))
copy_num=num

while(num>0):
    digit=num%10
    sum=sum+digit**order
    num=num//10
    
if(sum==copy_num):
    print(copy_num,"is armstrong number")

else:
    print(copy_num,"is not armstrong number")
    
    
'''armstrong number for given range:

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

for num in range(start, end + 1):
    sum = 0
    order = len(str(num))
    copy_num = num

    
    while num > 0:
        digit = num % 10
        sum = sum + digit ** order
        num = num // 10

    if sum == copy_num:
        print(copy_num, "is an Armstrong number")
    else:
        print(copy_num, "is not an Armstrong number")'''
