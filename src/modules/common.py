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

#Regular colors
white='\033[0m'
red='\033[0;31m'
green='\e[0;32m'
cyan='\033[0;96m'
orange='\e[0;33m'
blue='\e[0;34m'
purple='\e[0;35m'

#Bold colors

bred='\033[1;31m'
bgreen='\e[1;32m'
bcyan='\033[1;96m'
borange='\e[1;33m'
bblue='\e[1;34m'
bpurple='\e[1;35m'

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