from database.conn import CONN
from database.queries import get_events
from entity.EventPreload import EventPreload


def print_all_events():
    events = get_events(CONN)
    events = [EventPreload(*e) for e in events]
    for e in events:
        print(e)

# print_all_events()