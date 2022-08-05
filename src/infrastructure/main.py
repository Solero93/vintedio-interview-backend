import sys

from src.application.list_packages import ListPackages


def main():
    current_line = sys.stdin.readline()
    while current_line != "END":
        if current_line == "LIST":
            print("LIST")
            list_packages = ListPackages()
            list_packages.invoke()



if __name__ == "__main__":
    main()
