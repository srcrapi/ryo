# include

import os
from time import sleep
from modules import common

# code

def installImageEditor(imageEditor, package, site):
  from ryo import menu

  print(f"\n  {common.bblue}[*]{common.blue} Preparing to install {imageEditor}")
  print(f"  {common.bblue}[*] {common.blue}You can find more information about here: {common.purple}{site}\n\n")
  print(f"  {common.borange}[*] {common.orange}Press any key to continue", end="")
  os.system("pause > null")

  try:
    print(f"\n\n  {common.bgreen}[-] {common.green}Installing {imageEditor}{common.white}...")
    common.installPackage(package)
    print(f"\n  {common.bgreen}[+] {common.green}{imageEditor} sucessfuly installed{common.white}\n")
    
    print(f"  {common.bblue}[*] {common.blue}Press any key to return to ryo menu{common.white}", end="")
    os.system("pause > null")

    menu()
  except Exception as error:
    common.handleError(f"Error trying to install {imageEditor}")

def imageEditorMenu():
  from ryo import menu
  
  common.showLogo()

  print(f"{common.bwhite}  | Image Editor |{common.white}\n")
  print("  Choice :\n")
  print("  \t[1]\tGimp")
  print("  \t[2]\tKrita")
  print("       --------------------------")
  print("  \t[b] return to main menu\n")

  option_editor = str(input(f"  {common.borange}[?]{common.white} Option : "))

  match option_editor:
    case "1":
      installImageEditor("Gimp")
    case "2":
      installImageEditor("Krita")
    case "b":
      menu()
    case _:
      print(f"\n  {common.bred}[!] {common.red}\"{option_editor}\" is not a valid option.{common.red}")
      sleep(2)
      imageEditorMenu()