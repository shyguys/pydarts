import logging
import tkinter as tk
import tkinter.ttk as ttk

import pydarts.gui.pregame
import pydarts.help.tkh as tkh


class Root():
    def __init__(self, name: str):
        self._name = name
        self._app = tk.Tk()
        self._root = ttk.Frame(master=self._app)
        self._pregame_window = pydarts.gui.pregame.Root(self._root)
        self._build()
        self._bind()

    def mainloop(self, debug: bool = False):
        if debug:
            self._enable_debugging()
        self._app.mainloop()

    def _build(self):
        self._build_app()
        self._build_root()

    def _build_app(self):
        app = self._app
        app.title(self._name)
        width = 500
        height = 600
        x = int((app.winfo_screenwidth()/2)-(width/2))
        y = int((app.winfo_screenheight()/2)-(height/2))
        app.minsize(width=width, height=height)
        app.maxsize(width=width, height=height)
        app.geometry(f"{width}x{height}+{x}+{y}")
        app.rowconfigure(index=0, weight=1)
        app.columnconfigure(index=0, weight=1)

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        self._pregame_window.root.grid(row=0, column=0, sticky="nsew")

    def _bind(self):
        self._bind_root()

    def _bind_root(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PREGAME_WINDOW_FINISHED.value,
            self._handle_pregame_window_finished
        )

    # [TODO]: display grid cell borders
    def _enable_debugging(self):
        self._highlight_children()
        sequences = ["<KeyRelease>"]
        for sequence in sequences:
            self._catch_event(sequence)

    def _highlight_children(self):
        for widget in tkh.walk_children(self._root):
            try:
                widget.configure(borderwidth=1, relief="solid")
            except tk.TclError:
                # Widget has no 'borderwidth' option
                logging.warning(f"widget cannot be bordered: {widget!r}")

    def _catch_event(self, sequence: str):
        self._root.bind_all(sequence, self._handle_event)

    def _handle_event(self, event: tk.Event = None):
        logging.info(
            f"application caught event:\n"
            f"  event: {event!r}\n"
            f"  widget: {event.widget!r}"
        )

    def _handle_pregame_window_finished(self, event: tk.Event = None):
        self._pregame_window.root.destroy()
