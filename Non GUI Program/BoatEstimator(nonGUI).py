from breezypythongui import EasyFrame
from tkinter import  *
from boatTypeMath import labor
from coverTypeMath import ct
from boatLengthMath import blcost


totalCost = labor + blcost + ct
print()
print("The estimate for your custom cover is $", + totalCost)


