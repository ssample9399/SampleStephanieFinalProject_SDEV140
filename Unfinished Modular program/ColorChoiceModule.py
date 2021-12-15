"""
File: ColorChoiceModule
Author:Stephanie Sample
Last Modified: 12/14/21
Purpose:

This program sets up the Color Choice Module for the Boast Estimator Program 


"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import  *


class ColorChoiceModule(EasyFrame):
    """ Module that sets up the Color Choices"""

    def __init__(self):
        """Sets up the window and the labels."""
        colorpick = ""
        EasyFrame.__init__(self, title = "Boat Cover Estimator")#width = 450, height = 450
        self.setResizable(True)               


      
        self.addLabel(text = "What color would you like?", row = 0, column = 0, columnspan = 2)

        #Creates the buttons for the user to select the canvas color
        self.tanBtn = self.addButton(text = "Tan Canvas", row = 1, column = 0, command = self.tan)
        self.grayBtn = self.addButton(text = "Gray Canvas", row = 1, column = 1, command = self.gray)
        self.blackBtn = self.addButton(text = "Black Canvas", row = 2, column = 0, command = self.black)
        self.whiteBtn = self.addButton(text = "White Canvas", row = 2, column = 1, command = self.white)
        

    #Sets the event handlers for the commands inside the buttons
    def tan(self):
        self.tanBtn["state"] = "normal"
        self.grayBtn["state"] = "disabled"
        self.blackBtn["state"] = "disabled"
        self.whiteBtn["state"] = "disabled"
        self.colorpick = "Tan"
      
            
    def gray(self):
        self.tanBtn["state"] = "disabled"
        self.grayBtn["state"] = "normal"
        self.blackBtn["state"] = "disabled"
        self.whiteBtn["state"] = "disabled"
        self.colorpick = "Gray"

  
    def black(self):
        self.tanBtn["state"] = "disabled"
        self.grayBtn["state"] = "disabled"
        self.blackBtn["state"] = "normal"
        self.whiteBtn["state"] = "disabled"
        self.colorpick = "Black"

    
    def white(self):
        self.tanBtn["state"] = "disabled"
        self.grayBtn["state"] = "disabled"
        self.blackBtn["state"] = "disabled"
        self.whiteBtn["state"] = "normal"
        self.colorpick = "White"

  
# Instantiates and pops up the window.
if __name__ == "__main__":
    ColorChoiceModule().mainloop()  
