import runpy

from pkg_resources import run_script

#Problem number 1

def greeting():
    xname = input ('What is your name? ')
    from datetime import date
    today = date.today()
    return f"Hello {xname}! Thank you for being here! The date today is {today}"

#---------------------------------------------------------------------------------------
#function number 2
# 2 numbers are inputted and added together

def addtwo():
    one = input ('What is the first number would you like to add? ')
    two = input ('What is the second number you would like to add? ')
    first = int(one)
    second = int(two)
    Out = first + second
    return (f"The results of {one}+{two} is {Out}")
#----------------------------------------------------------
#function #3
# a number is inputted and then 1 is added to the number.
def nextnumber():
    number = input ("Input a number: ")
    num = int(number)
    final = num + 1
    return (f"You inputted {num}. The result of {num} + 1 is {final}")

#---------------------------------------------------------------
#function #4
# converts minutes to seconds
def minsec():
    x = input ('Convert minutes to seconds. Input any integer: ')
    y = int(x)
    sec = y * 60
    return (f"{x} minutes is equivelent to {sec} seconds.")
#---------------------------------------------------------------
#function #5
#calculates amount of days since birth
def alivefor():
    from datetime import date
    today = date.today()
    byear = input ("What year were you born? ")
    bmonth = input ("What month were you born? Please enter the number of the month. ")
    bday = input ("What day were you born? ")
    intbday = int(bday)
    intbyear = int(byear)
    intbmonth = int(bmonth)
    birth = date(intbyear, intbmonth, intbday)
    alive = today - birth
    return (f"You have been alive for {alive.days} days.")
#-----------------------------------------------------------------
#Function #6
#Write a function to get a string made of the first 2 and the last 2 characters from a given string
#If the string is less than 2 return instead of the empty string
def stringchange():
    unnamed = input('Enter a string to get the first two and last two letters of it. ')
    if len(unnamed) > 2:
        exname = unnamed[0:2]
        exyname = unnamed[-2:]
        fullname = exname + exyname
        return(fullname)
    elif len(unnamed) == 2:
        double = unnamed + unnamed
        return(double)
    elif len(unnamed) <= 1:
        return unnamed
#---------------------------------------------------------------------------------------
#function #7
#Write a python function to get a single string from 2 given strings, seperated by a space and swap the first
#two characters of each string
def replacestring():
    stringone = input ("Please input the first string. ")
    stringtwo = input ("Please input the second string. ")
    newstring = stringtwo[0:2] + stringone[2:]
    newerstring = stringone[0:2] + stringtwo[2:]
    neweststring = newstring + ' ' + newerstring
    return neweststring
#----------------------------------------------------------------------------------------
#function #8 
#Write a function that prints the lengt of a string that is passed to it then folds the string until its all reversed
def reversestring():
    firststring = input("What string would you like reversed? ")
    stringlength = len(firststring)
#make a loop
    
    









#menu time
print("------------------------Python Menu of Menus------------------------")
print("1. Standard greeting code, with date and time.")
print("2. Adds two entered integers together.")
print("3. Adds one to the entered integer.")
print("4. Converts entered amount of minutes to seconds.")
print("5. Calculates how many days a person has been alive based off inputted birth date.")
print("6. Returns the first and last two letters of a given string unless the string is 1-2 letters long.")
print("7. Takes two given strings and swaps the first two letters of each string with each other.")
response = input("What program would you like to run? Press Q to quit. ")
if (response == "q"):
    print("Exiting program.")
    exit()
elif (response == "1"):
    print (greeting())
elif (response == "2"):
    print (addtwo())
elif (response == "3"):
    print(nextnumber())
elif (response == "4"):
    print(minsec())
elif (response == "5"):
    print(alivefor())
elif (response == "6"):
    print(stringchange())
elif (response == "7"):
    print(replacestring())
else:   
    runpy.run_path("g:\My Drive\Class Digital Notebooks\CNS1\Programming\Python Scripts\CNS Problems.py")