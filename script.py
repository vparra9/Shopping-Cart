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
            print("\nInvalid input. Please enter a number: ")

# function with while loop to see if users need to add more money
def addMoney(current_money):
    while True:
        choice = (input(f"Your current balance is ${current_money:.2f}, would you like to add more? (Y or N): ")).upper()

        if choice == "Y":
            extra = userMoney() # Uses userMoney() function to add more money
            return current_money + extra
        elif choice == "N":
            return current_money
        else:
            print("Invalid input. Please enter Y or N: ")


# Ask user how much money they would like to add before shopping
balance = userMoney()
print(f"Your final balance is: ${balance:.2f}")

# Function that displays menu and allows user to choose from it

def menu(balance):
    while True:
        print("\n----Menu----\n1. Drinks\n2. Food & Snacks\n3. Desserts")
        menuChoice = input ("Would you like to see the menu for 1. Drinks, 2. Food & snacks, 3. Desserts 4. Finish shopping? Enter 1, 2, 3, or 4: ")

        # Menu choice for Drinks
        if menuChoice == "1":
            # While loop to allow user to shop in the Drinks Menu
            while True:
                print("\n---- Drinks Menu ----\n1. Coffee -- $1.50\n2. Iced Latte -- $4.75\n3. Soda -- $2.00\n4. Bottled Water -- $1.50")
                drinkChoice = input("\nEnter 1, 2, 3, or 4 for the drink you would like and 5 to exit the drinks menu: ").strip()
                print(f"DEBUG: You selected {drinkChoice}")
                if drinkChoice == "1":
                    while True:
                        cost = 1.50 
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your coffee!")
                            print(f"Remaining balance: ${balance:.2f} ")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")

                    # Then add in a function or if statement that checks if balance is too low, and then it will call addMoney
                if drinkChoice == "2":
                    while True:
                        cost = 1.50 
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your iced latte!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase: ")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    
                if drinkChoice == "3":
                    while True:
                        cost = 1.50 
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your soda!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    

                if drinkChoice == "4":
                    while True:
                        cost = 1.50 
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your bottled water!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    
                if drinkChoice == "5":
                    print("Exiting drink menu.")
                    break

        ##########################################################################
        # Menu choice for Food & Snacks
        elif menuChoice == "2":
            while True:
                print("\n---- Food & Snacks Menu ----\n1. Burger -- $8.50\n2. Slice of Pizza -- $3.25\n3. Fries -- $2.75\n4. Sandwich -- $6.50")
                foodChoice = input("\nEnter 1, 2, 3, or 4 for the food/snack you would like and 5 to exit the Food & Snacks menu: ").strip()
                print(f"DEBUG: You selected {foodChoice}")

                if foodChoice == "1":
                    while True:
                        cost = 8.50
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your burger!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to food and snacks menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                if foodChoice == "2":
                    while True:
                        cost = 3.25
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your slice of pizza!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
            
                if foodChoice == "3":
                    while True:
                        cost = 2.75
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere are your fries!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to food and snacks menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    
                if foodChoice == "4":
                    while True:
                        cost = 6.50
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your sandwich!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to food and snacks menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    
                if foodChoice == "5":
                    print("Exiting food & snacks menu.")
                    break        
               

#########################################################################
        # Menu choice for Deserts
        elif menuChoice == "3":
            while True:
                print("\n---- Deserts Menu ---- \n1. Cookie -- $1.50 \n2. Icecream -- $2.50\n3. Donut -- $1.25")

                desertChoice = input("\nEnter 1, 2, or 3 for the desert you would like and 4 to exit the Deserts menu: ").strip()
                print(f"DEBUG: You selected {desertChoice}")

                if desertChoice == "1":
                    while True:
                        cost = 1.50
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your cookie!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to deserts menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                if desertChoice == "2":
                    while True:
                        cost = 2.50
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your icecream!")
                            print(f"\nCurrent balance: {balance:.2f}")
                            
                            break # Will exit and return back to drink menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
            
                if desertChoice == "3":
                    while True:
                        cost = 1.25
                        # Check to make sure there is enough money in their balance
                        if balance >= cost:
                            balance = balance - cost
                            print("\nHere is your donut!")
                            print(f"\nCurrent balance: {balance:.2f}")

                            break # Will exit and return back to food and snacks menu
                        # If there is not enough money have them add more money through addMoney() 
                        else:
                            print("\nYou do not have enough money to complete this purchase.")
                            old_balance = balance # Keep track of current balance before adding more money 
                            balance = addMoney(balance)
                            # If user selects no to adding more money
                            if old_balance == balance:
                                print("Purchase cancelled")
                                break # Escapes loop
                            print(f"\nCurrent balance: {balance:.2f}")
                    
                if desertChoice == "4":
                    print("Exiting deserts menu.")
                    break

        # Ends users shopping experience
        elif menuChoice == "4":
            print("\nThanks for shopping!")
            break
            
            # Handle checkout here, create checkout function and place in here.
        # Handles if user enters an invalid input
        else:
            print("\nInvalid input, please enter 1, 2, 3, or 4.")

menu(balance)




        


