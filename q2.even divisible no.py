num=int(input("enter the number : "))
if num%2==0:
    if num%5==0:
        print(num,"even number and divisible by 5")
    else:
        print(num,"even number but not divisible by 5")
else:
    if num%5==0:
        print(num,"odd number or divisible by 5")
    else:
        print(num,"odd number or not divisible by 5")