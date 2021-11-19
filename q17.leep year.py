year=int(input("enter the year : "))
if year%4==0:
    print(year,"leep year")
elif year%100==0:
    print(year,"leep year")
elif year%400==0:
    print(year,"leep year")
else:
    print(year,"not leep year")