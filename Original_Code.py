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
chrome_path = "C:\QuickNeed\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
#os.system('notepad.exe')   
#def opengeforce():
    #subprocess.call("C:")
print("Hello, welcome to the PC!")
print("I'm still a work in progress so have patience.")
print("My creator has big plans for me.")

def menuopen():
    x = input("What would you like to open? Q to quit. ")
    if (x == "q"):
        print("Exiting Program...")
        exit()
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
    elif (x == "esc"):
        
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\The_Escapists\Escapists.exe")
    elif (x == "geo"):
        
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\Geometry_Dash_Old\GeometryDash.exe")
    elif (x == "vs"):
        subprocess.call("C:\Users\Tgoodwin\AppData\Roaming\Microsoft\Windows\Start_Menu\Programs\Visual_Studio_Code\code.exe")
    else:
        print("That program was either not recognized or has not been inputted into the program.")
        print("Please retry opening the program if there was a typo.")
        print("If you want a program added to the program add it.")
    return(menuopen())
    

print(menuopen())