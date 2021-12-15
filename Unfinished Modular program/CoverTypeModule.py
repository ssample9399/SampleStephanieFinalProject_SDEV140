"""
File: CoverTypeModule
Author: Stephanie Sample
Last Modified: 12/14/21
Purpose:

"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font
from tkinter import  *



class CoverTypeModule(EasyFrame):
    def __init__ (self):
        self.coverType = 50

        EasyFrame.__init__(self, title = "Boat Cover Estimator", width = 450, height = 450)
        self.setResizable(True)

        self.addLabel(text = "What kind of cover do you need? (Select 1)", row = 6, column = 0, columnspan = 2)


        self.roadCoverCB = self.addCheckbutton(text = "Road/Travel Cover", row = 7, column = 0, columnspan = 2, command = self.rc)

        self.snapCoverCB = self.addCheckbutton(text = "Snap-on Cover", row = 8, column = 0, columnspan = 2, command = self.sc)

        self.mooringSetCB = self.addCheckbutton(text = "Mooring Set", row = 9, column = 0, columnspan = 2, command = self.ms)

    def rc(self):
        self.coverType = 75
        self.snapCoverCB["state"] = "disabled"
        self.mooringSetCB["state"] = "disabled"
        self.roadCoverCB["state"] = "normal"        

        
    def sc(self):
        self.coverType = 100
        self.snapCoverCB["state"] = "normal"
        self.mooringSetCB["state"] = "disabled"
        self.roadCoverCB["state"] = "disabled"  
        
    def ms(self):
        self.coverType = 50
        self.snapCoverCB["state"] = "disabled"
        self.mooringSetCB["state"] = "normal"
        self.roadCoverCB["state"] = "disabled"  
        
    
# Instantiates and pops up the window.
if __name__ == "__main__":
    CoverTypeModule().mainloop()        
