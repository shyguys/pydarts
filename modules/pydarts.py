import argparse
import logging
import tkinter as tk
import tkinter.ttk as ttk

import modules.tkhelper as tkh
import modules.windows as windows


class PyDarts():
    def __init__(self, enable_debugging: bool = False):
        self.app = tk.Tk()
        self.root = ttk.Frame(master=self.app)
        self.pregame_window = windows.PregameWindow(parent=self.root)
        self.build()
        self.show()

        if enable_debugging:
            self.configure_debugging()

    def build(self):
        self.build_app()
        self.build_root()

    def build_app(self):
        app = self.app
        app.title(string="PyDarts")

        width = 500
        height = 600
        x = int((app.winfo_screenwidth()/2)-(width/2))
        y = int((app.winfo_screenheight()/2)-(height/2))
        app.minsize(width=width, height=height)
        app.maxsize(width=width, height=height)
        app.geometry(f"{width}x{height}+{x}+{y}")
        
        app.rowconfigure(index=0, weight=1)
        app.columnconfigure(index=0, weight=1)

    def build_root(self):
        widget = self.root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def show(self):
        self.pregame_window.root.grid(row=0, column=0, sticky="nsew")

    # [TODO]: display grid cell borders
    def configure_debugging(self):
        self.highlight_children()
        sequences = ["<KeyRelease>"]
        for sequence in sequences:
            self.catch_event(sequence)

    def highlight_children(self):
        for widget in tkh.walk_children(self.root):
            try:
                widget.configure(borderwidth=1, relief="solid")
            except tk.TclError:
                # Widget has no 'borderwidth' option
                logging.warning(f"widget cannot be bordered: {widget!r}")

    def catch_event(self, sequence: str):
        self.root.bind_all(sequence, self.handle_event)

    def handle_event(self, event: tk.Event = None):
        logging.info(
            f"application caught event:\n"
            f"  event: {event!r}\n"
            f"  widget: {event.widget!r}"
        )

def parse_args() -> argparse.Namespace:
    prog = "pydarts"
    parser = argparse.ArgumentParser(prog=prog)
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False,
        dest="enable_debugging", help="highlight widgets and be verbose"
    )
    return parser.parse_args()

def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s - %(levelname)s] %(message)s",
        datefmt="%H:%M:%S"
    )

def main():
    configure_logging()
    args = parse_args()
    pydarts = PyDarts(args.enable_debugging)
    pydarts.app.mainloop()
