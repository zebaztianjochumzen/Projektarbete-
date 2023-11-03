def cashier_mode():
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")

        while True:
            inputs = input()
            if inputs == "#":
                  break 
            else: 
                continue
cashier_mode()