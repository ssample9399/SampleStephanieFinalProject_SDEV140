"""
File: layoutdemo.py
Author: Stephanie Sample
Last Modified: 12/13/21
Purpose:




"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import  *
import math

class BoatEstimator(EasyFrame):
    """ WHAT DOES THIS PROGRAM DO? """

    def __init__(self):
        """Sets up the window and the labels."""
        
        EasyFrame.__init__(self, title = "Boat Cover Estimator",  width = 500, height = 700)
        self.setResizable(True)               


#'''********** BOAT LENGTH INPUT   **********'''
        def boat_Length():
            self.addLabel(text = "Please enter length of boat, rounded up to the nearest foot: ", row = 0, column = 0, columnspan = 2)
            self.inputField = self.addIntegerField(value = 0, row = 0, column = 1, width = 10)

            #boat length(bl) determines raw material cost
            #if bl is < 18
                #blcost = int(180)
            #if bl is > 18 but <= 20
                #blcost = int(200)
            #if bl is > 20 but <= 22
                #blcost = int(220)
            #if bl is > 22 but <= 24
                #blcost = int(240)
            #if bl is > 24 but <= 26
                #blcost = int(260)
            #if bl is > 26
                #blcost = int(280)

#'''********** BOAT TYPE SELECTIONS   **********'''
            

#Get Boat Type
        def boat_Type():
            self.addLabel(text = "What type of boat do you have?", row = 1, column = 0, columnspan = 2)
        

        #speedboat image
            self.addButton1(text = "Speed Boat", row = 2, column = 0)#, command = self.boatType DO I NEED A COMMAND HERE?
            
            imageLabel = self.addLabel(text = "Speed Boat", row = 3, column = 0, sticky = "NSEW")                   
            self.image1 = PhotoImage(file = "speed.gif")
            imageLabel["image"] = self.image1

        #pontoon image
            self.addButton2(text = "Pontoon", row = 2, column = 1)#, command = self.boatType DO I NEED A COMMAND HERE?
            
            imageLabel = self.addLabel(text = "Pontoon", row = 3, column = 1, sticky = "NSEW")
            self.image2 = PhotoImage(file = "pontoon.gif")
            imageLabel["image"] = self.image2
            

        #fishing image
            self.addButton3(text = "Fishing Boat", row = 4, column = 0)#, command = self.boatType DO I NEED A COMMAND HERE?
            
            imageLabel = self.addLabel(text = "Fishing Boat", row = 5, column = 0, sticky = "NSEW")
            self.image3 = PhotoImage(file = "fishing.gif")
            imageLabel["image"] = self.image3
                    

        #cabin cuddy image
            self.addButton4(text = "Cabin Cuddy", row = 4, column = 1)#, command = self.boatType DO I NEED A COMMAND HERE? 
            
            imageLabel = self.addLabel(text = "Cabin Cuddy Boat", row = 5, column = 1, sticky = "NSEW")
            self.image4 = PhotoImage(file = "cabincuddy.gif")
            imageLabel["image"] = self.image4

        #def labor_hours()
        #labor is estimated based:
            # on the type of boat selected @50 hr shop rate * job hours
                #if Speed Boat:
                    #then labor = int(600)
                #if Pontoon:
                    #then labor = int(700)
                #if Fishing Boat:
                    #then labor = int(500)
                # if Cabin Cuddy:
                    #then labor = int(800)

          
                
#'''********** COVER TYPE SELECTIONS   **********'''
            
            
        def cover_type():
            self.addLabel(text = "What kind of cover do you need? (Select 1)", row = 6, column = 0, columnspan = 2)
            
            # Adds four check buttons
            self.roadCoverCB = self.addCheckbutton(text = "Road/Travel Cover", row = 7, column = 0, columnspan = 2)
            self.snapCoverCB = self.addCheckbutton(text = "Snap-on Cover", row = 8, column = 0, columnspan = 2)
            self.mooringSetCB = self.addCheckbutton(text = "Mooring Set", row = 9, column = 0, columnspan = 2)

                #if roadCoverCB:
                    #then cover_Type = int(75)
                #if snapCoverCB:
                    #then cover_Type = int(100)
                #if mooringSetCB:
                    #then cover_Type = int(0)


#********** COLOR SELECTIONS   **********
#COLOR SELECTIONS does not need calculated, only for displaying to customer
        def color_Choice():           
        
            self.addLabel(text = "What color would you like?", row = 10, column = 0, columnspan = 2)

        #Tan Swatch
            self.addButton(text = "Tan Canvas", row = 11, column = 0)
            imageLabel = self.addLabel(text = "Tan Material", row = 12, column = 0, sticky = "NSEW")                    
            self.image5 = PhotoImage(file = "tan.gif")
            imageLabel["image"] = self.image5
            

        #Gray Swatch
            self.addButton(text = "Gray Canvas", row = 11, column = 1)
            imageLabel = self.addLabel(text = "Gray Material", row = 12, column = 1, sticky = "NSEW")
            self.image6 = PhotoImage(file = "gray.gif")
            imageLabel["image"] = self.image6


        #Black Swatch
            self.addButton(text = "Black Canvas", row = 13, column = 0)
            imageLabel = self.addLabel(text = "Black Material", row = 14, column = 0, sticky = "NSEW")
            self.image7 = PhotoImage(file = "black.gif")
            imageLabel["image"] = self.image7
            

        #White Swatch
            self.addButton(text = "White Canvas", row = 13, column = 1)
            imageLabel = self.addLabel(text = "White Material", row = 14, column = 1, sticky = "NSEW")
            self.image8 = PhotoImage(file = "white.gif")
            imageLabel["image"] = self.image8


#Calculations  ***********************
            

        #def estimted_cost()
            #cost is estimated by:
                #labor hours + cover type + boat length
                #for example a road cover for an 18 to 20 ft speed boat = 600 (labor) + 200 (length) + 75 (cover type)
                    # total of $875



        # The command button
        self.addButton(text = "Get Est", row = 15, column = 0,
                       columnspan = 2, command = self.computeEst)

    # The event handling method for the button
    def computeEst(self):
        """Inputs the integer, computes the square root,
        and outputs the result."""
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)

   
# Instantiates and pops up the window.
if __name__ == "__main__":
    BoatEstimator().mainloop()

''' 
#May need to place "Get Est" button at end of program
        self.addButton(text = "Get Estimate", row = 15, column = 0,
                       columnspan = 2, command = self.placeOrder)

     
    # Event handler method

    def placeOrder(self): #may need to rename "placeOrder"
        """Display a message box with the order information."""
        message = ""
        if self.roadCoverCB.isChecked():
            message += "Road/Travel Cover\n\n"
        if self.snapCoverCB.isChecked():
            message += "Snap-on Cover\n\n"
        if self.mooringSetCB.isChecked():
            message += "Mooring Set\n"
        if message == "": message = "No product selected!"
        self.messageBox(title = "Estimate", message = message)



       

'''
    
