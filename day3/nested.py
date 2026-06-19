age=int(input('Enter your age:'))

#age validation
if age<0 or age>150:
    print('Enter valid age')
else:
    if age>=0 and age<=60:
        if age>=0 and age<=12:
            print('You are a child')
        elif age>=13 and age<=19:
            print("You are teenager")
        elif age>=20 and age<=60:
            print('You are adult')
    else:
        print('You are old son')