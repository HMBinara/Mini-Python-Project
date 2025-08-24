name = input("Type Your Name : ")
print(f"Welcome {name} to this adventure!")

answer= input("You are on a dirt road,it has come to an end you can go left or right.Which way would you like to go?").lower()

if answer == "left":
    answer = input("You come to a river , you can walk around it or swim accross? Type walk around and swim to swim accross: ")
    
    if answer == "swim":
        print("You swam accross and were eaten by an alligator.")
    elif answer == "walk":
        print("You walk for many miles , ran out of water and you lost the game")
    else:
        print('Not a valid option . You Lose')    
 
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly , do you want to cross it or head back (cross/back)? ")
    
    if answer == "back":
        print("You go back and lose .")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger.Do you talk to them(Yes/No)?")
        
        if answer == "yes":
            print("You talk to the Stanger and they give you gold. You WIN!!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print('Not a valid option . You Lose')
    else:
        print('Not a valid option . You Lose') 
    
else:
    print('Not a valid option . You Lose')  
    
    
print(f"Thank you for Trying {name}")  

