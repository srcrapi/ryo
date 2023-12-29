# includes

import os
from modules import common


# code

def ideMenu():
  common.showLogo()
  
  print("  | Development Environments |\n")
  print("  Choice :\n")
  print("  \t[b] return to main menu")

  option_ide = str(input("[?] Select an option : "))

  match option_ide:
    case "b":
      from ryo import menu
      menu()
    case _:
      print("  [!] Enter a valid value.\n")