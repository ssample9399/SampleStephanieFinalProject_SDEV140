"""
File: BoatTypeModule
Author: Stephanie Sample
Last Modified: 12/14/21
Purpose:

This program sets the Boat Type Module for the Boast Estimator Program 

"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import  *



class BoatTypeModule(EasyFrame):
    """ Module that sets up the Color Choices """

    def __init__(self):
        """Sets up the window and the labels."""
        self.boatType = 900
        
        EasyFrame.__init__(self, title = "Boat Type Selector")#,  width = 450, height = 450
        self.setResizable(True)               


        self.addLabel(text = "What type of boat do you have?", row = 1, column = 0, columnspan = 2)
        
#   ***** IMAGES *****   #

    #speedboat image
        
        imageLabel = self.addLabel(text = "Speed Boat", row = 3, column = 0, sticky = "NSEW")                   
        self.image1 = PhotoImage(file = "speed.gif")
        imageLabel["image"] = self.image1

    #pontoon image
        
        imageLabel = self.addLabel(text = "Pontoon", row = 3, column = 1, sticky = "NSEW")
        self.image2 = PhotoImage(file = "pontoon.gif")
        imageLabel["image"] = self.image2
        

    #fishing image
        
        imageLabel = self.addLabel(text = "Fishing Boat", row = 5, column = 0, sticky = "NSEW")
        self.image3 = PhotoImage(file = "fishing.gif")
        imageLabel["image"] = self.image3
                

    #cabin cuddy image
        
        imageLabel = self.addLabel(text = "Cabin Cuddy Boat", row = 5, column = 1, sticky = "NSEW")
        self.image4 = PhotoImage(file = "cabincuddy.gif")
        imageLabel["image"] = self.image4


        ##Creates the buttons for the user to select the boat type
        self.speedBtn = self.addButton(text = "Speed Boat", row = 2, column = 0, command = self.speed)
        self.pontoonBtn = self.addButton(text = "Pontoon", row = 2, column = 1, command = self.pontoon)
        self.fishingBtn = self.addButton(text = "Fishing Boat", row = 4, column = 0, command = self.fishing)
        self.cabinBtn = self.addButton(text = "Cabin Cuddy", row = 4, column = 1, command = self.cabin)
        #self.estBtn = self.addButton(text = "Get Estimate", row = 15, column = 0, columnspan = 2, command = self.estBt)
       


    #Sets the event handlers for the commands inside the buttons
    def speed(self):
        self.speedBtn["state"] = "normal"
        self.pontoonBtn["state"] = "disabled"
        self.fishingBtn["state"] = "disabled"
        self.cabinBtn["state"] = "disabled"
        self.boatType = 900
      
    def pontoon(self):
        self.speedBtn["state"] = "disabled"
        self.pontoonBtn["state"] = "normal"
        self.fishingBtn["state"] = "disabled"
        self.cabinBtn["state"] = "disabled"        
        self.boatType = 1000

    def fishing(self):
        self.speedBtn["state"] = "disabled"
        self.pontoonBtn["state"] = "disabled"
        self.fishingBtn["state"] = "normal"
        self.cabinBtn["state"] = "disabled"        
        self.boatType = 800

    def cabin(self):
        self.speedBtn["state"] = "disabled"
        self.pontoonBtn["state"] = "disabled"
        self.fishingBtn["state"] = "disabled"
        self.cabinBtn["state"] = "normal"        
        self.boatType = 1100
        
   
# Instantiates and pops up the window.
if __name__ == "__main__":
    BoatTypeModule().mainloop()
