import os
from datetime import datetime

# Find name of folders
current_path = os.path.abspath(os.path.dirname(__file__))
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))

# name logfiles
log_file_current = os.path.join(current_path, "log_current_path.txt")
log_file_parent = os.path.join(parent_path, "log_parent_path.txt")

# message formatting
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
message = f"(simple_log_file.py) {timestamp}: Wrote this to file at current path location.\n"

# write to logfiles, or create files
def write_log(file_path):
    with open(file_path, "a") as log_file:
        log_file.write(message)

# save/ write to log files
write_log(log_file_current)
write_log(log_file_parent)

print("Log entries added.")

