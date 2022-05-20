#Tyler Goodwin
#CNS1, Original Python Code
#The code will be a menu that allows me to open applications I use everyday
#The code is being built so I can get around my home computer easier.
#The code will be able to open and close applications, possibly input an application name and it will open/close it
#-----------------------------------------------------------------------------------
import os
import subprocess
#os.system('notepad.exe')
def opensteam():
    subprocess.call("C:\SteamR\Steam\steam.exe")

#subprocess.call()
subprocess.call("C:\Program Files\Google\Drive File Stream\launch.bat")
subprocess.call("C:\SteamR\Steam\steamapps\common\Terraria\Terraria.exe")
print("Hello, welcome to the PC!")
print("I'm still a work in progress so have patience.")
print("My creator has big plans for me.")
print("What would you like to do?")
