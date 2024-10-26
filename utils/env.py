import os
from dotenv import load_dotenv
from utils.log import log_action

log_action("INITIALIZING ENV VARS EXTRACTION TASK ===== ===== ===== =====")

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')

load_dotenv(ENV_PATH)

DB_NAME = os.getenv('DB_NAME', 'test')
WORK_DIR = os.getenv('WORKING_DIR', '/')

if not os.path.exists(WORK_DIR):
    WORK_DIR = os.path.abspath(os.sep)
    log_action(f"Directorio no encontrado. WORK_DIR se establece en el directorio root: {work_dir}", "WARNING")

log_action(f"   Database Name: {DB_NAME} ")
log_action(f"   Working Directory: {WORK_DIR} ")

print("Database Name: ", DB_NAME)
print("Work Dir: ", WORK_DIR)