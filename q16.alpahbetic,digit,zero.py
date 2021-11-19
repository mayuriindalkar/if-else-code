# num=input("enter the number or letter : ")
# if num>="a" and num<="z":
#     print(num,"alpahbetic")
# elif num > "0" and num <= "9":
#     print(num,"digit")
# else:
#     print(num,"zero")

# a = [10, 20]
# b = a
# b += [30, 40]
# print(a)
# print(b)


num=int(input("enter the number : "))
i=1
while i<=num:
    j=1
    while j<=i:
        print("*",end=" ")
        j=j+1
    print()
    i=i+1