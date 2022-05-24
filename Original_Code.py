#Tyler Goodwin
#CNS1, Original Python Code
#The code will be a menu that allows me to open applications I use everyday
#The code is being built so I can get around my home computer easier.
#The code will be able to open and close applications, possibly input an application name and it will open/close it
#-----------------------------------------------------------------------------------
import os
from tracemalloc import start
from unittest.mock import call
import subprocess
import webbrowser
chrome_path = "C:\QuickNeed\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
#os.system('notepad.exe')   
def opendrive():
    subprocess.call("C:\Program Files\Google\Drive File Stream\launch.bat")    
#def opengeforce():
    #subprocess.call("C:")
print("Hello, welcome to the PC!")
print("I'm still a work in progress so have patience.")
print("My creator has big plans for me.")
def menuopen():
    x = input("What would you like to open? ")
    if (x == "q"):
        print("Exiting Program...")
        exit()
    elif (x == "chrome"):
        print("Opening Chrome...")
        webbrowser.get('chrome').open_new_tab("chrome://newtab/")
    #except():
        #print("Unrecognized response, Please re enter what you were trying to say")
    elif (x == "youtube"):
        print("Opening Youtube...")
        webbrowser.get('chrome').open("https://www.youtube.com/")
    elif (x == "netacad"):
        print("Opening Cisco Netacademy...")
        webbrowser.get('chrome').open("https://id.cisco.com/")
    elif (x== "steam"):
        print("Opening Steam....")
        subprocess.call("C:\QuickNeed\Steam\steam.exe")
    elif (x == "wordle"):
        print("Opening Wordle, good luck...")
        webbrowser.get('chrome').open("https://www.nytimes.com/games/wordle/index.html")
    elif (x == 'terraria'):
        print("Opening Terraria...")
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\Terraria\Terraria.exe")
    return(menuopen())
print(menuopen())