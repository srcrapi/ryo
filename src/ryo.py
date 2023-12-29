# includes

from modules import developmentEnvironments
from modules import common
from modules import install
from modules import uninstall

# ryo 1.0

def showAbout():
    common.showLogo()
    
    print("  +------------------------------------------------+")
    print("  |                      Ryo                       |")
    print("  |          Windows Application Installer         |")
    print("  +------------------------------------------------+")
    print("  |                OS      : Windows               |")
    print("  |                Version : 1.0                   |")
    print("  |                Author  : rap1                  |")
    print("  +------------------------------------------------+\n")
    print("  Description\n")
    print("  Ryo is a script write in powershell")
    print("  with the objetive to be an app installer for windows.\n")
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
    print("""
  [*] Thank you for using ryo.
  [*] For more info you can always contact me on discord: .rap1\n""")

def menu():
    common.showLogo()

    print("""\n
         [1] Development Environments       [2] Uninstall\n
      [a] About ryo script         [q] Exit\n\n""")
    
    try:
        option = str(input("  [?] Select one option : "))

        match option:
            case "1":
                developmentEnvironments.ideMenu()
            case "2":
                uninstall.Uninstall()
            case "a":
                showAbout()
            case "q":
                ryoExit()
            case _:
                print("  [!] Enter a valid value.\n")
    except:
        print("\n\n  [!] Program Interrupted\n")
        

if __name__ == "__main__":
    menu()