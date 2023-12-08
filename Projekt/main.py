#Zebaztian Jochumzen | 145 Varuprisdatabas
import pandas as pd
import csv
class Good: 
    """This class defines what a good actually is, and which attribute each good has"""
    def __init__(self, code, name , price, amount):

        self.code = code
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Product: " + str(self.name) + "\n" "Code: " + str(self.code) + "\n" "Price: " + str(self.price) + "\n" "Amount: " + str(self.amount)

class Database:
    """This class defines the database, it stores all the goods and contains the function cashier mode"""

    def __init__(self):
        """This creates the different lists and dictionaries to enable the cashier function to have its funtionality"""
        self.goods = []
        self.products = {} #Detta är en dictionary som lagrar key: Code och value: Name 
        self.products_price = {}
        self.products_amount = {}
    
    def read_goods(self):
        """ This function reads from the goods list, it reads from the file goods.txt"""
        file = open("goods.txt", "r", encoding="utf-8")
        code = file.readline().strip()
        while code:
            name = (file.readline().strip())
            price = int(file.readline().strip())
            amount = int(file.readline().strip())
            new_goods = Good(code,name,price,amount)
            self.goods.append(new_goods)
            self.products.update({code : name}) # Denna biten är ny och lägger till attributen code och name. Code = key och Name = Value
            self.products_price.update({code : price})
            self.products_amount.update({code : amount})
            code = file.readline().strip()
        file.close()

    
    def cashier_mode(self):
        """ This function is the main part of the program, its the user friendly part where you cant actually write in the products you want to add.
            It also contains error handeling, so you can not write in odd inputs.
        """
        print("You have now entered the cashier mode:")
        print("Just write out the product codes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")
        self.cart = []
        self.cart2= []
        self.price = []
        self.number_products = {}
        self.total = []
        
        while True:
            user_input = (input().split(" "))
            if user_input[0] == "#":
                    break
            if all(element.isdigit() for element in user_input):
                if user_input[0] in self.products:
                    if len(user_input) <=1:
                        print("Enter a valid amount")
                        continue
                    if int(user_input[1]) > self.products_amount[user_input[0]]:
                            print("The amount you typed in does not exist")    
                    
                    elif user_input[0] in self.products_price:
                        price = ((self.products_price[user_input[0]] * int(user_input[1])))
                        self.price.append(price)
                        self.cart.append([self.products[user_input[0]],user_input[1],self.products_price[user_input[0]],price])
                        
                        
                else:
                    print("That item does not exist")
                    continue
            else:
                print("Invalid Input")
        print(self.cart)


    def write_out_recipiet(self):
        """
        This function writes out the recipiet to the file named receipt.txt
        """
        total = 0
        for i in self.price:
            total += int(i)
            self.total.append(total)
        file = open("receipt.txt", "w", encoding="utf-8")
        recipt = ("Products" +"      " + "Amount" +"     "+"A-Price"+"    "+"Price")
        line = ("--------------------------------------------")
        file.write(recipt +"\n" + line ) 
        
        for index, i in enumerate(self.cart):
            if(index % 4 == 0):
                file.write("\n")
            file.writelines(str(i)+ "         ")
        file.write
        file.write("\n"+ "Total" + "                                " + str(total))
        file.close()
        
        """
        This function writes out the recipiet to the file named receipt.txt
            """
        with open("receipt.csv", "w", newline="",encoding="utf-8") as file:
            fields = ("Products","Amount","A-Price","Price")
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(self.cart)
            
            df = pd.read_csv("receipt.csv")
            price_sum = df["Price"].sum()
            print("Total Price:", price_sum)
            
#Använd remove, för att fixa så att vi kan ta bort spefecika produkter från den totala listan. 
#Använd en funktion som kollar och ändrar en listposition så att man kan ändra antalet i listan. 
#Lägg till och använd pandas så att vi summerar den sista kolumnen och lägger en print sats i slutet av csv filen. 
            
def menu():
    print("-------------------------------")
    print("C Cashier mode")
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
            cashier.write_out_recipiet()
            break
        elif option == "Q":
            print("Bye!")
            quit()
        option =menu()
if __name__ == "__main__":
    main()
