# includes

import os
from time import sleep
from modules import common

# code

def installBrowser(browser, package, site):
  from main import menu

  print(f"\n  {common.bblue}[*]{common.blue} Preparing to install {common.bwhite}{browser}")
  print(f"  {common.bblue}[*] {common.blue}You can find more information about here: {common.purple}{site}\n\n")
  print(f"  {common.borange}[*] {common.orange}Press any key to continue", end="")
  os.system("pause > null")

  try:
    print(f"\n\n  {common.bgreen}[-] {common.green}Installing {browser}{common.white}...")
    common.installPackage(package)
    print(f"\n  {common.bgreen}[+] {common.green}{browser} sucessfuly installed{common.white}\n")
    
    print(f"  {common.bblue}[*] {common.blue}Press any key to return to ryo menu{common.white}", end="")
    os.system("pause > null")

    menu()
  except:
    common.handleError(f"Error trying to install {browser}")

def browserMenu():
  from main import menu

  common.showLogo()

  print(f"{common.bwhite}  | Browsers |{common.white}\n")
  print("  Choice :\n")
  print("  \t[1]\tFirefox")
  print("  \t[2]\tVivaldi")
  print("  \t[3]\tGoogle Chrome")
  print("  \t[4]\tChromium")
  print("  \t[5]\tWaterfox")
  print("  \t[6]\tOpera")
  print("  \t[7]\tOpera Gx")
  print("  \t[8]\tBrave")
  print("  \t[9]\tTor")
  print("       --------------------------")
  print("  \t[b] return to main menu\n")

  option_browser = str(input(f"  {common.borange}[?]{common.white} Option : "))

  match option_browser:
    case "1":
      installBrowser("Firefox", "extras/firefox", "https://www.mozilla.org/firefox")
    case "2":
      installBrowser("Vivaldi", "extras/vivaldi", "https://vivaldi.com")
    case "3":
      installBrowser("Google Chrome", "extras/googlechrome", "https://www.google.com/chrome")
    case "4":
      installBrowser("Chromium", "extras/chromium", "https://www.chromium.org")
    case "5":
      installBrowser("Waterfox", "extras/waterfox", "https://www.waterfox.net")
    case "6":
      installBrowser("Opera", "extras/opera", "https://www.opera.com")
    case "7":
      installBrowser("Opera Gx", "extras/opera-gx", "https://www.opera.com/gx")
    case "8":
      installBrowser("Brave", "extras/brave", "https://brave.com")
    case "9":
      installBrowser("Tor", "extras/tor-browser", "https://www.torproject.org")
    case "b":
      menu()
    case _:
      print(f"\n  {common.bred}[!] {common.red}\"{option_browser}\" is not a valid option.{common.white}")
      sleep(2)
      browserMenu()