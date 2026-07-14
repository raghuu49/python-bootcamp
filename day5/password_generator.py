import random

upper_case=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_case=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols=['!','@','#','$','%','^','&','*','(',')','_','+','=','-','[',']','{','}','|',':',';','"',"'",'<','>','.','?','/']
numbers=['0','1','2','3','4','5','6','7','8','9']

root_list=[upper_case,lower_case,symbols,numbers]

# Password generator 
# Minimum length-8 maximum length-20
# -First letter should be a alphabet
# -Atleast one symbol
# -Atleast one number
# -Upper case and lower case both

#take user input and validate
while(True):
    password_length=int(input('Enter the password length\n'))
    if 8<=password_length<=20:
        break
    print('Length should be between 8 and 20 try again')

#enforce first letter to be alphabet, strings are immutable in python so we will take a list, in root list alphabets are between 0 and 1 and to enforce upper and lower both we can take first as lower, second as upper then completely randomise

password_list=[]
password_list.append(lower_case[random.randint(0,25)]) # lower case added
password_list.append(upper_case[random.randint(0,25)]) # upper case added

# now we have password_length-2 spots left symbols must be between [1,password_length-2-1(for number)]
while True:
    symbol_length=int(input('How many symbols you want\n'))
    if 1<=symbol_length<=password_length-3:
        break
    print('Invalid choice! please enter valid number')

# now lets choose number of symbols
for i in range(1,symbol_length+1):
    password_list.append(random.choice(symbols))

# now to append numbers we have password_length-2-symbol spot left so choice is [1,passwordlength-2-symbol_length]

while True:
    number_length=int(input('How many numbers you want\n'))
    if 1<=number_length<=password_length-2-symbol_length:
        break
    print('Invalid choice, please enter a number valid')

for i in range(1,number_length+1):
    password_list.append(random.choice(numbers))

# now possible chance password length is not fulfiled
remaining_chars=password_length-2-symbol_length-number_length
if(remaining_chars>0):
    for i in range (0,remaining_chars):
         first_index=random.randint(0,1)
         second_index=random.randint(0,25)
         password_list.append(root_list[first_index][second_index])

first_char=password_list[0]
remaining=password_list[1:]
random.shuffle(remaining)
password=first_char+"".join(remaining)
print(password)

 