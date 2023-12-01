from livereload import Server, shell
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class BuildJupyterBookHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command

    def on_any_event(self, event):
        os.system(self.command)

if __name__ == "__main__":
    path = 'digital_solutions_text'  # Replace with the path to your Jupyter Book
    build_command = 'jupyter-book build ' + path  # Command to build Jupyter Book

    # Set up watchdog observer
    event_handler = BuildJupyterBookHandler(build_command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    # Set up livereload server
    server = Server()
    server.watch(path, shell(build_command))
    server.serve(root='digital_solutions_text\_build\html')  # Replace with the path to your built book

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
