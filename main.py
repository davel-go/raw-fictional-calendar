from database.conn import CONN
from database.init import initialize_events_table
from database.queries import get_events
from entity.EventPreload import EventPreload

initialize_events_table(CONN)

