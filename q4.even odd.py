num=int(input("enter the number : "))
if num<50:
    if num%2==0:
        print(num,"even number")
    else:
        print(num,"odd number ")
elif num>50:
    if num%2==0:
        print(num,"even number ")
    else:
        print(num,"odd number")
else:
    print(num,"equal")