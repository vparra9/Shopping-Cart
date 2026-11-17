# Welcome users and explain what this program is for 
print("Welcome to Shopping Cart! There will be a menu listing items and their prices.")
print("You will choose what items you need to purchase then pay when you are ready.")

# while statement to ask how much money users have to spend 

def userMoney():
    while True:
        try:
            money = float(input("\nHow much money would you like to add today? "))
            return money # Sends money variable value out of function and exits loop
        except ValueError:
            print("\nInvalid input. Please enter a number.")

# function with while loop to see if users need to add more money
def addMoney(current_money):
    while True:
        choice = (input(f"You have ${current_money}, would you like to add more? (Y or N): ")).upper()

        if choice == "Y":
            extra = userMoney() # Uses userMoney() function to add more money
            return current_money + extra
        elif choice == "N":
            return current_money
        else:
            print("Invalid input. Please enter Y or N.")


# Ask user how much money they would like to add before shopping
balance = userMoney()
print(f"Your final balance is: ${balance:.2f}")

# Function that displays menu and allows user to choose from it

def menu():
    while True:
        print("\n----Menu----\n1. Drinks\n2. Food & Snacks\n3. Desserts")
        menuChoice = input ("Would you like to see the menu for 1. Drinks, 2. Food & snacks, 3. Desserts 4. Finish shopping? Enter 1, 2, 3, or 4.")

        # Menu choice for Drinks
        if menuChoice == "1":
            print("\n---- Drinks Menu ----\n1. Coffee -- $1.50\n2. Iced Latte -- $4.75\n3. Soda -- $2.00\n4. Bottled Water -- $1.50")
        # Menu choice for Food & Snacks
        elif menuChoice == "2":
            print("\n---- Food & Snacks Menu ----\n1. Burger -- $8.50\n2. Slice of Pizza -- $3.25\n3. Fries -- $2.75\n4. Sandwich -- $6.50")
        # Menu choice for Deserts
        elif menuChoice == "3":
            print("\n---- Deserts Menu ---- \n1. Cookie -- $1.50 \n2. Icecream -- $2.50\n3. Donut -- $1.25")
        # Ends users shopping experience
        elif menuChoice == "4":
            print("\nThanks for shopping!")
            # Handle checkout here, create checkout function and place in here.
        # Handles if user enters an invalid input
        else:
            print("\nInvalid input, please enter 1, 2, 3, or 4.")

menu()


# Handles adding more money after shopping
balance = addMoney(balance)
print(f"Your final balance is: ${balance:.2f}")


        


