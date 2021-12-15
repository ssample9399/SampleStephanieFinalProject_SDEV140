"""
Program: coverTypeMath
Author: Stephanie Sample
Date Modified: 12/12/21
Purpose: The module that the sets the ct variable needed in the Boat Estimate Program 
"""

#Greetings & inputs
print()
print("Please Select a Cover Type from the list below:")
print("Enter [1] for Road/Travel Cover\nEnter [2] for Snap-On Cover;\nEnter [3] for Mooring Set")

coverType = input("Cover Type? ")
print()
ct = 0 #sets the initial ct variable to 0
#if statement to set ct variable for calucation
if coverType == "1":
    ct = 75
    print("A Road Cover adds an additional $", + ct)
if coverType == "2":
    ct = 100
    print("A Snap-On Cover adds an additional $", ct)
if coverType == "3":
    ct = 50
    print("A Mooring Set adds an additional $", ct)
#else:
#    print("Valid choices are: [1] [2] [3]")
    

