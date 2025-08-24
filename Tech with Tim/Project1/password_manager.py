pwd = input("What is the Master Password? ")

def view():
    with open('passwordsnew.txt', 'r') as f:
        for line in f.readlines():
            print(line)




def add():
    name = input('Account Name:')
    
    pwd = input("Password: ")
    
    with open('passwordsnew.txt', 'a') as f:
        f.write("=========New==========\n")
        f.write(f"Name: {name}  \nPassword :{pwd} \n")
        






    


while True:
    mode = input("Would you like to add a new password or view existing ones (view,add)? ")

    if mode == "q":
        break
        
        
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue