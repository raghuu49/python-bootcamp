print('Welcome to Treasure Island!!')

while True:
    which_way=input('Which way you want to go? Left or right\n').lower()
    if which_way!="left":
        print("You Lose")
        break
    next_action=input("What do you want?Swim or wait\n").lower()
    if next_action!="wait":
        print("Attacked by trout game over")
        break
    which_door=input("Which door you want?Red, Blue or Yellow\n").lower()
    if which_door=="red":
        print("Burned by fire, game over")
        break
    if which_door=="blue":
        print("Eaten by beasts, game over")
        break
    if which_door!="yellow":
        break
    print("You win")
    break
