import argparse
from utils.controller import get_event


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

    subparsers = parser.add_subparsers(dest="command")
    event_parser = subparsers.add_parser("event", help="Get information about an event  with its ID")
    event_parser.add_argument("event_id", type=int, help="Event ID")

    args = parser.parse_args()

    if args.command == "event":
        event_info = get_event(args.event_id)
        if event_info is None:
            print("We couldn't find that event id in the database")
        else:
            print("Event information: \n ===", event_info, "\n===")

    print("Welcome to fcalendar. Use '--help' to see the available options.")


if __name__ == "__main__":
    main()
