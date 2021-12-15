"""
Program: boatTypeMath
Author: Stephanie Sample
Date Modified: 12/12/21
Purpose: The module that the sets the labor variable needed in the
Boat Estimate Program 

"""
labor = 0 #sets the initial labor variable to 0

#Greetings & inputs
print()
print("Please select a Boat Type from the following list:")
print("Enter [s] for Speed Boat\nEnter [p] for Pontoon\nEnter [f] for Fishing Boat\nEnter [c] for Cabin Cuddy")

boatType = str(input("Boat Type: "))#gets user input and stores it in the boatType variable
print()
#if statements to set labor variable for later calucation
if boatType == "s":
    labor = 900
    print("Covers for a Speed Boat start at $", + labor)
if boatType == "p":
    labor = 1000
    print("Covers for a Pontoon start at $", + labor)
if boatType == "f":
    labor = 800
    print("Covers for a Fishing Boat start at $", + labor)
if boatType == "c":
    labor = 1100
    print("Covers for a Cabin Cuddy start at $", + labor)
