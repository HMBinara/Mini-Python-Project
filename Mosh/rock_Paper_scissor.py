import random

while True:
    answer = ('r', 'p','r')
    answer = input("Rock, paper, or scissors? (r/p/s):").lower()
    
    if answer == 'r' or 'p' or 's' :
        print(f"Your Chose : {answer}")
        guess = random.choice(['r','p','s'])
                
        print(f"Computer chose : {guess}")
                
        if answer == guess:
            print("You Won")
        else:
            print("You lose")
            
            cont = input("Continue? (y/n):").lower()
            if cont== 'y':
                continue
            elif cont == 'n':
                print("Ok Thanks Came to Next")
                break
            else:
                print("Invalid choice !")
                
    if answer not in 'r' and 'p' and 's':
        print("Invalid choice !")
    