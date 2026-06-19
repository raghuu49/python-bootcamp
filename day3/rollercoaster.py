height=int(input("Enter your height:"))
ticket_price=0

if height>=120:
    age=int(input('Enter your age:'))
    if age<=18:
        ticket_price+=15
    elif age<=21:
        ticket_price+=18
    else:
        ticket_price+=21
    photo_want = input('Do you want a photo? (yes/no): ').lower() == 'yes'
    if photo_want:
        ticket_price+=2
    print(f'ticket price is {ticket_price}')
else:
    print('You need to grow taller')
