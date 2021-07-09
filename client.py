import os
from colours import bcolors, enterprompt
from __main__ import greeting
import subprocess


def main(path, syner):
    os.chdir(path)
    choi = "1"
    while choi != "5":
        os.system("cls")
        greeting()
        print(f"\n1) {bcolors.OKGREEN}Push/Pull Related Options{bcolors.ENDC}\n"
              f"2) {bcolors.OKBLUE}Commit, Checkout And Stash{bcolors.ENDC}\n"
              f"3) {bcolors.OKCYAN}Show Differences{bcolors.ENDC}\n"
              f"4) {bcolors.HEADER}Branch Administration{bcolors.ENDC}\n"
              f"99) {bcolors.WARNING}Quit{bcolors.ENDC}")
        choi = input(": ")
        match choi:
            case "1":
                import origin
                origin.main()
            case "2":
                import commit
                commit.main()
            case "3":
                print(f"\n\n{bcolors.UNDERLINE}{bcolors.OKGREEN}Red = Removed\nGreen = Added\nUse The Up And Down Arrow To Go Up And Down\nType 'q' To Leave!{bcolors.ENDC}\n\n")
                enterprompt()
                a = subprocess.call("git diff", shell=True)
                print(a)
            case "4":
                import branches
                branches.main()
            case "99":
                os.system("cls")
                quit(0)
            case _:
                pass

