import os
from dotenv import load_dotenv

# Ruta al archivo .env en el directorio raíz del proyecto
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')

# Cargar las variables de entorno desde el archivo .env
load_dotenv(ENV_PATH)

# Ejemplo de acceso a las variables de entorno
DB_NAME = os.getenv('DB_NAME', 'test')
WORK_DIR = os.getenv('WORKING_DIR', '/')

print("Database Name:", DB_NAME)
print("Work Dir:", WORK_DIR)