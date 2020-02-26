import os
import sys
import time
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

Image.MAX_IMAGE_PIXELS = 1000000000  

path = u'path to file watches' # поменяем директорию на ту, где у нас расположены картинки

class Event(LoggingEventHandler):
    def dispatch(self, event):
        if event.event_type == 'modified':
            if event.is_directory == False:
                if ('.tif' in event.src_path or '.tiff' in event.src_path) and (not '.png' in event.src_path):                    					
					self.convertfile(event.src_path)
    
    def convertfile(self, filename):
        time.sleep(10) 
        if not os.path.exists(filename + ".png"):
                try:                    
                    im = Image.open(filename)
                    im.save(filename + ".png", "PNG")
                except:
                    print("error converting file " + filename)


event_handler = Event()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

