#Tyler Goodwin
#CNS1, Original Python Code
#The code will be a menu that allows me to open applications I use everyday
#The code is being built so I can get around my home computer easier.
#The code will be able to open and close applications, possibly input an application name and it will open/close it
#-----------------------------------------------------------------------------------
import os
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
        print("Opening Chrome...")
        webbrowser.get('chrome').open_new_tab("chrome://newtab/")
    elif (x == "drive"):
        print("Opening Drive...")
        webbrowser.get('chrome').open("https://drive.google.com/drive/u/0/my-drive")
    elif (x == "github"):
        print("Opening GitHub...")
        webbrowser.get('chrome').open("https://github.com/tmangoodie")
    elif (x == "youtube"):
        print("Opening Youtube...")
        webbrowser.get('chrome').open("https://www.youtube.com/")
    elif (x == "netacad"):
        print("Opening Cisco Netacademy...")
        webbrowser.get('chrome').open("https://www.netacad.com/")
    elif (x== "steam"):
        print("Opening Steam....")
        subprocess.call("C:\QuickNeed\Steam\steam.exe")
    elif (x == "wordle"):
        print("Opening Wordle, good luck...")
        webbrowser.get('chrome').open("https://www.nytimes.com/games/wordle/index.html")
    elif (x == 'terraria'):
        print("Opening Terraria...")
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\Terraria\Terraria.exe")
    elif (x == "esc"):
        print("Opening The Escapists...")
        subprocess.call("C:\QuickNeed\Steam\steamapps\common\The_Escapists\Escapists.exe")
    else:
        print("That program was either not recognized or has not been inputted into the program.")
        print("Please retry opening the program if there was a typo.")
        print("If you want a program added to the program add it.")
    return(menuopen())
    

print(menuopen())