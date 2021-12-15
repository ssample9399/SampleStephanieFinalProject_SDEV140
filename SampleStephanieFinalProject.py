"""
Program: Custom Cover Estimator for Boats
Author: Stephanie Sample
Last Modified: 12/15/21
Purpose:

To allow users to select different choices and receive a quote back.

"""


from breezypythongui import EasyFrame
from tkinter import  *
import math


class BoatEstimator(EasyFrame): #Sets up the module as a class

    def __init__(self): #Sets up the window and the labels
        EasyFrame.__init__(self, title = "Boat Cover Estimator")
        self.setResizable(True)
        self.cc = "" #initializes the cc variable
        self.bt = "" #initializes the bt variable
        self.ct = "" #initializes the ct variable
        self.bl = "" #initializes the bl variable
        self.subTotal = 0 #initializes the sub total variable
        self.taxRate = 0.08 #initializes the tax rate variable
        self.finalTotal = 0 #initializes the final total variable

# ****** Labels and fields for the user inputs ************************************
        self.addLabel(text = "Welcome! Please enter the follwing fields below to get a boat cover estimate ", row = 0, column = 0, columnspan = 4)#Label for Boat Length input instructions
        self.addLabel(text = "We need to know boat length, boat type, and the type & type of the cover you want.", row = 1, column = 0, columnspan = 4)#Label for Boat Length input instructions

        
        #Boat Length data 
        self.addLabel(text = "Please Enter BOAT LENGTH Between 5ft & 32ft, rounding up to nearest whole number.", row = 2, column = 0, columnspan = 4)#Label for Boat Length input instructions
        self.addLabel(text = "Length in whole #", row = 3, column = 0, columnspan = 3)#Label for Boat Length
        self.boatLengthInputField = self.addIntegerField(value = 0, row = 4, column = 0, width = 10)#Input field for Boat Length
        self.addLabel(text = "___________________________________________________________________________________", row = 5, column = 0, columnspan = 4)#Label for Boat Length

        #Boat Type data
        self.addLabel(text = "Please Select a BOAT TYPE", row = 6, column = 0, columnspan = 3)#Instruction Label for Boat Type
        self.addLabel(text = "Enter [ 1 ] for Speed Boat,[ 2 ] for Pontoon, [ 3 ] for Fishing Boat, [ 4 ] for Cabin Cuddy", row = 7, column = 0, columnspan = 4)#Instruction Label for Boat Type
        self.addLabel(text = "Boat Type", row = 8, column = 0)#Label for Boat Type
        self.boatTypeInputField = self.addIntegerField(value = 0, row = 9, column = 0, width = 10)#Input field for Boat type
        self.addLabel(text = "___________________________________________________________________________________", row = 10, column = 0, columnspan = 4)#Label for Boat Length

        #Cover Type data
        self.addLabel(text = "Please Select a COVER TYPE", row = 11, column = 0, columnspan = 3)#Instruction Label for cover type
        self.addLabel(text = "Enter [1] for Road/Travel Cover, [2] for Snap-On Cover, [3] for Mooring Set", row = 12, column = 0, columnspan = 4)#Instruction Label for cover type
        self.addLabel(text = "Cover Type", row = 13, column = 0)#Label for Cover Type
        self.coverTypeInputField = self.addIntegerField(value = 0, row = 14, column = 0, width = 10)#Input field for cover type
        self.addLabel(text = "___________________________________________________________________________________", row = 15, column = 0, columnspan = 4)#Label for Boat Length

        #Color Choice data
        self.addLabel(text = "Please Select a COVER COLOR", row = 16, column = 0, columnspan = 3)#Instruction Label for cover color
        self.addLabel(text = "Color Choice", row = 17, column = 0)#Label for Color Choice
        self.colorChoiceInputField = self.addIntegerField(value = 0, row = 18, column = 0, width = 10)#Input field for cover color

        textLabel = self.addLabel(text = "[ 1 ]",row = 19, column = 0,sticky = "NSEW")
        imageLabel = self.addLabel(text = "[1] White", row = 20, column = 0, sticky = "NSEW")                   
        self.image1 = PhotoImage(file = "white.gif")
        imageLabel["image"] = self.image1

        textLabel = self.addLabel(text = "[ 2 ]",row = 19, column = 1,sticky = "NSEW")
        imageLabel = self.addLabel(text = "[2] Black", row = 20, column = 1, sticky = "NSEW")                   
        self.image2 = PhotoImage(file = "black.gif")
        imageLabel["image"] = self.image2

        textLabel = self.addLabel(text = "[ 3 ]",row = 19, column = 2,sticky = "NSEW")
        imageLabel = self.addLabel(text = "[3] Tan", row = 20, column = 2, sticky = "NSEW")                   
        self.image3 = PhotoImage(file = "tan.gif")
        imageLabel["image"] = self.image3

        textLabel = self.addLabel(text = "[ 4 ]",row = 19, column = 3,sticky = "NSEW")
        imageLabel = self.addLabel(text = "[4] Gray", row = 20, column = 3, sticky = "NSEW")                   
        self.image4 = PhotoImage(file = "gray.gif")
        imageLabel["image"] = self.image4

        self.addLabel(text = "___________________________________________________________________________________", row = 21, column = 0, columnspan = 4)#Label for Boat Length
        self.addLabel(text = "-----------------------------------------------------------------------------------", row = 22, column = 0, columnspan = 4)#Label for Boat Length

        #Labels to show the running subtotal
        self.addLabel(text = "Subtotal", row = 23, column = 0)
        self.subTotalLabel = self.addLabel(text = "0", row = 23, column = 1)
        
            
        # The command buttons
        self.button1 = self.addButton(text = "Add to quote", row = 4, column = 1, columnspan = 1, command = self.addBoatLengthEstimate)#boat length entry
        self.button2 = self.addButton(text = "Add to quote", row = 9, column = 1, columnspan = 1, command = self.addBoatTypeEstimate)#boat type entry
        self.button3 = self.addButton(text = "Add to quote", row = 14, column = 1, columnspan = 1, command = self.addCoverTypeEstimate)#cover type entry
        self.button4 = self.addButton(text = "Add to quote", row = 18, column = 1, columnspan = 1, command = self.addColorChoiceEstimate)#color choice entry
        self.addButton(text = "Get Quote", row = 24, column = 3, columnspan = 1, command = self.displayQuote)#Button that initiates pop-up window with final estimate info.
        

# ****** Event handling for the buttons ************************************
        

    def addBoatLengthEstimate(self):#boat length actions
        
        number = self.boatLengthInputField.getNumber()  
            
        if 5 <= number <= 18:
            self.subTotal = self.subTotal + 180
            self.bl = "5 to 18 ft"   
            
        if 18 < number <= 20:
            self.subTotal = self.subTotal + 200
            self.bl = "19 to 20 ft"


        if 20 < number <= 22:
            self.subTotal = self.subTotal + 220
            self.bl = "21 to 22 ft"
            

        if 22 < number <= 24:
            self.subTotal = self.subTotal + 240
            self.bl = "23 to 24 ft"
            

        if 24 < number <= 26:
            self.subTotal = self.subTotal + 260
            self.bl = "25 to 26 ft"
            

        if 26 < number <= 32:
            self.subTotal = self.subTotal + 300
            self.bl = "27 to 32 ft"
            
        
        self.subTotalLabel.config(text=str(self.subTotal))
        self.button1["state"] = "disabled"

                
    def addBoatTypeEstimate(self):#boat type actions
        
        number = self.boatTypeInputField.getNumber()  
        
        if number == 1:
            self.subTotal = self.subTotal + 900
            self.bt = "Speed Boat"
            
        if number == 2:
            self.subTotal = self.subTotal + 1000
            self.bt = "Pontoon"
            
        if number == 3:
            self.subTotal = self.subTotal + 800
            self.bt = "Fishing Boat"

        if number == 4:
            self.subTotal = self.subTotal + 1100
            self.bt = "Cabin Cuddy"
            
        
        self.subTotalLabel.config(text=str(self.subTotal))
        self.button2["state"] = "disabled"
        
    def addCoverTypeEstimate(self):#cover type actions
        
        number = self.coverTypeInputField.getNumber()  
        
        if number == 1:
            self.subTotal = self.subTotal + 75
            self.ct = "Road/Travel Cover" 
            
        if number == 2:
            self.subTotal = self.subTotal + 100
            self.ct = "Snap-On Cover" 
            
            
        if number == 3:
            self.subTotal = self.subTotal + 50
            self.ct = "Mooring Set" 
            
        
        self.subTotalLabel.config(text=str(self.subTotal))
        self.button3["state"] = "disabled"
        
    def addColorChoiceEstimate(self):#color choice actions
        number = self.colorChoiceInputField.getNumber()  
        
        if number == 1:
            self.subTotal = self.subTotal + 10
            self.cc = "white"
            
        if number == 2:
            self.subTotal = self.subTotal + 10
            self.cc = "black"
            
        if number == 3:
            self.subTotal = self.subTotal + 15
            self.cc = "tan"

        if number == 4:
            self.subTotal = self.subTotal + 15
            self.cc = "gray"
            

        self.subTotalLabel.config(text=str(self.subTotal))
        self.button4["state"] = "disabled"


    def displayQuote(self):#quote to message box actions
        message = "A " + self.cc + " " + self.ct + " for a " + self.bl + " " + self.bt +"\n"   
        message += "Your subtotal is $: " + str(self.subTotal) + "\n" #Displays the running subtotal
        message += "Tax Rate: 8%" + "\n" # Displays the tax rate
        self.finalTotal = (self.subTotal * self.taxRate) + self.subTotal #calculates the final total
        message += "The Total Estimate Is: $" + str(self.finalTotal) +"\n" #Displays the final total
        message += "Please close the message box and restart the program for a new quote."
        
        self.messageBox(title = "Custom Estimate", message = message) #creates the pop-up window
    
# Instantiates and pops up the window.
if __name__ == "__main__":
    BoatEstimator().mainloop()


 


