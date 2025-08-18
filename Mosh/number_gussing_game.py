import random
pc_Guess = random.randint(1,100)


while True:
    try:
        
            number = int(input('Guess the number between 1 and 100 : '))
            
            if pc_Guess <number:
                print("Too high!")
                
            elif pc_Guess > number:
                print("Too low!")  
            else:
                print("Congratulation! You guessed the number.")
                break 

    except ValueError:
        print("Pleas Enter the Valid Number!")

