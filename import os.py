import os
import runpy
import subprocess
import webbrowser
import psutil
def menureopen():
    x = input("What would you like to open now? B to go back to the main menu. ")
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
    return(menureopen())