num=input("enter the number or digit : ")
if num>="A" and num<="Z":
        print(num,"alphabetic upper case letter")
elif num>="a" and num<="z":
        print(num,"alphabetic lower case letter")
elif num>="0" and num<="9":
    print(num,"digit")
else:
    print(num,"special charctor")