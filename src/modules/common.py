# includes

import os
from time import sleep

# Variables

epicGamesPath = "C:\\Program Files (x86)\\Epic Games"
discordPath = os.path.join(os.environ["APPDATA"], "Discord")
spotifyPath = os.path.join(os.environ["APPDATA"], "Spotify")
chocoPath = "C:\\ProgramData\\chocolatey\\"
browserSelected = False
ideSelected = False

# Colors

# Functions

def showLogo():
    os.system("cls")
    
    print("\n    +--------------------------------------+")
    sleep(0.1)
    print("    |                                      |")
    sleep(0.1)
    print("    |      ██████╗ ██╗   ██╗ ██████╗       |")
    sleep(0.1)
    print("    |      ██╔══██╗╚██╗ ██╔╝██╔═══██╗      |")
    sleep(0.1)
    print("    |      ██████╔╝ ╚████╔╝ ██║   ██║      |")
    sleep(0.1)
    print("    |      ██╔══██╗  ╚██╔╝  ██║   ██║      |")
    sleep(0.1)
    print("    |      ██║  ██║   ██║   ╚██████╔╝      |")
    sleep(0.1)
    print("    |      ╚═╝  ╚═╝   ╚═╝    ╚═════╝       |")
    sleep(0.1)
    print("    |               By rap1                |")
    sleep(0.1)
    print("    +--------------------------------------+\n")
    sleep(0.1)