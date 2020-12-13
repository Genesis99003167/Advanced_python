#!/usr/bin/env python
# coding: utf-8

# In[33]:



class cafe:
    def __init__(self,cust_name,no_of_people,table_no):
        self.cust_name = 2
        self.no_of_people = 3
        self.table_no = 4
    def customer(self):
        print("Enter name of the customer: ")
        self.cust_name = input()
        print("Enter no. of people: ")
        self.no_of_people = input()
        print("Enter the table no assigned: ")
        self.table_no = input()
    
        
class menu:
    def sweetcornsoup(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*(120)
        return self.cost
    def garlicbread(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*120
        return self.cost
    def paneerpizza(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*220
        return self.cost
    def paneer65(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*150
        return self.cost
    def paneertikka(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*200
        return self.cost
    def honeychillypotato(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*100
        return self.cost
    def babycornfry(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*150
        return self.cost
    def crispycorn(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*120
        return self.cost
    def alootikki(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*150
        return self.cost
    def manchurian(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*150
        return self.cost
    def frenchfries(self):
        print("Enter the quantity: ")
        self.quan=int(input())
        self.cost=(self.quan)*100
        return self.cost

class selection(menu):
    def __init__(self,option,price):
        self.option=option
        self.price=0
    
    def choose(self):
        print("WELCOME TO GRNADSHIBA/n")
        
        print("1. sweetcornsoup")
        print("2. garlicbread")
        print("3. paneerpizza")
        print("4. paneer65")
        print("5. paneertikka")
        print("6. honeychillypotato")
        print("7. babycornfry")
        print("8. crispycorn")
        print("9. alootikki")
        print("10. manchurian")
        print("11. frenchfries")
        
  
        
        while True:
            try:
                option=int(input("select the food item: "))
                
            except:
                print("invaalid")
            if(option==1):
                self.price += obj1.sweetcornsoup()

            elif(option==2):
                self.price = self.price + obj1.garlicbread()

            elif(option==3):
                self.price = self.price + obj1.paneerpizza()

            elif(option==4):
                self.price = self.price + obj1.paneer65()
            elif(option==5):
                self.price = self.price + obj1.paneertikka()
            elif(option==6):
                self.price = self.price + obj1.honeychillypotato()
            elif(option==7):
                self.price = self.price + obj1.babycornfry()
            elif(option==8):
                self.price = self.price + obj1.crispycorn()

            elif(option==9):
                self.price = self.price + obj1.alootikki()
            elif(option==10):
                self.price = self.price + obj1.manchurian()
            elif(option==11):
                self.price = self.price + obj1.frenchfries()
            else:
                #print("invalid")
                break
        print("The total price is:",self.price)
        


obj1=menu()
obj2=cafe("","","")
obj2.customer()
obj=selection("","")
obj.choose()


  


# # 
