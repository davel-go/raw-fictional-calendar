from database.conn import CONN
from database.init import initialize_events_table

initialize_events_table(CONN)
