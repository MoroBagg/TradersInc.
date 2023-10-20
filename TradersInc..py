global inventory
inventory = [50, 6, 10, 4, 13]
global money
money = 1000.00
global name
name = ""

#the London market
def LondonMarket():
    global money
    global inventory
    global name
    print("\n")
    print("Welcome to London!")
    print("Would you like to 1. Travel, 2. Buy, 3. Sell, 4. check inventory (just input the number)")
    option = input("").strip().lower()

    #travel
    if option == "1":
        print("Where would you like to go then " + str(name) + "? You can go to Warsaw, Krakow, Dublin, York, Rome and Barcelona.")
        travel = input("").strip().lower()
        if travel == "rome":
            RomeMarket()

    #selling
    elif option == "2":
        print("Here Flour and sugar is more expensive, olive oil is at its normal price and milk and eggs are cheaper.")
        flourLondon = 3.20
        milkLondon = 2
        oilLondon = 1.50
        eggLondon = 0.80
        sugarLondon = 1.60

        print("Ok " + str(name) + ", what would you like to buy? 1. Flour, 2. Milk, 3. Olive oil, 4. Eggs, 5. Sugar (just input the number)")
        buy = input("").strip().lower()

        #buying flour
        if buy == "1":
            print("Flour is at a price of £3.20 a bag, how many bags would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(flourLondon * float(amount), 2)
                print("You want to buy " + str(amount) + " bags of flour at a price of £" + str(price) + "?")
                check = input("").strip().lower()
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[0] += int(amount)
                    print("You now have " + str(inventory[0]) + " bags of flour.")
                    LondonMarket()
                elif check == "no":
                    LondonMarket()
                else:
                    print("(Invalid option)")
                    LondonMarket()

            else:

                print("(Invalid option)")
                LondonMarket()

        #buying milk
        elif buy == "2":
            print("Milk is at a price of £2 a jug, how many jugs would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(milkLondon * float(amount), 2)
                print("You want to buy " + str(amount) + " jugs of milk at a price of £" + str(price) + "?")
                check = input("").strip().lower()
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[1] += int(amount)
                    print("You now have " + str(inventory[1]) + " jugs of milk.")
                    LondonMarket()
                elif check == "no":
                    LondonMarket()
                else:
                    print("(Invalid option)")
                    LondonMarket()

            else:

                print("(Invalid option)")
                LondonMarket()


        #buying olive oil
        elif buy == "3":
            print("Olive oil is at a price of £1.50 a bottle, how many bottles would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(oilLondon * float(amount), 2)
                print("You want to buy " + str(amount) + " bottles of olive oil at a price of £" + str(price) + "?")
                check = input("").strip().lower()
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[2] += int(amount)
                    print("You now have " + str(inventory[2]) + " bottles of olive oil.")
                    LondonMarket()
                elif check == "no":
                    LondonMarket()
                else:
                    print("(Invalid option)")
                    LondonMarket()

            else:

                print("(Invalid option)")
                LondonMarket()


        #buying eggs
        elif buy == "4":
            print("Eggs are at a price of £0.80 a carton, how many cartons would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(eggLondon * float(amount), 2)
                print("You want to buy " + str(amount) + " cartons of eggs at a price of £" + str(price) + "?")
                check = input("").strip().lower()
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[3] += int(amount)
                    print("You now have " + str(inventory[3]) + " cartons of eggs.")
                    LondonMarket()
                elif check == "no":
                    LondonMarket()
                else:
                    print("(Invalid option)")
                    LondonMarket()

            else:

                print("(Invalid option)")
                LondonMarket()


        #buying sugar
        elif buy == "5":
            print("Sugar is at a price of £1.20 a bag, how many bags would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(sugarLondon * float(amount), 2)
                print("You want to buy " + str(amount) + " bags of sugar at a price of £" + str(price) + "?")
                check = input("").strip().lower()
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[4] += int(amount)
                    print("You now have " + str(inventory[4]) + " bags of sugar.")
                    LondonMarket()
                elif check == "no":
                    LondonMarket()
                else:
                    print("(Invalid option)")
                    LondonMarket()

            else:

                print("(Invalid option)")
                LondonMarket()

    ###fix error when choosing amount for when you put string rather than amount it breaks using code from favtutor
    #selling
    elif option == "3":
        print("\n"); print("When selling here, you will get less money in return then when buying from here.")
        print("The higher value the item is worth, the less you lose out on in London.")
        print("This will vary from cities across Europe."); print("\n")
        sellflourLondon = 3
        sellmilkLondon = 1.80
        selloilLondon = 1.25
        selleggLondon = 0.50
        sellsugarLondon = 0.90
        print("When selling back"); print("1. flour is worth £3"); print("2. milk is worth £1.80")
        print("3. olive oil is worth £1.25"); print("4. eggs are worth 0.50")
        print("5. sugar is worth £0.90"); print("Which do you want to sell?  (just input the number)")
        selloption = input("")

        #selling flour
        if selloption == "1":
            print("You have " + str(inventory[0]) + " bags of flour available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * sellflourLondon
            print("You sure you want to sell " + str(sellAmount) + " bags of flour for £" + str(revenue) + "?")
            check = input("").strip().lower()
            if check == "yes":
                inventory[0] = inventory[0] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[0]) + " bags of flour left.")
                LondonMarket()
            elif check == "no":
                LondonMarket()

            else:
                print("(Invalid option)")
                LondonMarket()

        #selling milk
        elif selloption == "2":
            print("You have " + str(inventory[1]) + " jugs of milk available to sell. How many do you want to sell? (just input the number)"); print("\n")
            sellAmount = int(input(""))
            revenue = sellAmount * sellmilkLondon
            print("You sure you want to sell " + str(sellAmount) + " jugs of milk for £" + str(revenue) + "?")
            check = input("").strip().lower()
            if check == "yes":
                inventory[1] = inventory[1] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[1]) + " jugs of milk left.")
                LondonMarket()
            elif check == "no":
                LondonMarket()

            else:
                print("(Invalid option)")
                LondonMarket()

        #selling olive oil
        elif selloption == "3":
            print("You have " + str(inventory[2]) + " bottles of olive oil available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * selloilLondon
            print("You sure you want to sell " + str(sellAmount) + " bottles of olive oil for £" + str(revenue) + "?")
            check = input("").strip().lower()
            if check == "yes":
                inventory[2] = inventory[2] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[2]) + " bottles of olive oil left.")
                LondonMarket()
            elif check == "no":
                LondonMarket()

            else:
                print("(Invalid option)")
                LondonMarket()

        #selling eggs
        elif selloption == "4":
            print("You have " + str(inventory[3]) + " cartons of eggs available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * selleggLondon
            print("You sure you want to sell " + str(sellAmount) + " cartons of eggs for £" + str(revenue) + "?")
            check = input("").strip().lower()
            if check == "yes":
                inventory[3] = inventory[3] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[3]) + " cartons of eggs left.")
                LondonMarket()
            elif check == "no":
                LondonMarket()

            else:
                print("(Invalid option)")
                LondonMarket()
            
        #selling sugar
        elif selloption == "5":
            print("You have " + str(inventory[4]) + " bags of sugar available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * sellsugarLondon
            print("You sure you want to sell " + str(sellAmount) + " bags of sugar for £" + str(revenue) + "?")
            check = input("").strip().lower()
            if check == "yes":
                inventory[4] = inventory[4] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[4]) + " bags of sugar left.")
                LondonMarket()
            elif check == "no":
                LondonMarket()

            else:
                print("(Invalid option)")
                LondonMarket()
                

    #printing your inventory so you are aware of how much of everything you have
    elif option == "4":
        print("Ok then " + str(name) + ". You have " + str(inventory[0]) + " bags of flour, " + str(inventory[1]) + " jugs of milk, ")
        print(str(inventory[2]) + " bottles of olive oil, " + str(inventory[3]) + " eggs and " + str(inventory[4]) + " bags of sugar.")
        LondonMarket()

    else:
        print("(Invalid option)")
        LondonMarket()



#the Rome market
def RomeMarket():
    global money
    global inventory
    print("\n")
    print("Welcome to Rome!")
    print("Would you like to 1. Travel, 2. Buy, 3. Sell, 4. check inventory (just input the number)")
    option = input("")

    #travel
    if option == "1":
        print("Where would you like to go then " + str(name) + "? You can go to Warsaw, Krakow, Dublin, York, London and Barcelona.")
        travel = input("").strip().lower()
        if travel == "l
        ondon":
            LondonMarket()

    #selling
    elif option == "2":
        print("Here milk and oil is more expensive, sugar is at its normal price and flour and eggs are cheaper.")
        flourRome = 3
        milkRome = 2.40
        oilRome = 1.90
        eggRome = 0.6
        sugarRome = 1.50

        print("Ok " + str(name) + ", what would you like to buy? 1. Flour, 2. Milk, 3. Olive oil, 4. Eggs, 5. Sugar (just input the number)")
        buy = input("")

        #buying flour
        if buy == "1":
            print("Flour is at a price of £3 a bag, how many bags would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(flourRome * float(amount), 2)
                print("You want to buy " + str(amount) + " bags of flour at a price of £" + str(price) + "?")
                check = input("")
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[0] += int(amount)
                    print("You now have " + str(inventory[0]) + " bags of flour.")
                    RomeMarket()
                elif check == "no":
                    RomeMarket()
                else:
                    print("(Invalid option)")
                    RomeMarket()

            else:

                print("(Invalid option)")
                RomeMarket()
                
            

        #buying milk
        elif buy == "2":
            print("Milk is at a price of £2.40 a jug, how many jugs would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            price = round(milkRome * float(amount), 2)
            if amount.isdigit():

                price = round(milkRome * float(amount), 2)
                print("You want to buy " + str(amount) + " jugs of milk at a price of £" + str(price) + "?")
                check = input("")
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[1] += int(amount)
                    print("You now have " + str(inventory[1]) + " jugs of milk.")
                    RomeMarket()
                elif check == "no":
                    RomeMarket()
                else:
                    print("(Invalid option)")
                    RomeMarket()

            else:

                print("(Invalid option)")
                RomeMarket()

        #buying olive oil
        elif buy == "3":
            print("Olive oil is at a price of £1.90 a bottle, how many bottles would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(oilRome * float(amount), 2)
                print("You want to buy " + str(amount) + " bottles of olive oil at a price of £" + str(price) + "?")
                check = input("")
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[2] += int(amount)
                    print("You now have " + str(inventory[2]) + " bottles of olive oil.")
                    RomeMarket()
                elif check == "no":
                    RomeMarket()
                else:
                    print("(Invalid option)")
                    RomeMarket()

            else:

                print("(Invalid option)")
                RomeMarket()

        #buying eggs
        elif buy == "4":
            print("Eggs are at a price of £0.60 a carton, how many cartons would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(eggRome * float(amount), 2)
                print("You want to buy " + str(amount) + " cartons of eggs at a price of £" + str(price) + "?")
                check = input("")
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[3] += int(amount)
                    print("You now have " + str(inventory[3]) + " cartons of eggs.")
                    RomeMarket()
                elif check == "no":
                    RomeMarket()
                else:
                    print("(Invalid option)")
                    RomeMarket()

            else:

                print("(Invalid option)")
                RomeMarket()

        #buying sugar
        elif buy == "5":
            print("Sugar is at a price of £1.20 a bag, how many bags would you like? (You have £" + str(money) + " right now)")
            amount = input("")
            if amount.isdigit():

                price = round(sugarRome * float(amount), 2)
                print("You want to buy " + str(amount) + " bags of sugar at a price of £" + str(price) + "?")
                check = input("")
                if check == "yes" and money >= price:
                    money -= price
                    print("You now have £" + str(money))
                    inventory[4] += int(amount)
                    print("You now have " + str(inventory[4]) + " bags of sugar.")
                    RomeMarket()
                elif check == "no":
                    RomeMarket()
                else:
                    print("(Invalid option)")
                    RomeMarket()

            else:

                print("(Invalid option)")
                RomeMarket()

    ###fix error when choosing amount for when you put string rather than amount it breaks using code from favtutor
    #selling
    elif option == "3":
        print("\n"); print("When selling here, you will get less money in return then when buying from here.")
        print("If the item is of high value you will get 50p less in return, of normal value 30p less and of low value 20p less.")
        print("This will vary from cities across Europe."); print("\n")
        sellflourRome = 2.50
        sellmilkRome = 1.90
        selloilRome = 1.40
        selleggRome = 0.30
        sellsugarRome = 0.60
        print("When selling back"); print("1. flour is worth £2.50"); print("2. milk is worth £1.90")
        print("3. olive oil is worth £1.40"); print("4. eggs are worth 0.30")
        print("5. sugar is worth £0.60"); print("Which do you want to sell?  (just input the number)")
        selloption = input("")

        #selling flour
        if selloption == "1":
            print("You have " + str(inventory[0]) + " bags of flour available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * sellflourRome
            print("You sure you want to sell " + str(sellAmount) + " bags of flour for £" + str(revenue) + "?")
            check = input("")
            if check == "yes":
                inventory[0] = inventory[0] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[0]) + " bags of flour left.")
                RomeMarket()
            elif check == "no":
                RomeMarket()

            else:
                print("(Invalid option)")
                RomeMarket()

        #selling milk
        elif selloption == "2":
            print("You have " + str(inventory[1]) + " jugs of milk available to sell. How many do you want to sell? (just input the number)"); print("\n")
            sellAmount = int(input(""))
            revenue = sellAmount * sellmilkRome
            print("You sure you want to sell " + str(sellAmount) + " jugs of milk for £" + str(revenue) + "?")
            check = input("")
            if check == "yes":
                inventory[1] = inventory[1] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[1]) + " jugs of milk left.")
                RomeMarket()
            elif check == "no":
                RomeMarket()

            else:
                print("(Invalid option)")
                RomeMarket()

        #selling olive oil
        elif selloption == "3":
            print("You have " + str(inventory[2]) + " bottles of olive oil available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * selloilRome
            print("You sure you want to sell " + str(sellAmount) + " bottles of olive oil for £" + str(revenue) + "?")
            check = input("")
            if check == "yes":
                inventory[2] = inventory[2] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[2]) + " bottles of olive oil left.")
                RomeMarket()
            elif check == "no":
                RomeMarket()

            else:
                print("(Invalid option)")
                RomeMarket()

        #selling eggs
        elif selloption == "4":
            print("You have " + str(inventory[3]) + " cartons of eggs available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * selleggRome
            print("You sure you want to sell " + str(sellAmount) + " cartons of eggs for £" + str(revenue) + "?")
            check = input("")
            if check == "yes":
                inventory[3] = inventory[3] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[3]) + " cartons of eggs left.")
                RomeMarket()
            elif check == "no":
                RomeMarket()

            else:
                print("(Invalid option)")
                RomeMarket()
            
        #selling sugar
        elif selloption == "5":
            print("You have " + str(inventory[4]) + " bags of sugar available to sell. How many do you want to sell? (just input the number)")
            sellAmount = int(input(""))
            revenue = sellAmount * sellsugarRome
            print("You sure you want to sell " + str(sellAmount) + " bags of sugar for £" + str(revenue) + "?")
            check = input("")
            if check == "yes":
                inventory[4] = inventory[4] - sellAmount
                money = money + revenue
                print("You made £" + str(revenue) + " and have £" + str(money) + " now.")
                print("You have " + str(inventory[4]) + " bags of sugar left.")
                RomeMarket()
            elif check == "no":
                RomeMarket()

            else:
                print("(Invalid option)")
                RomeMarket()
                

    #printing your inventory so you are aware of how much of everything you have
    elif option == "4":
        print("Ok then " + str(name) + ". You have " + str(inventory[0]) + " bags of flour, " + str(inventory[1]) + " jugs of milk, ")
        print(str(inventory[2]) + " bottles of olive oil, " + str(inventory[3]) + " eggs and " + str(inventory[4]) + " bags of sugar.")
        RomeMarket()

    else:
        print("(Invalid option)")
        RomeMarket()


























def StartCode():
    global name
    print("Welcome to the world of trading at TradersInc.")
    print("What's your name trader?")
    name = input("")
    print("Nice to meet you " + str(name) + " I'll take you to London where you can start off your trading empire!")
    LondonMarket()

StartCode()
