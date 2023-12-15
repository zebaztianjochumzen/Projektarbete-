#Zebaztian Jochumzen | 145 Varuprisdatabas
import pandas as pd
import csv
import errorhandeling as er
class Good: 
    """This class defines what a good actually is, and which attribute each good has"""
    def __init__(self, code, name , price, amount):

        self.code = code
        self.name = name
        self.price = price
        self.amount = amount

    def __str__(self):
        return "Product: " + str(self.name) + "\n" "Code: " + str(self.code) + "\n" "Price: " + str(self.price) + "\n" "Amount: " + str(self.amount)

class Cashier:
    """This class defines the database, it stores all the goods and contains the function cashier mode"""

    def __init__(self):
        """This creates the different lists and dictionaries to enable the cashier function to have its funtionality"""
        #self.goods = []
        self.products = {}
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
            #self.goods.append(new_goods)
            self.products.update({code : name}) 
            self.products_price.update({code : price})
            self.products_amount.update({code : amount})
            code = file.readline().strip()
        file.close()

    
    def cashier_mode(self):
        """ This function is the main part of the program, its the user friendly part where you can actually write in the products you want to add.
            It also contains error handeling, so you can not write in odd inputs."""
        print("You have now entered the cashier mode:")
        print("Just write out the productcodes you want to add and the quantity")
        print("To exit and get a receipt finish with (#)")
        self.cart = []
        while True:
            user_input = (input().split(" "))
            if user_input[0] == "#":
                    break
            if all(element.isdigit() for element in user_input):
                if user_input[0] in self.products:
                        if len(user_input) <=1:
                            print("Enter a valid amount")
                            continue
                        elif user_input[1] == '0':
                                print("Enter a valid amount")
                                continue
                                
                        elif int(user_input[1]) > self.products_amount[user_input[0]]:
                            print("The amount you typed in exceeds the amount in the datbase")
                            continue    
                            
                        if user_input[0] in self.products_price:
                            price = ((self.products_price[user_input[0]] * int(user_input[1])))
                            self.cart.append([self.products[user_input[0]],user_input[1],self.products_price[user_input[0]],price])
                else:
                    print("That item does not exist")
                    continue

            else:
                print("Invalid Input")
                
        print("This is the items in the basket")
        for item in self.cart:
            print(f"{item}\n")
    
            
        

    def edit_receipt(self):
        """This function enables the user to change the amount before the receipt prints out, this also enables the user to delete unasked products, it also checks if the amount 
        the user types in exceeds the amount in the database."""
        while True:
            end_question = input("Do you want to edit the cart? ").lower() 
            if end_question == "yes" and len(self.cart)>0:
                edit_line = (er.get_valid_input("Which line do you want to edit? ") -1)
                if 0 <= edit_line < len(self.cart):
                    print("The line you are edeting", self.cart[edit_line])
                    i, j = 0, 0
                    while j == 0:
                        if edit_line < len(self.cart) or edit_line > len(self.cart):
                            edit_question = input("What do you want to edit? ").lower()
                            if edit_question == "a":
                                while i == 0:
                                    new_amount = er.get_valid_input("Enter the new amount: ")
                                    self.cart[edit_line][1] = new_amount
                                    for key, value in self.products.items():
                                        if self.cart[edit_line][0] == value:
                                            if key in self.products_amount:
                                                if new_amount > self.products_amount[key]:
                                                    print("Remember that the new amount cant exceed the database amount!")
                                                    i = 0
                                        
                                                elif int(new_amount) == 0:
                                                        del self.cart[edit_line]
                                                        print("Line removed.")
                                                        i += 1
                                                        j += 1
                                                        break
                                                else:
                                                    new_price = (self.cart[edit_line][2] * int(new_amount))
                                                    self.cart[edit_line][3] = new_price
                                                    print("Edit successful")
                                                    print(self.cart[edit_line])
                                                    i += 1
                                                    j += 1
                                                    break
                            else:
                                print(f"Editing {edit_question} is not supported.")
                                j = 0
                        else:
                            print(f"You can not edit line {edit_line}. Try Again!")
                            j = 0
                else: 
                    print("Item not found, please try again")
                    
            elif end_question == "no":
                break
                
        print("Printing receipt.....")

    def write_out_receipt(self):
        """This function writes out the receipt to the file named receipt.csv"""
        
        with open("receipt.csv", "w", newline="",encoding="utf-8") as file:
            fields = ("Products","Amount","A-Price","Price")
            writer = csv.writer(file)
            writer.writerow(fields)
            writer.writerows(self.cart)
            
        df = pd.read_csv("receipt.csv")
        price_sum = df["Price"].sum()
        
        with open("receipt.csv", "a", newline="",encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Total: "+ "      "+ "    " + "    " + str(price_sum)])
            
            
def menu():
    """This function creates the menu which gives the user the opportunity to choose what they want to do"""
    print("-------------------------------")
    print("C Cashier mode")
    print("Q Quit")
    option = input("What do you want to do? ").upper()
    return option 

def main():
    """This is the main function which controlls all the other functions"""
    print("\n"+"         "+"Welcome")
    print("This is a cashier software")
    print("Please choose a option below")
    print("-------------------------------")
    database = Cashier()
    database.read_goods()
    cashier = database
    option = menu()
    
    while True != "Q":
        if option == "C":
            database.read_goods()
            cashier.cashier_mode()
            cashier.edit_receipt()
            cashier.write_out_receipt()
            break
        elif option == "Q":
            print("Bye!")
            quit()
        option =menu()
if __name__ == "__main__":
    main()
