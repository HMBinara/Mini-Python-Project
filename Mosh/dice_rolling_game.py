import random
    
while True :
    answer = input("Roll the dice?(y/n) :")
    
    if answer.lower() == "y" :
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f'({die1},{die2})')
    elif answer.lower() == "n" :
        print ("Thank for the Game ")
        break
    else:
        print("Invalid Choice")
        
  