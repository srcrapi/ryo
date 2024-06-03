import components
import os
import time
import subprocess

def admin_verification() -> bool:


  return True


def scoop_verification() -> None:
  user: str = os.getlogin()
  scoop_dir: str = f"C:\\Users\\{user}\\.config\\scoop"

  if not os.path.isdir(scoop_dir):
    return

  print("Scoop not installed...")

  install_scoop = str(input("Install Scoop (yes/no)? ")).lower()

  while("y" not in list(install_scoop)[0] and "n" not in list(install_scoop)[0]):
    print("You can only answer with \"yes\" or \"no\"")
    install_scoop = str(input("Install Scoop (yes/no)? ")).lower()

  if "n" in list(install_scoop)[0]:
    return

  try:
    subprocess.Popen(["powershell", "Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser"], shell=True)
  except subprocess.CalledProcessError as err:
    print(f"Faild to complete the operation: {err.output}")


  time.sleep(5)



def main() -> None:
  admin_verification()
  scoop_verification()

  os.system("cls")

  print("[1] Browsers")
  print("[2] Development Environment")
  print("[3] Image Editors")
  print("[4] About")
  print("[5] Exit\n\n")

  try:
    option = int(input("Option: "))
  except ValueError:
    print("The option can only be a integer")
    time.sleep(2)

    main()

  match option:
    case 1:
      components.browsers.browser_menu()
    case _:
      print(f"\nOption \"{option}\" don't exist")
      main()


if __name__ == "__main__":
  main()