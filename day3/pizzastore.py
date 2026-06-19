print("Welcome to Raghu's Pizza!!!")

while True:
    size=input('What size you want? S for small, M for medium, L for large\n').upper()
    if size in ['S','M','L']:
        break
    print('Invalid size. Please enter again')

while True:
    extra_cheese=input('Do you want extra cheese? y for yes n for No\n').lower()
    if extra_cheese in ['y','n']:
        break
    print('Invalid input, please try again')

while True:
    pepporoni_cheese=input('Do you want pepporoni?y for yes n for No\n').lower()
    if pepporoni_cheese in ['y','n']:
        break
    print('Invalid input, please try again')

bill=0

if size == 'S':
    bill += 12
elif size == 'M':
    bill += 15
else:  # size == 'L'
    bill += 18

if pepporoni_cheese == 'y':
    bill += 3
if extra_cheese == 'y':
    bill += 2


print(f'the final bill is {bill}')

