class Goods: 
    def __init__(self, code, name , price, amount):

        self.code = code
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Product: " + str(self.name) + "\n" "Code: " + str(self.code) + "\n" "Price: " + str(self.price) + "\n" "Amount: " + str(self.amount)

class Database:
    """ Tror att jag behöver fixa någon typ av dictionary utöver txt filen som lagrar PLU koden till ett visst namn, så att när kassören skriver in vilken koden så är det automatiskt översatt till en vara.
    """
    def transformation():
        """
        Tanken med denna funktionen är att vi ska kunna ta attributerna från Goods och lagra attributen code som key 
        och då att key:n ska kunna tillkalla rätt vara. 
        Vet dock ej hur jag ska lösa detta än.
        """

    def __init__(self):
        self.goods = []
        self.products = {} #Detta är en dictionary som lagrar key: Code och value: Name 
        self.products_price = {}
        self.products_amount = {}
    
    def read_goods(self):
        file = open("goods.txt", "r", encoding="utf-8")
        code = file.readline().strip()
        while code:
            name = (file.readline().strip())
            price = int(file.readline().strip())
            amount = int(file.readline().strip())
            new_goods = Goods(code,name,price,amount)
            self.goods.append(new_goods)
            self.products.update({code : name}) # Denna biten är ny och lägger till attributen code och name. Code = key och Name = Value
            self.products_price.update({code : price})
            self.products_amount.update({code : amount})
            code = file.readline().strip()
        file.close()

    def save_goods(self):
        file = open("goods.txt", "w", encoding="utf-8")
        for goods in self.goods:
            file.write(str(goods.code) + "\n")
            file.write(str(goods.name) + "\n")
            file.write(str(goods.price) + "\n")
            file.write(str(goods.amount)+ "\n")
        file.close()

    def show_goods(self):
        for products in self.goods:
            print(products)
        print(self.products)
        print(self.products_price)
        print(self.products_amount)
    
    def new_goods(self):
        code = int(input("PLU CODE: "))
        name = str(input("NAME: "))
        price = int(input("PRICE: "))
        amount = int(input("AMOUNT "))
        new = Goods(code, name, price, amount)
        self.goods.append(new)
        self.products.update({code : name,})
        self.products_price.update({code : price})
        self.products_amount.update({code : amount}) # Denna biten är ny och lägger till attributen code och name. Code = key och Name = Value
    
    def cashier_mode(self):
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")
        self.cart = []
        self.price = []
        total = 0
        
        while True:
            user_input = (input().split(" "))
            if user_input[0] == "#":
                    break
            if all(element.isdigit() for element in user_input):
                if user_input[0] in self.products:
                    self.cart.append(self.products[user_input[0]])
                    if len(user_input) is 1:
                        self.cart.append(1)
                    else:
                        self.cart.append(user_input[1])
                else:
                    print("That item does not exist")
                    continue
            else:
                print("Invalid Input")
            """
            If statementet nedan kollar om user_input är kopplat till ett pris, alltså att varan man skriver in är ett pris
            Det som händer då är att den multiplicerar den andra delen av user_input och sen lägger till det i en lista. 
            Detta gör alltså att man kan se totalpriset baserat för varje vara baserat på hur många varor man köper.

            """
            if user_input[0] in self.products_price:
                self.price.append((self.products_price[user_input[0]] * int(user_input[1])))
            else:
                print("The product that you wrote does not have an assigned price\nPlease try again")

        """
        Det denna den for loopen under gör att den tar listan self.price och sen så tar den och summerar alla positionerna med ett
        specefikt värde med varandra så att man får en total summa. 
        """
        
        for i in self.price:
            total += int(i)
            
        print("The item in your cart is:",self.cart)
        print(self.price)
        print("Total", total)

        
        
        """while True:
            input1 = input().split(" ")
            cart.append(input1)
            print(cart)
            if input1 == "#":
                  break 
            else: 
                print(cart)
                continue"""

    """
    def cashier_mode(self):
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")
        total = []
        while True:
            input1 = input().split(" ")
            total.append(input1)
            
            if input1 = self.pr
                continue
            elif input1 == ["#"]:
                  break 
            else: 
                print(total)
                continue
              
    def sum_products():
        Planen med denna funktionen är att den ska beräkna det totala priset beroende på antalet produkter som kassören skriver in. Hur vet jag inte än...
        
    def write_out_receipt():
      
        Har absolut ingen aning om hur jag ska framställa kvittot än lol.
    """

def menu():
    print("-------------------------------")
    print("A Add goods")
    print("C Cashier mode")
    print("S Show all Goods")
    print("Q Quit")
    option = input("What do you want to do? ").upper()
    return option 

def main():
    print("Welcome")
    print("---------------------------------")
    database = Database()
    database.read_goods()
    cashier = database
    option = menu()
    while True != "Q":
        if option == "A":
            database.new_goods()
            database.save_goods()
            break
        elif option == "S":
            print("\n")
            print("\n" "The products in the database is:")
            database.show_goods()
            break
        if option == "C":
            database.read_goods()
            cashier.cashier_mode()
            break
        elif option == "Q":
            print("Bye!")
            quit()
        option =menu()
if __name__ == "__main__":
    main()