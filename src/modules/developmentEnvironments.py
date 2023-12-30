# includes

import os
from modules import common

# code

def handleError(message, error):
  print(f"  -> {message} : {error}")
  exit()

def scoopInstall(package):
  os.system("scoop install add extras > null")

  command = f"scoop install {package}"

  os.system(command)

def installIDE(ide, package, site):
  from ryo import menu

  print(f"\n  [*] Preparing to install {ide}\n")
  print(f"  [*] You can find more information about here: {site}\n\n")
  print("  [*] Press any key to continue", end="")
  os.system("pause > null")

  try:
    print(f"\n\n  [-] Installing {ide}...")
    scoopInstall(package)
    print(f"\n  [+] {ide} sucessfuly installed")
    
    print("  [*] Press any key to return to ryo menu", end="")
    os.system("pause > null")

    menu()
  except Exception as error:
    handleError(f"Error trying to install {ide}", error)

def ideMenu():
  common.showLogo()
  
  print("  | Development Environments |\n")
  print("  Choice :\n")
  print("  \t[1]\tArduino")
  print("  \t[2]\tVisual Studio Code")
  print("  \t[3]\tVS Codium")
  print("  \t[4]\tCode Blocks")
  print("  \t[5]\tEclipse")
  print("  \t[6]\tPycharm")
  print("  \t[7]\tNetbeans")
  print("  \t[8]\tVisual Studio")
  print("  \t[9]\tIntelliJ IDEA Community Edition")
  print("  \t[10]\tAndroid Studio")
  print("  \t[11]\tPHPStorm")
  print("       --------------------------")
  print("  \t[b] return to main menu\n")

  option_ide = str(input("  -> Option : "))

  while True:
    match option_ide:
      case "1":
        installIDE("Arduino", "extras/arduino", "https://www.arduino.cc/")
        break
      case "2":
        installIDE("Visual Studio Code", "vscode", "https://code.visualstudio.com/")
        break
      case "3":
        installIDE("VS Codium", "extras/vscodium", "https://vscodium.com/")
        break
      case "4":
        installIDE("Code Blocks", "extras/vscodium", "https://vscodium.com/")
        break
      case "5":
        installIDE("Eclipse", "extras/vscodium", "https://vscodium.com/")
        break
      case "6":
        installIDE("Pycharm", "extras/vscodium", "https://vscodium.com/")
        break
      case "7":
        installIDE("Netbeans", "extras/vscodium", "https://vscodium.com/")
        break
      case "8":
        installIDE("Visual Studio", "extras/vscodium", "https://vscodium.com/")
        break
      case "9":
        installIDE("IntelliJ IDEA Community Edition", "extras/vscodium", "https://vscodium.com/")
        break
      case "10":
        installIDE("Android Studio", "extras/vscodium", "https://vscodium.com/")
        break
      case "11":
        installIDE("PHPStorm", "extras/vscodium", "https://vscodium.com/")
        break
      case "b":
        from ryo import menu
        menu()
      case _:
        print("\n  [!] Enter a valid value.\n")