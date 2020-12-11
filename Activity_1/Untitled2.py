#!/usr/bin/env python
# coding: utf-8

# In[4]:


class appetisers():
    def __init__(self,name,price):                      # Defining price and name in the menu
        self.name=name
        self.price = price
    def getprice(self):                                 # Return price
        return self.price
    def __str__(self):
        return self.name + ':'+str(self.getprice())
   
    #file handling
class ip_op_file:
    def file_read(self):
        fr=open('inputfile.txt','r')                    #Reading input file line by line
        for line in fr:
            print(line)
        fr.close()  
def main():                                            # Welcome to restaurant
    print("WELCOME TO CAFE")
    obj=ip_op_file()                                   # Creating object
    obj.file_read()                                    # Reading input file
    output = open('outputfile.txt','a')
    item_food = int(input("Please enter the number of food items.\n"))
    item_list = [str(input("What is the item #" + str(count + 1) + " on your list?\n")) for count in range(item_food)]
    '''for i in range(item_food):
        x[i]=int(input("Enter the price of the food item \n"))
        item_prize=item_prize+x[i]'''
    item_price = sum(int(input("Enter the price of the food item \n")) for i in range(item_food))  # Input price of the ordered items
    item_quan = (sum(int(input("What is the quantity of food item #" + str(count + 1) + " that you ordered?\n")) for count in range(item_food)))/(item_food) #Enter the quantity of food items
    subtotal = (sum(int(item_price * item_quan)for i in range(item_food)))/(item_food)             # Totalling the food items
    print ("The subtotal is...")
    print (subtotal)
    tax = 0.07 * item_quan                                                                         # Tax is added 
    total = subtotal + tax                                                                         #Totalling after adding tax
    print ("The grand total is...")
    print (total)
    total1 = str(total)
    output.write("The grand total is...")                                                          
    output.write(total1)                                                                          # Total is written in output file 
    output.close()
    
main()


# ## 

# ## 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




