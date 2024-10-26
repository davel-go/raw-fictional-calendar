import sqlite3
import os
from utils.env import WORK_DIR, DB_NAME
from utils.log import log_action

DB_PATH = os.path.join(WORK_DIR, DB_NAME + '.db')
CONN = sqlite3.connect(DB_PATH)

if not os.path.exists(DB_PATH):
    log_action("There was a problem creating the database file", "ERROR")
else:
    log_action("Successful creation of the database file. Connection loaded")
