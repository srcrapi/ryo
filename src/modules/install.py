# includes

from ryo import menu
from modules import common
import os

# code

def chocoInstall(package):
    command = f"choco install {package}"

    os.system(command)

def wgInstall(package):
    command = f"winget install {package}"

    os.system(command)

def install_package(package):
    match package:
        case "discord":
            package_name = "Discord"
        case "epicgameslauncher":
            package_name = "Epic Games"
        case "spotify":
            package_name = "Spotify"

    option = str(input(f"  [*] Do you want to install {package_name}? (y/n) : ")).lower()

    while option not in ["y", "yes", "n", "no"]:
        print("  [!] Enter a valid option.")
        option = str(input(f"  [*] Do you want to install {package_name}? (y/n) : ")).lower()
    
    if option in ["y", "yes"]:
        print(f"  [+] Installing {package_name}...")
        chocoInstall(package)
        print(f"  [!] {package_name} installed sucessfuly.")

def IDEinstall():
    print("\n  [*] Select one IDE:\n")
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
                chocoInstall("vscode")
                ide = "VSCode"
                common.ideSelected = True
            case 2:
                chocoInstall("vscodium")
                ide = "VSCodium"
                common.ideSelected = True
            case 3:
                chocoInstall("pycharm-community")
                ide = "Pycharm"
                common.ideSelected = True
            case 4:
                chocoInstall("visualstudio2022community")
                ide = "Visual Studio"
                common.ideSelected = True
            case _:
                print("  [!] Enter a valid value.")
                ide_option = str(input("  -> Option : "))

    print(f"\n  [!] {ide} installed sucessfuly.")

    print("  [*] All the programs are installed.")

def StandardInstall():
    print("\n  [*] Select one browser:\n")
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
                chocoInstall("firefox")
                browser = "Firefox"
                common.browserSelected = True
            case "2":
                chocoInstall("vivaldi")
                browser = "Vivaldi"
                common.browserSelected = True
            case "3":
                chocoInstall("googlechrome")
                browser = "Chrome"
                common.browserSelected = True
            case "4":
                wgInstall("Hibbiki.Chromium")
                browser = "Chromium"
                common.browserSelected = True
            case "5":
                chocoInstall("waterfox")
                browser = "Waterfox"
                common.browserSelected = True
            case "6":
                chocoInstall("brave")
                browser = "Brave"
                common.browserSelected = True
            case "7":
                chocoInstall("opera-gx")
                browser = "Opera GX"
                common.browserSelected = True
            case "b":
                Install()
            case _:
                print("  [!] Enter a valid value.")
                browser_option = str(input("  -> Option : "))

    print(f"\n  [!] {browser} installed sucessfuly.")

    if not os.path.exists(common.discordPath):
        install_package("discord")
    
    if not os.path.exists(common.epicGamesPath):
        install_package("epicgameslauncher")
    
    if not os.path.exists(common.spotifyPath):
        install_package("spotify")

    print("  [*] All the programs are installed.")

def DevInstall():
    print("\n  [*] Select one browser:\n")
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
                chocoInstall("firefox")
                browser = "Firefox"
                common.browserSelected = True
            case "2":
                chocoInstall("vivaldi")
                browser = "Vivaldi"
                common.browserSelected = True
            case "3":
                chocoInstall("googlechrome")
                browser = "Chrome"
                common.browserSelected = True
            case "4":
                wgInstall("Hibbiki.Chromium")
                browser = "Chromium"
                common.browserSelected = True
            case "5":
                chocoInstall("waterfox")
                browser = "Waterfox"
                common.browserSelected = True
            case "6":
                chocoInstall("brave")
                browser = "Brave"
                common.browserSelected = True
            case "7":
                wgInstall("TorProject.TorBrowser")
                browser = "Tor"
                common.browserSelected = True
            case "b":
                Install()
            case _:
                print("  [!] Enter a valid value.")
                browser_option = str(input("  -> Option : "))
    
    print(f"\n  [!] {browser_option} installed sucessfuly.")

    if os.system(f"cd {common.discordPath}") != True:
        discord_option = str(input("  [*] Do you want to uninstall discord? (y/n) : ")).lower()

        while discord_option != "y" and discord_option != "yes" and discord_option != "n" and discord_option != "no":
            print("  [!] Enter a valid option.")
            discord_option = str(input("  [*] Do you want to uninstall discord? (y/n) : ")).lower()
        
        if discord_option == "y" or discord_option == "yes":
            print("  [+] Installing discord...")
            chocoInstall("discord")
            print("  [!] Discord installed sucessfuly.")
    
    if os.system(f"cd {common.spotifyPath}") != True:
        spotify_option = str(input("  [*] Do you want to install spotify(y/n) : ")).lower()

        while spotify_option != "y" and spotify_option != "yes" and spotify_option != "n" and spotify_option != "no":
            print("  [!] Enter a valid option.")
            spotify_option = str(input("  [*] Do you want to uninstall spotify? (y/n) : ")).lower()
        
        if spotify_option == "y" or spotify_option == "yes":
            print("  [+] Installing Spotify...")
            chocoInstall("spotify")
            print("  [!] Spotify installed sucessfuly.") 

    IDEinstall()

def Install():
    common.showLogo()

    print("\n                  +---------------+") 
    print("                  |    Install    |")
    print("                  +---------------+\n")
    print("  [1] Stantard Installation     [2] Dev Installation\n")
    print("                      [b] Back\n\n")

    option = str(input("  [?] Select one option : "))

    while True:
        match option:
            case "1":
                StandardInstall()
                break
            case "2":
                DevInstall()
                break
            case "b":
                menu()
                break
            case _:
                print("  [!] Enter a valid value")
                option = str(input("  [?] Select one option : "))