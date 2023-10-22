import re
import sys

# requires a strong password function
def is_strong_password(password):
    if (
        len(password) < 8
        or not re.search(r'[A-Z]', password)
        or not re.search(r'[a-z]', password)
        or not re.search(r'[0-9]', password)
        or not re.search(r'[!@#$%^&*()_+]', password)
    ):
        return False
    return True

# account creation function
def create_account():
    while True:
        username = input("Enter a username: ")
        with open("C:/Meiple-Tree-Clothing/UserData.txt", "r") as file:
            for line in file:
                account_info = line.strip().split(",")
                if len(account_info) == 4 and account_info[0] == username:
                    print("Username is already taken. Please choose another.")
                    break
            else:
                password = input("Enter a password: ")
                if is_strong_password(password):
                    email = input("Enter your email: ")
                    full_name = input("Enter your full name: ")
                    with open("C:/Meiple-Tree-Clothing/UserData.txt", "a") as file:
                        file.write(f"{username},{password},{email},{full_name}\n")
                    print("Account created successfully!")
                    break
                else:
                    print("Password is not strong enough. It should be at least 8 characters long and contain uppercase, lowercase, digit, and a special character.")
                    break

# logging in will run the base script
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("C:/Meiple-Tree-Clothing/UserData.txt", "r") as file:
        for line in file:
            account_info = line.strip().split(",")
            if len(account_info) == 4 and account_info[0] == username and account_info[1] == password:
                print("Login successful. Welcome, " + account_info[3] + "!")
                import ClothingLine
                Address = str(input("Where is your current address for delivery?: "))
                while True:
                    try:
                        PhnNumber = int(input("What is your current phone number? [+63]: "))
                        if 999999999 <= PhnNumber <= 9999999999:
                            break
                        else:
                            print('Please enter a correct phone number')
                    except ValueError:
                        print('Please enter a valid phone number')
                informationresult = str(input('Is the information presented above correct? [Y/N] :'))
                if informationresult.lower() == "y":
                    print()
                    while True:
                        print("\n__________________________Meiple Tree______________________________\n")
                        print(f'Hello! {account_info[3]} here is your order and info\n')
                        if ClothingLine.jackets_cart:
                            for item in ClothingLine.jackets_cart:
                                print(f"{item}\n")
                        if ClothingLine.shirts_cart:
                            for item in ClothingLine.shirts_cart:
                                print(f"{item}\n")
                        if ClothingLine.pants_cart:
                            for item in ClothingLine.pants_cart:
                                print(f"{item}\n")
                        if ClothingLine.hats_cart:
                            for item in ClothingLine.hats_cart:
                                print(f"{item}\n")
                        print(f'Your Address: {Address}\nYour phone number: +63{PhnNumber}')
                        print("\n____________________________________________________________________\n")
                        with open('C:/Meiple-Tree-Clothing/Resibo.txt', 'r') as file:
                            f_contents = file.read()
                            print(f_contents)
                        sys.exit()
                elif informationresult.lower() == "n":
                    print("Connection timed-out")
                    sys.exit()
                else:
                    print("Enter only Y/N.")
                break
        else:
            print("Enter Credentials Again!.")

# where the code starts
print("____________________________________________________________________")
print("""                                                                                            
        Welcome to                      
            Meiple Tree     
                           .\^/.               |
                         . |`|/| .        _|\__|__/|_  
                         |\|\|'|/|       `>.-' | '-.<`  
                      .--'-\`|/-''--.    /.-' /|' '-.\ 
                       \`-._\|./.-'/    '--.-/.|\-..--'
                        >`-._|/.-'<        |/|/|.|\|   
                       '~|/~~|~~\|~'       ' |.|\| '
                             |               '/. '
""")
print("____________________________________________________________________")

while True:
    choice = input("Do you want to create an account, login, or exit? (create/login/exit): ")
    if choice.lower() == "create":
        create_account()
    elif choice.lower() == "login":
        login()
    elif choice.lower() == "exit":
        print("Bye!")
        break
    else:
        print("Invalid choice. Please enter 'create', 'login', or 'exit'.")
