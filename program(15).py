import os
import time
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


# ------------------------------------------------
# Log file
# ------------------------------------------------

LOG_FILE = "file_monitor.log"


def log_event(event_type, path):
    """Record an event with date and time."""

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    message = (
        f"[{timestamp}] "
        f"{event_type}: {path}"
    )

    print(message)

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(message + "\n")


# ------------------------------------------------
# File System Event Handler
# ------------------------------------------------

class MonitorHandler(FileSystemEventHandler):

    def on_created(self, event):

        if not event.is_directory:
            log_event(
                "FILE CREATED",
                event.src_path
            )

    def on_modified(self, event):

        if not event.is_directory:
            log_event(
                "FILE MODIFIED",
                event.src_path
            )

    def on_deleted(self, event):

        if not event.is_directory:
            log_event(
                "FILE DELETED",
                event.src_path
            )

    def on_moved(self, event):

        if not event.is_directory:
            log_event(
                "FILE RENAMED",
                f"{event.src_path} -> {event.dest_path}"
            )


# ------------------------------------------------
# Main Program
# ------------------------------------------------

folder = input(
    "Enter folder path to monitor: "
).strip()

# Check whether folder exists
if not os.path.isdir(folder):
    print("Error: Folder does not exist.")
    exit()

print("\n====================================")
print("       FILE SYSTEM MONITOR")
print("====================================")

print("Monitoring:", folder)
print("Log file  :", LOG_FILE)
print("\nPress Ctrl+C to stop.\n")


# Create event handler
handler = MonitorHandler()

# Create observer
observer = Observer()

observer.schedule(
    handler,
    folder,
    recursive=True
)

observer.start()

try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    print("\nStopping monitor...")

    observer.stop()

observer.join()

print("Monitoring stopped.")
