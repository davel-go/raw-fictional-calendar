import os
from datetime import datetime


def log_action(message, level='INFO', log_file='project.log'):
    # Get log file or create if not exists
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = os.path.join(project_root, log_file)

    # Format
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_message = f"[{timestamp}] [{level}] {message}\n"

    # Write message
    with open(log_file, 'a') as f:
        f.write(log_message)

    print("Log actualizado:", log_message.strip())
