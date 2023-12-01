import os
from livereload import Server, shell
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BuildHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        os.system('jupyter-book build .')

if __name__ == '__main__':
    # Set up the build handler
    event_handler = BuildHandler()
    observer = Observer()
    observer.schedule(event_handler, '.', recursive=True)
    observer.start()

    # Set up the server
    server = Server()
    server.watch('.', shell('jupyter-book build .'))
    server.serve(root='_build/html', open_url_delay=1)
