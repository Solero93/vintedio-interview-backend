from src.application.list_packages import list_packages
from src.infrastructure.output_formatter import format_output


def main():
    packages = list_packages()
    print(format_output(packages))


if __name__ == "__main__":
    main()
