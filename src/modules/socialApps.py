# includes

import os
from time import sleep
from modules import common

# code

def installSocialApp(socialApp, package, site):
  from main import menu

  print(f"\n  {common.bblue}[*]{common.blue} Preparing to install {common.bwhite}{socialApp}")
  print(f"  {common.bblue}[*] {common.blue}You can find more information about here: {common.purple}{site}\n\n")
  print(f"  {common.borange}[*] {common.orange}Press any key to continue", end="")
  os.system("pause > null")

  try:
    print(f"\n\n  {common.bgreen}[-] {common.green}Installing {socialApp}{common.white}...")
    common.installPackage(package)
    print(f"\n  {common.bgreen}[+] {common.green}{socialApp} sucessfuly installed{common.white}\n")
    
    print(f"  {common.bblue}[*] {common.blue}Press any key to return to ryo menu{common.white}", end="")
    os.system("pause > null")

    menu()
  except:
    common.handleError(f"Error trying to install {socialApp}")

def socialAppsMenu():
  from main import menu

  common.showLogo()

  print(f"{common.bwhite}  | Social Apps |{common.white}\n")
  print("  Choice :\n")
  print("  \t[1]\tDiscord")
  print("  \t[2]\tTelegram") 
  print("  \t[3]\tTeams")
  print("       --------------------------")
  print("  \t[b] return to main menu\n")

  option_socialApps = str(input(f"  {common.borange}[?]{common.white} Option : "))

  match option_socialApps:
    case "1":
      installSocialApp("Discord", "extras/discord", "https://discord.com/")
    case "2":
      installSocialApp("Telegram", "extras/telegram", "https://telegram.org/")
    case "3":
      installSocialApp("Teams", "extras/microsoft-teams", "https://www.microsoft.com/en-us/microsoft-teams/")
    case "b":
      menu()
    case _:
      print(f"\n  {common.bred}[!] {common.red}\"{option_socialApps}\" is not a valid option.{common.white}")
      sleep(2)
      socialAppsMenu()