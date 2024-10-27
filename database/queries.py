import sqlite3
from entity.EventPreload import EventPreload


def get_events(conn: sqlite3.Connection):
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM events")
    return data.fetchall()


def get_events_as_kvm(conn : sqlite3.Connection):
    cursor = conn.cursor()
    data = cursor.execute("SELECT * FROM events")
    events = [EventPreload(*e) for e in data.fetchall()]
    kvm = {e.id: e for e in events}
    return kvm


def get_event(conn : sqlite3.Connection, id: int):
    cursor = conn.cursor()
    query = f"SELECT * FROM events WHERE id = {id}"
    data = cursor.execute(query)
    return data.fetchone()
