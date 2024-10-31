import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="fcalendar",
        description="fcalendar: CLI to manage fictional calendar data"
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='fcalendar 1.0',
        help="shows the app version"
    )

    args = parser.parse_args()

    print("Welcome to fcalendar. Use '--help' to see the available options.")


if __name__ == "__main__":
    main()
