import time

money = int(input("Hey, How much money do you have?\n"))
if money<4:
    print("Sorry you dont have enough money for our menu...")
    exit()
name = input("And whats your name?\n")
capsname = name.capitalize()
menu = ["Tomato", "Cheese", "Turkey"]
price = 4
menustr = "Tomato, Cheese and Turkey"
print("Hey " + capsname + " welcome to our restaurant!\nWe got " + menustr +
      "\nOur prices for everything are 4$")
order = input("So whats your order? \n")
capsorder = order.capitalize()
while capsorder not in menu:
    print("Sorry thats not in our menu, could you repeat the order?")
    order = input()
    capsorder = order.capitalize()
Count = int(input("How many " + capsorder + " would you like?\n"))
total = Count * price
remainder = money - total
if capsorder in menu:
    if money < total:
        print("Sorry but you dont have enough money")
    if money > total or money == total:
        print("Great ill get you that right away!")
        time.sleep(2)
        print("Here you go sir, your total is: " + str(total))
        print("You have " + str(remainder) + "$ left")
        time.sleep(20)
        print("cya")
