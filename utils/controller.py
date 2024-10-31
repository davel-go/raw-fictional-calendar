from database.conn import CONN
from database.queries import db_get_event
from entity.EventPreload import EventPreload
from utils.log import log_action


def get_event(id):
    log_action(f"CONTROLLER ACTION  --get_event--   Searching event with ID: {id}")
    event = db_get_event(CONN, id)
    if event is None:
        log_action(f"    Event not found (event id: {id})", "WARNING")
    else:
        event = EventPreload(*event)
        log_action(f"    Successful extraction of event {id}")
    return event
