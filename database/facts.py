import sqlite3


def generate_event_facts(conn: sqlite3.Connection, events):
    cursor = conn.cursor()
    # Delete EVENT_FACTS table content
    cursor.execute('DROP TABLE IF EXISTS EVENT_FACTS')

    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS EVENT_FACTS (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            story_arc TEXT,
            character TEXT,
            location_1 TEXT,
            location_2 TEXT,
            location_3 TEXT,
            type TEXT NOT NULL,
            description TEXT,
            day INTEGER,
            month INTEGER,
            year INTEGER
        )
    ''')

    # Insert events
    for event in events:
        cursor.execute('''
                INSERT INTO EVENT_FACTS (story_arc, character, location_1, location_2, location_3, type, description, day, month, year)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (event.story_arc, event.character,
                  event.location_1, event.location_2, event.location_3,
                  event.type, event.description,
                  event.day, event.month, event.year))

    conn.commit()
    return True
