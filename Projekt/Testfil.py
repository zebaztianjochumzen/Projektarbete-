class Cashier:
    def cashier_mode():
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")
        total = []
        while True:
            input1 = input().split(" ")
            total.append(input1)
            if input1 == ["#"]:
                  break 
            else: 
                print(total)
                continue
    cashier_mode()