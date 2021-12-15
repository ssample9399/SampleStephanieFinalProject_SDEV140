"""
File: BoatLengthModule
Author: Stephanie Sample
Last Modified: 12/14/21
Purpose:

This program sets up the Boat Lenght Module for the Boast Estimator Program

"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import  *


class BoatLengthModule(EasyFrame):
    """ Module that sets up the Boat Length Choices """

    def __init__(self):
        """Sets up the window and the labels."""
        
        self.blcost = 180
        EasyFrame.__init__(self, title = "Boat Length Estimator")
        self.setResizable(True)

        self.addLabel(text = "What is the boat length? (Select 1)", row = 0, column = 0, columnspan = 2)

        #Creates the checkboxes for user to select boat length
        self.group1CB = self.addCheckbutton(text = "5 ft to 18 ft", row = 1, column = 0, command = self.g1)#columnspan = 2, 
        self.group2CB = self.addCheckbutton(text = "18.1 ft to 20 ft", row = 1, column = 1, command = self.g2)#columnspan = 2, 
        self.group3CB = self.addCheckbutton(text = "20.1 ft to 22 ft", row = 2, column = 0, command = self.g3)#columnspan = 2,         
        self.group4CB = self.addCheckbutton(text = "22.1 ft to 24 ft", row = 2, column = 1, command = self.g4)#columnspan = 2, 
        self.group5CB = self.addCheckbutton(text = "24.1 ft to 26 ft", row = 3, column = 0, command = self.g5)#columnspan = 2, 
        self.group6CB = self.addCheckbutton(text = "26.1 ft to 32 ft", row = 3, column = 1, command = self.g6)#columnspan = 2,

    #Sets the event handlers for the commands inside the buttons
    def g1(self):
        self.blCost = 180
        self.group1CB["state"] = "normal"
        self.group2CB["state"] = "disabled"
        self.group3CB["state"] = "disabled"
        self.group4CB["state"] = "disabled"
        self.group5CB["state"] = "disabled"
        self.group6CB["state"] = "disabled" 

        
    def g2(self):
        self.blCost = 220
        self.group1CB["state"] = "disabled"
        self.group2CB["state"] = "normal"
        self.group3CB["state"] = "disabled"
        self.group4CB["state"] = "disabled"
        self.group5CB["state"] = "disabled"
        self.group6CB["state"] = "disabled" 
        
    def g3(self):
        self.blCost = 240
        self.group1CB["state"] = "disabled"
        self.group2CB["state"] = "disabled"
        self.group3CB["state"] = "normal"
        self.group4CB["state"] = "disabled"
        self.group5CB["state"] = "disabled"
        self.group6CB["state"] = "disabled" 

    def g4(self):
        self.blCost = 260
        self.group1CB["state"] = "disabled"
        self.group2CB["state"] = "disabled"
        self.group3CB["state"] = "disabled"
        self.group4CB["state"] = "normal"
        self.group5CB["state"] = "disabled"
        self.group6CB["state"] = "disabled" 

    def g5(self):
        self.blCost = 280
        self.group1CB["state"] = "disabled"
        self.group2CB["state"] = "disabled"
        self.group3CB["state"] = "disabled"
        self.group4CB["state"] = "disabled"
        self.group5CB["state"] = "normal"
        self.group6CB["state"] = "disabled" 

    def g6(self):
        self.blCost = 300
        self.group1CB["state"] = "disabled"
        self.group2CB["state"] = "disabled"
        self.group3CB["state"] = "disabled"
        self.group4CB["state"] = "disabled"
        self.group5CB["state"] = "disabled"
        self.group6CB["state"] = "normal"        

   
# Instantiates and pops up the window.
if __name__ == "__main__":
    BoatLengthModule().mainloop()
        
