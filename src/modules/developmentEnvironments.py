# includes

import os
from time import sleep
from modules import common

# code

def installIDE(ide, package, site):
  from main import menu

  print(f"\n  {common.bblue}[*]{common.blue} Preparing to install {ide}")
  print(f"  {common.bblue}[*] {common.blue}You can find more information about here: {common.purple}{site}\n\n")
  print(f"  {common.borange}[*] {common.orange}Press any key to continue", end="")
  os.system("pause > null")

  try:
    print(f"\n\n  {common.bgreen}[-] {common.green}Installing {ide}{common.white}...")
    common.installPackage(package)
    print(f"\n  {common.bgreen}[+] {common.green}{ide} sucessfuly installed{common.white}\n")
    
    print(f"  {common.bblue}[*] {common.blue}Press any key to return to ryo menu{common.white}", end="")
    os.system("pause > null")

    menu()
  except:
    common.handleError(f"Error trying to install {ide}")

def ideMenu():
  from main import menu

  common.showLogo()
  
  print(f"{common.bwhite}  | Development Environments |{common.white}\n")
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

  option_ide = str(input(f"  {common.borange}[?]{common.white} Option : "))

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
      print(f"\n  {common.bred}[!] {common.red}\"{option_ide}\" is not a valid option.{common.red}")
      sleep(2)
      ideMenu()