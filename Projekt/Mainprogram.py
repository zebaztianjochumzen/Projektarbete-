
class Goods: 
    def __init__(self, code, name , price, amount):

        self.code = code
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Product: " + str(self.name) + "\n" "Code: " + str(self.code) + "\n" "Price: " + str(self.price) + "\n" "Amount: " + str(self.amount)

class Database:
    """
    Tror att jag behöver fixa någon typ av dictionary utöver txt filen som lagrar PLU koden till ett visst namn, så att när kassören skriver in vilken koden så är det automatiskt översatt till en vara.
    """
    def transformation():



        """
        Tanken med denna funktionen är att vi ska kunna ta attributerna från Goods och lagra attributen code som key 
        och då att key:n ska kunna tillkalla rätt vara. 
        Vet dock ej hur jag ska lösa detta än.
        """

    def __init__(self):
        self.goods = []
        self.products1 = {} #Detta är en dictionary som lagrar key: Code och value: Name 
    
    def read_goods(self):
        file = open("goods.txt", "r", encoding="utf-8")#
        code = file.readline().strip()
        while code:
            name = (file.readline().strip())
            price = int(file.readline().strip())
            amount = int(file.readline().strip())
            new_goods = Goods(code,name,price,amount)
            self.goods.append(new_goods)
            self.products1.update({code: name}) # Denna biten är ny och lägger till attributen code och name. Code = key och Name = Value
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
            
        print(self.products1)
    
    def new_goods(self):
        code = int(input("PLU CODE: "))
        name = str(input("NAME: "))
        price = int(input("PRICE: "))
        amount = int(input("AMOUNT "))
        new = Goods(code, name, price, amount)
        self.goods.append(new)
        self.products1.update({code : name}) # Denna biten är ny och lägger till attributen code och name. Code = key och Name = Value

class Cashier:

    """Planen med den är funktionen är att vi ska vara i cashier mode, vilket innebär att vi ska kunna 
        uppfylla de kraven på ett användarvänligt program, där "kassören" ska kunna skriva in PLU koden 
        från databasen och sedan skriva in antalet. För att sedan kunna avsluta med #.
        """
    def cashier_mode():
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")



    def sum_products():
        """Planen med denna funktionen är att den ska beräkna det totala priset beroende på antalet produkter som kassören skriver in. Hur vet jag inte än..."""
    
    def write_out_receipt():
        """
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
    cashier = Cashier()
    option = menu()
    while menu != "Q":
        if option == "A":
            database.new_goods()
            database.save_goods()
        elif option == "S":
            print("\n")
            print("\n" "The products in the database is:")
            database.show_goods()
        if option == "C":
            cashier.cashier_mode()
        option =menu()
    print("Bye!")

if __name__ == "__main__":
    main()
 