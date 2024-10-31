from database.conn import CONN
from database.queries import db_get_event
from entity.EventPreload import EventPreload


def get_event(id):
    event = db_get_event(CONN, id)
    if event is not None:
        event = EventPreload(*event)
    return event
