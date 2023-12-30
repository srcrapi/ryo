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
white = '\033[0m'
red = '\033[0;31m'
green = '\033[0;32m'
cyan = '\033[0;96m'
orange = '\033[0;33m'
blue = '\033[0;34m'
purple = '\033[0;35m'

#Bold colors

bwhite='\033[1m'
bred = '\033[1;31m'
bgreen = '\033[1;32m'
bcyan = '\033[1;96m'
borange = '\033[1;33m'
bblue = '\033[1;34m'
bpurple = '\033[1;35m'

# Functions

def installPackage(package):
  if package == "visualstudiocommunity2013":
    os.system("choco install visualstudiocommunity2013")

  else:
    os.system("scoop install add extras > null")

    command = f"scoop install {package}"

    os.system(command)

def handleError(message):
  print(f"  {borange}->{white} {message}")
  exit()

def showLogo():
    os.system("cls")
    
    print("\n    +--------------------------------------+")
    sleep(0.1)
    print("    |                                      |")
    sleep(0.1)
    print(f"    |      {blue}██████{cyan}╗ {blue}██{cyan}╗   {blue}██{cyan}╗ {blue}██████{cyan}╗{white}       |")
    sleep(0.1)
    print(f"    |      {blue}██{cyan}╔══{blue}██{cyan}╗╚{blue}██{cyan}╗ {blue}██{cyan}╔╝{blue}██{cyan}╔═══{blue}██{cyan}╗{white}      |")
    sleep(0.1)
    print(f"    |      {blue}██████{cyan}╔╝ ╚{blue}████{cyan}╔╝ {blue}██{cyan}║   {blue}██{cyan}║{white}      |")
    sleep(0.1)
    print(f"    |      {blue}██{cyan}╔══{blue}██{cyan}╗  ╚{blue}██{cyan}╔╝  {blue}██{cyan}║   {blue}██{cyan}║{white}      |")
    sleep(0.1)
    print(f"    |      {blue}██{cyan}║  {blue}██{cyan}║   {blue}██{cyan}║   ╚{blue}██████{cyan}╔╝{white}      |")
    sleep(0.1)
    print(f"    |      {cyan}╚═╝  ╚═╝   ╚═╝    ╚═════╝{white}       |")
    sleep(0.1)
    print(f"    |               By {bblue}rap1{white}                |")
    sleep(0.1)
    print("    +--------------------------------------+\n")
    sleep(0.1)