logo="""

                     .-.       .-.                                                            ___                                 
                    /    \    /    \                                                         (   )       .-.                      
  .--.      .--.    | .`. ;   | .`. ;    .--.     .--.      ___ .-. .-.     .---.    .--.     | | .-.   ( __)  ___ .-.     .--.   
 /    \    /    \   | |(___)  | |(___)  /    \   /    \    (   )   '   \   / .-, \  /    \    | |/   \  (''") (   )   \   /    \  
|  .-. ;  |  .-. ;  | |_      | |_     |  .-. ; |  .-. ;    |  .-.  .-. ; (__) ; | |  .-. ;   |  .-. .   | |   |  .-. .  |  .-. ; 
|  |(___) | |  | | (   __)   (   __)   |  | | | |  | | |    | |  | |  | |   .'`  | |  |(___)  | |  | |   | |   | |  | |  |  | | | 
|  |      | |  | |  | |       | |      |  |/  | |  |/  |    | |  | |  | |  / .'| | |  |       | |  | |   | |   | |  | |  |  |/  | 
|  | ___  | |  | |  | |       | |      |  ' _.' |  ' _.'    | |  | |  | | | /  | | |  | ___   | |  | |   | |   | |  | |  |  ' _.' 
|  '(   ) | '  | |  | |       | |      |  .'.-. |  .'.-.    | |  | |  | | ; |  ; | |  '(   )  | |  | |   | |   | |  | |  |  .'.-. 
'  `-' |  '  `-' /  | |       | |      '  `-' / '  `-' /    | |  | |  | | ' `-'  | '  `-' |   | |  | |   | |   | |  | |  '  `-' / 
 `.__,'    `.__.'  (___)     (___)      `.__.'   `.__.'    (___)(___)(___)`.__.'_.  `.__,'   (___)(___) (___) (___)(___)  `.__.'  
                                                                                                                                  
"""
money=0
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def report():
    
    """Giving a report """
    
    print("Water : "+str(resources["water"]))
    print("Milk : "+str(resources["milk"]))
    print("Coffee : "+str(resources["coffee"]))
    print("Money : $",money)




def checkResources(coffee_name):
    for item in coffee_name:
        if coffee_name[item]>resources[item]:
            print("sorry we dont have enough"+item)
            return False
    return True
            
        
    
    
def ProcessCoins(coffee):
    
    #counting the coins giving and verifiying if it is enough for the coffee
    print("please insert coins !!")
    quarters=float(input("how many quarters ?"))
    dimes=float(input("how many dimes ?"))
    nickles=float(input("how many nickles ?"))
    pennies=float(input("how many pennies ?"))
    total=quarters*0.25+0.1*dimes+nickles*0.05+pennies*0.01
    if total<coffee["cost"]:
        print("Not enough money.Money refunded")
    else:
        print("here is $",round(total-coffee["cost"],3),"in change")
        print("here is your coffee ")
        global money
        money+=coffee["cost"]
        ing=coffee["ingredients"]
        resources["water"]-=ing["water"]
        resources["coffee"]-=ing["coffee"]
        resources["milk"]-=ing["milk"]
        




def makeCoffee():
    is_on=True
    print(logo)
    while is_on:
        
        choice=input("​What would you like? (espresso/latte/cappuccino):")
        if choice=="report":
            report()
        elif choice=="latte":
            if checkResources(MENU[choice]["ingredients"]):
                ProcessCoins(MENU["latte"])
               
        elif choice=="espresso":
            if checkResources(MENU[choice]["ingredients"]):
                ProcessCoins(MENU["espresso"])
               
                
        elif choice=="cappucino":
            if checkResources(MENU[choice]["ingredients"]):
                ProcessCoins(MENU["cappucino"])
        elif choice=="off":
            is_on=False       
                
                
            
        
    
makeCoffee()