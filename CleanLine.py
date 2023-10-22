import sys

# Define clothing data
clothing_data = {
    "jackets": {
        "varsity": {"name": "varsity", "cost": 450},
        "plain": {"name": "plain", "cost": 400},
        "bomber": {"name": "bomber", "cost": 500},
        "flannel": {"name": "flannel", "cost": 600}
    },
    "shirts": {
        "graphic": {"name": "graphic", "cost": 400},
        "plain": {"name": "plain", "cost": 300},
        "polo": {"name": "polo", "cost": 500}
    },
    "pants": {
        "denim": {"name": "denim", "cost": 500},
        "cargo": {"name": "cargo", "cost": 450},
        "wide": {"name": "wide", "cost": 500},
        "ankle": {"name": "ankle", "cost": 400}
    },
    "hats": {
        "branded": {"name": "branded", "cost": 200},
        "beanie": {"name": "beanie", "cost": 300},
        "bucket": {"name": "bucket", "cost": 200}
    }
}

# Get user input for quantity, clothing line, and size
def get_quantity():
    while True:
        quantity = int(input("Enter the quantity: "))
        if quantity > 0:
            return quantity
        else:
            print("Please enter a valid quantity.")

def get_clothing_line():
    while True:
        clothing_line = input("Select your thrift [shirts, jackets, pants, or hats]: ").lower()
        if clothing_line in clothing_data:
            return clothing_line
        else:
            print("Enter only 'shirts', 'jackets', 'pants', or 'hats'.")

def get_size():
    sizes_data = {
        "small": {"name": "small", "cost": 5},
        "medium": {"name": "medium", "cost": 10},
        "large": {"name": "large", "cost": 15}
    }
    while True:
        size = input("Enter your size [small, medium, large]: ").lower()
        if size in sizes_data:
            return sizes_data[size]
        else:
            print("Enter only 'small', 'medium', or 'large'!")

# Initialize shopping carts
jackets_cart = []
shirts_cart = []
hats_cart = []
pants_cart = []

print("Welcome to Meiple Tree Clothing")

while True:
    control = input("Do you want to browse our shop? (Y) Yes, (N) Check out, (E) Exit: ").lower()
    
    if control == "y":
        size = get_size()
        print(f"The added cost of {size['name']} size is {size['cost']} pesos.")
        
        clothing_line = get_clothing_line()
        data = clothing_data[clothing_line]
        
        print(f"{data['name']} {clothing_line} costs {data['cost']} pesos")
        
        quantity = get_quantity()
        item_cost = data['cost'] * quantity
        
        if clothing_line == "jackets":
            jackets_cart.append(f"jacket/s: {data['name']}, quantity: {quantity}, cost: {item_cost} pesos")
        elif clothing_line == "shirts":
            shirts_cart.append(f"shirt/s: {data['name']}, quantity: {quantity}, cost: {item_cost} pesos")
        elif clothing_line == "pants":
            pants_cart.append(f"pants: {data['name']}, quantity: {quantity}, cost: {item_cost} pesos")
        elif clothing_line == "hats":
            hats_cart.append(f"hat/s: {data['name']}, quantity: {quantity}, cost: {item_cost} pesos")
        
        print(f"That would be {item_cost} pesos")
        print("Item has been added to the cart.")
    
    elif control == "n":
        # Checkout
        print("\nYour Meiple Tree Cart:")
        for cart in [jackets_cart, shirts_cart, pants_cart, hats_cart]:
            for item in cart:
                print(item)
        cart_response = input("Are you sure about your current purchase? (Y) Yes, (N) No: ").lower()
        if cart_response == "y":
            print("Thank you for shopping with us!")
            sys.exit()
    
    elif control == "e":
        print("Please come again!")
        sys.exit()
    
    else:
        print("Enter either 'Y' for Yes, 'N' for No, or 'E' for Exit.")
