import logging
import tkinter as tk
import tkinter.ttk as ttk

import modules.tkhelper as tkh
import modules.windows as windows


class _App():
    def __init__(self, root: tk.Tk):
        self.root = root
        self.pregame_window: windows.PregameWindow = None

    def build(self):
        self.build_root()
        self.build_pregame_window()

    def build_root(self):
        width = 600
        height = 600
        x = int((self.root.winfo_screenwidth()/2)-(width/2))
        y = int((self.root.winfo_screenheight()/2)-(height/2))
        self.root.title(string="PyDarts")
        self.root.minsize(width=width, height=height)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)

    def build_pregame_window(self):
        self.pregame_window = windows.PregameWindow(parent=self.root)
        self.pregame_window.build()

    def bind(self):
        self.bind_pregame_window()

    def bind_pregame_window(self):
        self.pregame_window.bind()

    def show(self):
        self.show_pregame_window()

    def show_pregame_window(self):
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


class App(tk.Tk):
    def __init__(self, enable_debugging: bool = False):
        super().__init__()
        self.app = _App(root=self)
        self.app.build()
        self.app.bind()
        self.app.show()

        if enable_debugging:
            self.app.configure_debugging()
