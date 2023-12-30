# includes

from modules import developmentEnvironments, browsers, imageEditor
from modules import common
from modules import uninstall
from time import sleep

# ryo 1.0

def showAbout():
    common.showLogo()
    
    print("  +------------------------------------------------+")
    print(f"  |                      {common.bblue}Ryo{common.white}                       |")
    print(f"  |          {common.orange}Windows Application Installer{common.white}         |")
    print("  +------------------------------------------------+")
    print(f"  |                {common.bwhite}OS{common.white}      : {common.bpurple}Windows{common.white}               |")
    print(f"  |                {common.bwhite}Version{common.white} : {common.bpurple}1.0{common.white}                   |")
    print(f"  |                {common.bwhite}Author{common.white}  : {common.bpurple}rap1{common.white}                  |")
    print("  +------------------------------------------------+\n")
    print(f"  {common.bred}Description\n")
    print(f"  {common.blue}Ryo is a script write in python")
    print(f"  with the objetive to be an app installer for windows.{common.white}\n")
    print("                      [b] Back\n\n")

    try:
        back = str(input("  -> Option : "))

        while back != "b":
            print("  [!] Enter a valid value.")
            back = str(input("  -> Option : "))

        menu()
    except:
        print("\n\n  [!] Program Interrupted.\n")
        exit
        

def ryoExit():
    print(f"""
  {common.bblue}[*]{common.white} Thank you for using {common.bwhite}ryo{common.white}.
  {common.bblue}[*]{common.white} For more info you can always contact me on discord: {common.bpurple}.rap1{common.white}\n""")

def menu():
    common.showLogo()

    print("""\n
  [1] Development Environments     
  [2] Browsers
  [3] Image Editors
          
       [a] About ryo script         [q] Exit\n\n""")
    
    try:
        option = str(input(f"  {common.borange}[?]{common.white} Select one option : "))

        match option:
            case "1":
                developmentEnvironments.ideMenu()
            case "2":
                browsers.browserMenu()
            case "3":
                imageEditor.imageEditorMenu()
            case "a":
                showAbout()
            case "q":
                ryoExit()
            case _:
                print(f"\n  {common.bred}[!] {common.red}\"{option}\" is not a valid option.{common.white}")
                sleep(2)
                menu()
    except:
        print(f"\n\n  {common.bred}[!]{common.red} Program Interrupted{common.white}\n")
        

if __name__ == "__main__":
    menu()