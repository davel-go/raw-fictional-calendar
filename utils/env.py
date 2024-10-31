import os
from dotenv import load_dotenv
from utils.log import log_action

log_action("INITIALIZING ENV VARS EXTRACTION TASK ===== ===== ===== =====")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')

load_dotenv(ENV_PATH)

DB_NAME = os.getenv('DB_NAME', 'test')
WORK_DIR = os.getenv('WORKING_DIR', '/')
DAYS_PER_MONTH = os.getenv('DAYS_PER_MONTH', 115)
MONTHS_PER_YEAR = os.getenv('MONTHS_PER_YEAR', 6)

if not os.path.exists(WORK_DIR):
    WORK_DIR = os.path.abspath(os.sep)
    log_action(f"Directory not found. WORK_DIR will be: {WORK_DIR}", "WARNING")

log_action(f"   Database Name: {DB_NAME} ")
log_action(f"   Working Directory: {WORK_DIR} ")
log_action(f"   DAYS_PER_MONTH: {DAYS_PER_MONTH} ")
log_action(f"   MONTHS_PER_YEAR: {MONTHS_PER_YEAR} ")

print("Database name: ", DB_NAME)
print("Work dir: ", WORK_DIR)
print("Days per mont: ", DAYS_PER_MONTH)
print("Months per year: ", MONTHS_PER_YEAR)