from livereload import Server, shell
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time

class BuildJupyterBookHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.last_run = 0
        self.debounce_seconds = 10

    def should_rebuild(self):
        current_time = time.time()
        if current_time - self.last_run >= self.debounce_seconds:
            self.last_run = current_time
            return True
        return False

    def on_any_event(self, event):
        if event.is_directory or not event.src_path.endswith(('.ipynb', '.md')):
            return
        if self.should_rebuild():
            os.system(self.command)

if __name__ == "__main__":
    source_path = 'digital_solutions_text'  # Source files directory
    build_output_path = 'digital_solutions_text\_build\html'  # Adjust the path as per your system
    build_command = 'jupyter-book build ' + source_path

    # Set up watchdog observer
    event_handler = BuildJupyterBookHandler(build_command)
    observer = Observer()
    observer.schedule(event_handler, source_path, recursive=True)
    observer.start()

    # Set up livereload server
    server = Server()
    server.watch(source_path, shell(build_command))
    server.serve(root=build_output_path)

    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
