import sys

# for quantity of the items 
def get_quantity():
    while True:
        quantity = int(input("Enter the quantity: "))
        if quantity > 0:
            return quantity
        else:
            print("Please enter a valid quantity.")

# for types of items to buy 
def get_clothing_line():
    while True:
        clothing_line = str(input("Select your thrift [shirts, jackets, pants, or hats]: "))
        if clothing_line in ["shirts", "jackets", "pants", "hats"]:
            return clothing_line

# for size of the items
def get_size():
    sizes_data = {
        "small": {
            "name": "small",
            "cost": 5
        },
        "medium": {
            "name": "medium",
            "cost": 10
        },
        "large": {
            "name": "large",
            "cost": 15
        }
    }
    while True:
        size = str(input("Enter your size [small, medium, large]: "))
        if size in sizes_data:
            data = sizes_data[size]
            return data, data['cost']
        else:
            print("enter only small, medium, or large!")

print("____________________________________________________________________")
print("""                                                                                            
                              
    Meiple Tree Clothing
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

# lists
jackets_cart = []
shirts_cart = []
hats_cart = []
pants_cart = []

# main script
while True:
    control = str(input("Do you want to browse our shop? Y (yes) N (check out) E (exit): "))
    if control.lower() == "y":
        size, size_cost = get_size()
        print(f"The added cost of {size['name']} size is {size_cost} pesos.")

        # jackets
        def get_jackets():
            jackets_data = {
                "varsity": {
                    "name": "varsity",
                    "cost": 450
                },
                "plain": {
                    "name": "plain",
                    "cost": 400
                },
                "bomber": {
                    "name": "bomber",
                    "cost": 500
                },
                "flannel": {
                    "name": "flannel",
                    "cost": 600
                }
            }
            while True:
                jacket = str(input("Select either [varsity, plain, bomber, or flannel]: "))
                if jacket in jackets_data:
                    data = jackets_data[jacket]
                    print(f"{data['name']} jackets cost {data['cost']} pesos")
                    return data, data['cost']
                else:
                    print("Enter only 'varsity', 'plain', 'bomber', or 'flannel'!")

        # shirts
        def get_shirts():
            shirts_data = {
                "graphic": {
                    "name": "graphic",
                    "cost": 400
                },
                "plain": {
                    "name": "plain",
                    "cost": 300
                },
                "polo": {
                    "name": "polo",
                    "cost": 500
                }
            }
            while True:
                shirt = str(input("Select either [graphic, plain, or polo]: "))
                if shirt in shirts_data:
                    data = shirts_data[shirt]
                    print(f"{data['name']} shirts cost {data['cost']} pesos")
                    return data, data['cost']
                else:
                    print("Enter only 'graphic', 'plain', or 'polo'!")

        # pants
        def get_pants():
            pants_data = {
                "denim": {
                    "name": "denim",
                    "cost": 500
                },
                "cargo": {
                    "name": "cargo",
                    "cost": 450
                },
                "wide": {
                    "name": "wide",
                    "cost": 500
                },
                "ankle": {
                    "name": "ankle",
                    "cost": 400
                }
            }
            while True:
                pant = str(input("Select either [denim, cargo, wide, or ankle]: "))
                if pant in pants_data:
                    data = pants_data[pant]
                    print(f"{data['name']} pants cost {data['cost']} pesos")
                    return data, data["cost"]
                else:
                    print("Enter only 'denim', 'cargo', 'wide', or 'ankle'!")

        # hats
        def get_hats():
            hats_data = {
                "branded": {
                    "name": "branded",
                    "cost": 200
                },
                "beanie": {
                    "name": "beanie",
                    "cost": 300
                },
                "bucket": {
                    "name": "bucket",
                    "cost": 200
                }
            }
            while True:
                hat = str(input("Select either [branded, beanie, or bucket]: "))
                if hat in hats_data:
                    data = hats_data[hat]
                    print(f"{data['name']} hats cost {data['cost']} pesos")
                    return data, data['cost']
                else:
                    print("Enter only 'branded', 'beanie', or 'bucket'!")

        clothing_line = get_clothing_line()

        if clothing_line == "jackets":
            data, cost = get_jackets()
            quantity = get_quantity()
            jacket_cost = cost * quantity
            jackets_cart.append(f"jacket/s: {data['name']},  quantity: {quantity}, cost: {jacket_cost}")
            print("that would be", jacket_cost, "pesos")
            print("Item has been added to the cart.")
        elif clothing_line == "shirts":
            data, cost = get_shirts()
            quantity = get_quantity()
            shirts_cost = cost * quantity
            shirts_cart.append(f"shirt/s: {data['name']}, quantity: {quantity}, cost: {shirts_cost}")
            print("that would be", shirts_cost, "pesos")
            print("Item has been added to the cart.")
        elif clothing_line == "pants":
            data, cost = get_pants()
            quantity = get_quantity()
            pants_cost = cost * quantity
            pants_cart.append(f"pants: {data['name']}, quantity: {quantity}, cost: {pants_cost}")
            print("that would be", pants_cost, "pesos")
            print("Item has been added to the cart.")
        elif clothing_line == "hats":
            data, cost = get_hats()
            quantity = get_quantity()
            hats_cost = cost * quantity
            hats_cart.append(f"hat/s: {data['name']}, quantity: {quantity}, cost: {hats_cost}")
            print("that would be", hats_cost, "pesos")
            print("Item has been added to the cart.")
    elif control.lower() == "n":
    # script for the cart
        while True:
            print("\n_____________________Your Meiple Tree Cart_________________________\n")
            if jackets_cart:
                for item in jackets_cart:
                    print(f"{item}\n")
            if shirts_cart:
                for item in shirts_cart:
                    print(f"{item}\n")
            if pants_cart:
                for item in pants_cart:
                    print(f"{item}\n")
            if hats_cart:
                for item in hats_cart:
                    print(f"{item}\n")
            print("\n____________________________________________________________________\n")
            cart_response = str(input("Are you sure on your current purchase? Y/N: "))
            print()
            if cart_response.lower() == "y":
                break
            elif cart_response.lower() == "n":
                print("Thank you for thrifting with us!")
                sys.exit()
            else:
                print("Please enter either Y (yes) or N (no) only")
        break        
    elif control.lower() == "e":
        print("Please come again!")
        sys.exit()
        #please fix
    else:
        print("Input either Y/N/E: ")
        
# delete line 