name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input("You are on a dirt road, it has come to an end. YOu can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a River, you can walk around it or swin accross it. Choice is yours. Type 'walk' to walk around and 'swim' to swim accross: ")

    if answer == "swim":
        print("You swam accros and were eaten by an Alligator. You loose.")
    elif answer == "walk":
        print("You walked for many miles and ran out of water. You loose.")
    else:
        print("not a valid option. You loose.")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. Do you want to cross it or would you go back?")

    if answer == "back":
        print("You go back. You Loose.")
    elif answer == "cross":
        answer = input("You crossed teh bridge and you meet a stranger. Yes or No?")
        if answer == "yes":
            print("You talked to a stranger and they give you gold. YOU WIN!!!")
        elif answer == "no":
            print("You ignored the stranger and they are offended, You Loose.")
        else:
            print("Not a valid option. You loose.")
    else:
        print("not a valid option. You loose.")
else:
    print("Not a valid option. You loose.")

print("Thank you for trying the game.")