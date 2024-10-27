from database.conn import CONN
from database.init import initialize_events_table
from database.queries import get_events
from entity.EventPreload import EventPreload

initialize_events_table(CONN)
events = get_events(CONN)
events = [EventPreload(*e) for e in events]
for e in events:
    print(e)
