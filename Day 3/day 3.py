year = int(input("Input you year"))

if year % 4 == 0:



    if year % 100 == 0 and year % 400 ==0:
        print("The year is leep year")

    elif year % 100 == 0:
        print("The year is not a leep Year")

    else:
        print("The year is a leep year")

else:
    print("The year is not a leep Year")