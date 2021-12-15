"""
Program: boatLenghtMath
Author: Stephanie Sample
Date Modified: 12/12/21
Purpose: The module that the sets the blcost variable needed in the Boat Estimate Program 
"""

blcost=0
print()
print("Please enter Boat Length, rounding up to next whole number in feet.")
bl = int(input("Boat Length? "))
print()
if bl == str(""):
    print("Please enter a valid number greater than 5")

if bl <5:
    print("Please enter a number greater than 5")

if bl >= 5 and bl <= 18:
    blcost = int(180)
    print("A", + bl, "ft boat adds an additional $", + blcost)
    
if bl > 18 and bl <= 20:
    blcost = int(200)
    print("A", + bl, "ft boat adds an additional $", + blcost)

if bl > 20 and bl <= 22:
    blcost = int(220)
    print("A", + bl, "ft boat adds an additional $", + blcost)

if bl >22 and bl <= 24:
    blcost = int(240)
    print("A", + bl, "ft boat adds an additional $", + blcost)

if bl > 24 and bl <= 26:
    blcost = int(260)
    print("A", + bl, "ft boat adds an additional $", + blcost)

if bl > 26 and bl <= 32:
    blcost = int(300)
    print("A", + bl, "ft boat adds an additional $", + blcost)

if bl > 32:
    print("Please call for estimate")

