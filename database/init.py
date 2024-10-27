import sqlite3
from utils.log import log_action


def initialize_events_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS EVENTS (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        story_arc TEXT,
        character TEXT,
        location_1 TEXT,
        location_2 TEXT,
        location_3 TEXT,
        type TEXT NOT NULL,
        desc TEXT,
        day INTEGER,
        month INTEGER,
        year INTEGER,
        anchor_event INTEGER,
        before BOOLEAN NOT NULL,
        a_day INTEGER,
        a_month INTEGER,
        a_year INTEGER
    )
    ''')
    # Save changes
    conn.commit()
    log_action("Events table initialized")
