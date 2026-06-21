import random
games=['rock', 'paper', 'scissor']

human_choice=int(input('What is your choice, 0 for rock, 1 for paper, 2 for scissor\n'))
computer_choice=random.randint(0,2)
print(f'human choice is {human_choice} computer choice is {computer_choice}')
if human_choice==0:
    if computer_choice==0:
        print('Both rocks!! Match draw') #(0,0)
    elif computer_choice==1:
        print('Human:Rock, Computer:Paper !! Computer Win') #(0,1)
    else:
        print('Human:Rock, Computer:Scissor !! Human Win') #(0,2)

elif human_choice==1:
    if computer_choice==0:
        print('Human:Rock, Computer:Paper !! Human Win') #(1,0)
    elif computer_choice==1:
        print('Both paper!! Match draw') # (1,1)
    else:
        print('Human:Paper, Computer: Scissor !! Computer Win') #(1,2)

else:
    if computer_choice==0:
        print('Human:Scissor, Computer:Rock !! Computer Win')
    elif computer_choice==1:
        print('Human:Scissor, Computer:Paper !! Human Win')
    else:
        print('Human:Scissor, Computer:Scissor!! Match draw')