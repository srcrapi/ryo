# includes

from modules import common
import os

# code

def chocoUninstall(package):
  command = f"choco uninstall {package}"

  os.system(command)

def wgUninstall(package):
  command = f"winget uninstall {package}"

  os.system(command)

def uninstall_package(package):
  match package:
    case "discord":
      package_name = "Discord"
    case "epicgameslauncher":
      package_name = "Epic Games"
    case "spotify":
      package_name = "Spotify"

  option = str(input(f"  [*] Do you want to uninstall {package_name}? (y/n) : ")).lower()

  while option not in ["y", "yes", "n", "no"]:
    print("  [!] Enter a valid option.")
    option = str(input(f"  [*] Do you want to uninstall {package_name}? (y/n) : ")).lower()
  
  if option in ["y", "yes"]:
    print(f"  [+] Uninstalling {package_name}...")
    chocoUninstall(package)
    print(f"  [!] {package_name} uninstalled sucessfuly.")

def uninstallAll_package(discord_package, epic_package, spotify_package):
  package_name = "Discord"
  
  print(f"  [+] Uninstalling {package_name}...")
  chocoUninstall(discord_package)
  print(f"  [!] {package_name} uninstalled sucessfuly.")

  package_name = "Epic Games"

  print(f"  [+] Uninstalling {package_name}...")
  chocoUninstall(epic_package)
  print(f"  [!] {package_name} uninstalled sucessfuly.")
  
  package_name = "Spotify"

  print(f"  [+] Uninstalling {package_name}...")
  chocoUninstall(spotify_package)
  print(f"  [!] {package_name} uninstalled sucessfuly.")

def IDEuninstall():
  print("\n  [*] Select one IDE to uninstall:\n")
  print("           [1] Visual Studio Code")
  print("           [2] VSCodium")
  print("           [3] Pycharm")
  print("           [4] Visual Studio")
  print("          ---------------------")
  print("           [b] Back\n")

  ide_option = str(input("  -> Option : "))

  while common.ideSelected != True:
    match ide_option:
      case 1:
        chocoUninstall("vscode")
        ide = "VSCode"
        common.ideSelected = True
      case 2:
        chocoUninstall("vscodium")
        ide = "VSCodium"
        common.ideSelected = True
      case 3:
        chocoUninstall("pycharm-community")
        ide = "Pycharm"
        common.ideSelected = True
      case 4:
        chocoUninstall("visualstudio2022community")
        ide = "Visual Studio"
        common.ideSelected = True
      case _:
        print("  [!] Enter a valid value.")
        ide_option = str(input("  -> Option : "))

  print(f"\n  [!] {ide} uninstalled sucessfuly.")

  print("  [*] All the programs are uninstalled.")

def uninstallAll(confirmation):
  if confirmation == "confirmStandard":
    print("\n  [*] Select one browser to uninstall:\n")
    print("           [1] Firefox")
    print("           [2] Vivaldi")
    print("           [3] Chrome")
    print("           [4] Chromium")
    print("           [5] Waterfox")
    print("           [6] Brave")
    print("           [7] OperaGX")
    print("          ----------------")
    print("           [b] Back\n")

  if confirmation == "confirmDev":
    print("\n  [*] Select one browser to uninstall:\n")
    print("           [1] Firefox")
    print("           [2] Vivaldi")
    print("           [3] Chrome")
    print("           [4] Chromium")
    print("           [5] Waterfox")
    print("           [6] Brave")
    print("          ----------------")
    print("           [b] Back\n")

  browser_option = str(input("  -> Option : "))

  while common.browserSelected != True:
    match browser_option:
      case "1":
        chocoUninstall("firefox")
        browser = "Firefox"
        common.browserSelected = True
      case "2":
        chocoUninstall("vivaldi")
        browser = "Vivaldi"
        common.browserSelected = True
      case "3":
        chocoUninstall("googlechrome")
        browser = "Chrome"
        common.browserSelected = True
      case "4":
        wgUninstall("Hibbiki.Chromium")
        browser = "Chromium"
        common.browserSelected = True
      case "5":
        chocoUninstall("waterfox")
        browser = "Waterfox"
        common.browserSelected = True
      case "6":
        chocoUninstall("brave")
        browser = "Brave"
        common.browserSelected = True
      case "7":
        if confirmation == "confirmStandard":
          chocoUninstall("opera-gx")
          browser = "Opera GX"
          common.browserSelected = True
      case "b":
        Uninstall()
      case _:
        print("  [!] Enter a valid value.")
        browser_option = str(input("  -> Option : "))

    print(f"\n  [!] {browser} uninstalled sucessfuly.")

    uninstallAll_package("discord", "epicgameslauncher", "spotify")

    IDEuninstall()

def StandardUninstall():
  print("\n  [*] Do you want to uninstall all? (y/n)\n")

  uninstallAll_option = str(input("  -> Option : ")).lower()

  if uninstallAll_option in ["y", "yes"]:
    uninstallAll("confirmStandard")
    exit()

  print("\n  [*] Select one browser to uninstall:\n")
  print("           [1] Firefox")
  print("           [2] Vivaldi")
  print("           [3] Chrome")
  print("           [4] Chromium")
  print("           [5] Waterfox")
  print("           [6] Brave")
  print("           [7] OperaGX")
  print("          ----------------")
  print("           [b] Back\n")
  
  browser_option = str(input("  -> Option : "))

  while common.browserSelected != True:
    match browser_option:
      case "1":
        chocoUninstall("firefox")
        browser = "Firefox"
        common.browserSelected = True
      case "2":
        chocoUninstall("vivaldi")
        browser = "Vivaldi"
        common.browserSelected = True
      case "3":
        chocoUninstall("googlechrome")
        browser = "Chrome"
        common.browserSelected = True
      case "4":
        wgUninstall("Hibbiki.Chromium")
        browser = "Chromium"
        common.browserSelected = True
      case "5":
        chocoUninstall("waterfox")
        browser = "Waterfox"
        common.browserSelected = True
      case "6":
        chocoUninstall("brave")
        browser = "Brave"
        common.browserSelected = True
      case "7":
        chocoUninstall("opera-gx")
        browser = "Opera GX"
        common.browserSelected = True
      case "b":
        Uninstall()
      case _:
        print("  [!] Enter a valid value.")
        browser_option = str(input("  -> Option : "))

    print(f"\n  [!] {browser} uninstalled sucessfuly.")

    if os.path.exists(common.discordPath):
      uninstall_package("discord")

    if os.path.exists(common.discordPath):
      uninstall_package("epicgameslauncher")

    if os.path.exists(common.discordPath):
      uninstall_package("spotify")

    print("  [*] All the programs are uninstalled.")

def DevUninstall():
  print("\n  [*] Do you want to uninstall all? (y/n)\n")

  uninstallAll_option = str(input("  -> Option : ")).lower()

  if uninstallAll_option in ["y", "yes"]:
    uninstallAll("confirmDev")
    os.system("exit")

  print("\n  [*] Select one browser to uninstall:\n")
  print("           [1] Firefox")
  print("           [2] Vivaldi")
  print("           [3] Chrome")
  print("           [4] Chromium")
  print("           [5] Waterfox")
  print("           [6] Brave")
  print("           [7] Tor")
  print("          ----------------")
  print("           [b] Back\n")

  browser_option = str(input("  -> Option : "))

  while common.browserSelected != True:
    match browser_option:
      case "1":
        chocoUninstall("firefox")
        browser = "Firefox"
        common.browserSelected = True
      case "2":
        chocoUninstall("vivaldi")
        browser = "Vivaldi"
        common.browserSelected = True
      case "3":
        chocoUninstall("googlechrome")
        browser = "Chrome"
        common.browserSelected = True
      case "4":
        wgUninstall("Hibbiki.Chromium")
        browser = "Chromium"
        common.browserSelected = True
      case "5":
        chocoUninstall("waterfox")
        browser = "Waterfox"
        common.browserSelected = True
      case "6":
        chocoUninstall("brave")
        browser = "Brave"
        common.browserSelected = True
      case "7":
        chocoUninstall("opera-gx")
        browser = "Opera GX"
        common.browserSelected = True
      case "b":
        Uninstall()
      case _:
        print("  [!] Enter a valid value.")
        browser_option = str(input("  -> Option : "))

    print(f"\n  [!] {browser} uninstalled sucessfuly.")

    if os.path.exists(common.discordPath):
      uninstall_package("discord")

    if os.path.exists(common.discordPath):
      uninstall_package("epicgameslauncher")

    if os.path.exists(common.discordPath):
      uninstall_package("spotify")

    IDEuninstall()

def Uninstall():
  common.showLogo()

  print("\n                  +---------------+") 
  print("                  |   Uninstall   |")
  print("                  +---------------+\n")
  print("  [1] Stantard Uninstallation    [2] Dev Uninstallation\n")
  print("                      [b] Back\n\n")

  option = str(input("  [?] Select one option : "))

  while True:
    match option:
      case "1":
        StandardUninstall()
        break
      case "2":
        DevUninstall()
        break
      case "b":
        menu()
        break
      case _:
        print("  [!] Enter a valid value")
        option = str(input("  [?] Select one option : "))
