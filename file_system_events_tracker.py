import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler

from_dir = "C:/Users/Swara/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):

   def on_created(self, event) :
      print("File hs been created {event.src_path}" )

   def on_deleted(self, event) :
      print("File has been deleted {event.src_path}")
    
   def on_modified(self, event) :
    print("File has been modified {event.src_path}")

   def on_closed(self, event) :
    print("File has been closed {event.src_path}")
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
   time.sleep(2)
   print("stopped")
   observer.stop()




