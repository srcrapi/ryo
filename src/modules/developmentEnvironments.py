# includes

import os
from time import sleep
from modules import common

# code

def handleError(message, error):
  print(f"  -> {message} : {error}")
  exit()

def installPackage(package):
  if package == "visualstudiocommunity2013":
    os.system("choco install visualstudiocommunity2013")

  else:
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
    installPackage(package)
    print(f"\n  [+] {ide} sucessfuly installed")
    
    print("  [*] Press any key to return to ryo menu", end="")
    os.system("pause > null")

    menu()
  except Exception as error:
    handleError(f"Error trying to install {ide}", error)

def ideMenu():
  from ryo import menu

  common.showLogo()
  
  print("  | Development Environments |\n")
  print("  Choice :\n")
  print("  \t[1]\tArduino")
  print("  \t[2]\tVisual Studio Code")
  print("  \t[3]\tVS Codium")
  print("  \t[4]\tCode Blocks")
  print("  \t[5]\tEclipse Java")
  print("  \t[6]\tPycharm Community")
  print("  \t[7]\tNetbeans")
  print("  \t[8]\tVisual Studio 2013")
  print("  \t[9]\tIntelliJ IDEA Community Edition")
  print("  \t[10]\tAndroid Studio")
  print("  \t[11]\tPHPStorm")
  print("       --------------------------")
  print("  \t[b] return to main menu\n")

  option_ide = str(input("  -> Option : "))

  match option_ide:
    case "1":
      installIDE("Arduino", "extras/arduino", "https://www.arduino.cc/")
    case "2":
      installIDE("Visual Studio Code", "vscode", "https://code.visualstudio.com/")
    case "3":
      installIDE("VS Codium", "extras/vscodium", "https://vscodium.com/")
    case "4":
      installIDE("Code Blocks", "extras/codeblocks", "www.codeblocks.org")
    case "5":
      installIDE("Eclipse Java", "extras/eclipse-java", "www.eclipse.org")
    case "6":
      installIDE("Pycharm Community", "extras/pycharm", "www.jetbrains.com/pycharm")
    case "7":
      installIDE("Netbeans", "extras/netbeans", "netbeans.apache.org")
    case "8":
      installIDE("Visual Studio", "visualstudiocommunity2013", "https://visualstudio.microsoft.com/")
    case "9":
      installIDE("IntelliJ IDEA Community Edition", "extras/idea", "https://www.jetbrains.com/idea/")
    case "10":
      installIDE("Android Studio", "extras/android-studio", "developer.android.com/studio")
    case "11":
      installIDE("PHPStorm", "extras/phpstorm", "www.jetbrains.com/phpstorm")
    case "b":
      menu()
    case _:
      print(f"\n  [!] \"{option_ide}\" is not a valid option.")
      sleep(2)
      ideMenu()