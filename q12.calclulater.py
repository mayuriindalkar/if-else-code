num1=int(input("enter the 1st number : "))
num2=int(input("enter the 2nd number : "))
num3=input("enter the operater : ")
if num3=="+":
    print(num1+num2,"add")
elif num3=="-":
    print(num1-num2,"sub")
elif num3=="*":
    print(num1*num2,"multiply")
elif num3=="**":
    print(num1**num2,"exponand")
elif num3=="/":
    print(num1/num2,"division")
elif num3=="//":
    print(num1//num2,"floor division")
elif num3=="%":
    print(num1%num2,"modulas")
