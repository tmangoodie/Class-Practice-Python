#Tyler Goodwin
#CNS1, Original Python Code
#The code will be a menu that allows me to open applications I use everyday
#The code is being built so I can get around my home computer easier.
#The code will be able to open and close applications, possibly input an application name and it will open/close it
#-----------------------------------------------------------------------------------
import os
import runpy
import subprocess
import webbrowser
import psutil
#Importing webbrowser and subprocess allows me to open webpages and apps from the code.
#Chrome_path makes a variable for registering the webbrowser.
chrome_path = "C:\QuickNeed\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
#os.system('notepad.exe')   
#def opengeforce():
    #subprocess.call("C:")
print("Hello, welcome to the PC!")
#All of this menu is in menu open.
#I plan to make another menu to close apps
def menuopen():
    x = input("What would you like to open? Q to quit. ")
    if (x == "q"):
        print("Exiting Program...")
        exit()
        #Exis stops the program in its tracks, one of my first priorities
    elif (x == "chrome"):
        webbrowser.get('chrome').open_new_tab("chrome://newtab/")
    elif (x == "drive"):
        webbrowser.get('chrome').open("https://drive.google.com/drive/u/0/my-drive")
    elif (x == "github"):
        webbrowser.get('chrome').open("https://github.com/tmangoodie")
    elif (x == "youtube"):
        webbrowser.get('chrome').open("https://www.youtube.com/")
    elif (x == "netacad"):
        webbrowser.get('chrome').open("https://www.netacad.com/")
    elif (x== "steam"):
        subprocess.call("C:\QuickNeed\Steam\steam.exe")
    elif (x == "wordle"):
        webbrowser.get('chrome').open("https://www.nytimes.com/games/wordle/index.html")
    elif (x == 'terraria'):
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\Terraria\Terraria.exe")
    elif (x == "escapists"):
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\The_Escapists\Escapists.exe")
    elif (x == "wallpaper"):
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\wallpaper_engine\wallpaper64.exe")
    else:
        #Will print this if the input isnt recognized as any of the options
        print("That program was either not recognized or has not been inputted into the program.")
        print("Please retry opening the program if there was a typo.")
        print("If you want a program added to the program add it.")
    return(menuopen())
    
def menuclose():
    y = input("What program would you like to close?" )
    if (y == 'q'):
        print("Exiting Program...")
        exit()
    elif (y == 'chrome'):
        for process in (process for process in psutil.process_iter() if process.name()=="chrome.exe"):
            process.kill()
#print(menuopen())