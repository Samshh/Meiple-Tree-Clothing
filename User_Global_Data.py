import re

# dictionary for the accounts
user_accounts = {}  

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
        if username in user_accounts:
            print("Username is already taken. Please choose another.")
        else:
            password = input("Enter a password: ")
            if is_strong_password(password):
                user_accounts[username] = {
                    "password": password,
                    "email": input("Enter your email: "),
                    "full_name": input("Enter your full name: "),
                }
                print("Account created successfully!")
                break
            else:
                print("Password is not strong enough. It should be at least 8 characters long and contain uppercase, lowercase, digit, and special character.")

# logging in will run the base script
def login():
    username = input("Enter your username: ")
    if username in user_accounts:
        password = input("Enter your password: ")
        if user_accounts[username]["password"] == password:
            print("Login successful. Welcome, " + user_accounts[username]["full_name"] + "!")
            # base script will run
            import ClothingLine
            # main script for delivery and cart
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
                    print(f'Hello! {user_accounts[username]["full_name"]} here is your order and info\n')
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
                    print(f'''Your Address: {Address}
Your phone number: +63{PhnNumber}''')
                    print("\n____________________________________________________________________\n")
                    with open('C:\SCdVSC\PythonProgs\Projects\Resibo.txt', 'r') as f:
                        f_contents = f.read()
                        print(f_contents)
                    break
            if informationresult.lower() == "n":
                print("Kindly Double Check the information")
            else:
                print("")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please create an account first.")

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
        break
    else:
        print("Invalid choice. Please enter 'create', 'login', or 'exit'.")
