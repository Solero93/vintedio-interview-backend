from src.application.list_packages import ListPackages
from src.infrastructure.output_formatter import format_output


def main():
    list_packages = ListPackages()
    print(format_output(list_packages.invoke()))


if __name__ == "__main__":
    main()
