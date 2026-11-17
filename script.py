print("Welcome to Shopping Cart! There will be a menu listing items and their prices.")
print("You will choose what items you need to purchase then pay when you are ready.")

while True:
    try:
        money = float(input("How much money do you have to spend today? "))
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

while True:
    try:
        addMoney = float(input(f"You have ${money}. Do you need to add? (Y OR N)")
        break
    except ValueError:
        print("Invalid")


