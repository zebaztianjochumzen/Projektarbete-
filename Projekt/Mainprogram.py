class Goods: 
    def __init__(self, code, name , price, amount):

        self.code = code
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        pass

class Database:
    def __init__(self):
        self.goods = []
    
    def read_goods(self):
        file = open("goods.txt", "r", encoding="utf-8")
        code = file.readline().strip()
        while code:
            name = int(file.readline().strip())
            price = int(file.readline().strip())
            amount = int(file.readline().strip())
            new_goods = Goods(code,name,price,amount)
            self.goods.append(new_goods)
            code = file.readline().strip()
        file.close()

    def save_goods(self):
        file = open("goods.txt", "a", encoding="utf-8")
        self.goods.sort()
        for goods in self.goods:
            file.write(str(goods.code + "\n"))
            file.write(str(goods.name) + "\n")
            file.write(str(goods.price) + "\n")
            file.write(str(goods.amount)+ "\n")
        file.close()

    def show_goods(self):
        for goods in self.goods:
            print (goods)
    
    def new_goods(self):
        code = int(input("PLU CODE: "))
        name = int(input("NAME: "))
        price = int(input("PRICE: "))
        amount = int(input("AMOUNT "))
        new = Goods(code, name, price, amount)
        self.goods.append(new)


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
    option = menu()
    while menu != "Q":
        if option == "A":
            database.new_goods()
        elif option == "C":
            pass
        elif option == "S":
            database.show_goods()
        option =menu()
    database.save_goods()
    print("Bye!")

if __name__ == "__main__":
    main()
            




