#Nikolei Advani, 9/23/16
import math

def printInstructions():
    '''This function prints the instructions to the user'''
    print("This program will solve the quadratic formula for you. You will be prompted to give the values of a, b, and c.")

def getFirstCoefficient():
    '''This function prompts the user for the value of a'''
    a = float(input("what is the value of a?"))
    return a

def getSecondCoefficient():
    '''This function prompts the user for the value of b'''
    b = float(input("what is the value of b?"))
    return b

def getThirdCoefficient():
    '''This function prompts the user for the value of c'''
    c = float(input("what is the value of c?"))
    return c

def calculateRoots(a, b, c):
    '''This function plugs a, b, and c into the quadratic equation and solves it'''
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    print(x1, x2)

def main():
    '''This function calls all the other functions'''
    printInstructions()
    a = getFirstCoefficient()
    b = getSecondCoefficient()
    c = getThirdCoefficient()
    calculateRoots(a, b, c)
#Program runs.
main()





