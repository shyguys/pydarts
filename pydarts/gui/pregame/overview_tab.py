import tkinter as tk
import tkinter.ttk as ttk

import pydarts.core.metadata as metadata
import pydarts.gui.pregame.texts


class _Mode():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Labelframe(master=self._parent)
        self._name = ttk.Label(master=self._root)
        self._separator = ttk.Separator(master=self._root)
        self._description = ttk.Label(master=self._root)
        self._texts = pydarts.gui.pregame.texts.OVERVIEW_TAB["mode"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Labelframe:
        return self._root

    def _build(self):
        self._build_root()
        self._build_name()
        self._build_separator()
        self._build_description()

    def _build_root(self):
        text: str = self._texts["title"]
        widget = self._root
        widget.configure(padding=5, text=text, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew", pady=10)
        widget.rowconfigure(index=0, weight=1)
        widget.rowconfigure(index=1, weight=1)
        widget.rowconfigure(index=2, weight=8)
        widget.columnconfigure(index=0, weight=1)

    def _build_name(self):
        widget = self._name
        widget.configure(
            padding=5, anchor="center", justify=tk.CENTER, takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")

    def _build_separator(self):
        widget = self._separator
        widget.configure(orient=tk.HORIZONTAL, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew")

    def _build_description(self):
        widget = self._description
        widget.configure(
            padding=5, anchor="center", justify=tk.CENTER, takefocus=0
        )
        widget.grid(row=2, column=0, sticky="nsew")

    def _bind(self):
        self._bind_mode_id_var()

    def _bind_mode_id_var(self):
        pydarts.gui.pregame.Vars.mode_id.trace_add(
            "write", self._handle_mode_id_write)

    def _handle_mode_id_write(self, *args, **kwargs):
        mode = metadata.Modes.get_mode(pydarts.gui.pregame.Vars.mode_id.get())
        self._name.configure(text=mode.name)
        self._description.configure(text=mode.description)


class _Players():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Labelframe(master=self._parent)
        self._view = ttk.Treeview(master=self._root)
        self._texts = pydarts.gui.pregame.texts.OVERVIEW_TAB["players"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Labelframe:
        return self._root

    def _build(self):
        self._build_root()
        self._build_view()

    def _build_root(self):
        text: str = self._texts["title"]
        widget = self._root
        widget.configure(padding=5, text=text, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew", pady=10)
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_view(self):
        texts: dict[str, str] = pydarts.gui.pregame.texts.PLAYERS_TAB["root"]["view"]["columns"]
        widget = self._view

        widget.configure(
            columns=list(texts)[1:], selectmode="none", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="player", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

    def _bind(self):
        self._bind_players_var()

    def _bind_players_var(self):
        pydarts.gui.pregame.Vars.players.trace_add(
            "write", self._handle_players_write)

    def _handle_players_write(self, *args, **kwargs):
        self._update_players_view()

    def _update_players_view(self):
        for item in self._view.get_children():
            self._view.delete(item)

        for position, player in enumerate(pydarts.gui.pregame.Vars.players.get(), start=1):
            self._view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )


class Root():
    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._mode = _Mode(parent=self._root)
        self._players = _Players(parent=self._root)
        self._start = ttk.Button(master=self._root)
        self._texts = pydarts.gui.pregame.texts.OVERVIEW_TAB["root"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Notebook:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()
        self._build_start()

    def _build_root(self):
        text: str = self._texts["title"]
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        self._parent.add(child=widget, text=text)
        widget.rowconfigure(index=0, weight=1)
        widget.rowconfigure(index=1, weight=3)
        widget.columnconfigure(index=0, weight=1)

    def _build_start(self):
        text: str = self._texts["start"]["title"]
        widget = self._start
        widget.configure(padding=5, text=text)
        widget.grid(row=2, column=0, sticky="nsew")

    def _bind(self):
        self._bind_mode_id_var()
        self._bind_players_var()
        self._bind_start()

    def _bind_mode_id_var(self):
        pydarts.gui.pregame.Vars.mode_id.trace_add(
            "write", self._handle_mode_id_write)

    def _bind_players_var(self):
        pydarts.gui.pregame.Vars.players.trace_add(
            "write", self._handle_players_write)

    def _bind_start(self):
        self._start.configure(command=self._handle_start)

    def handle_change_to_self(self, event: tk.Event = None):
        self._toggle_start()
        self._start.focus_set()
        ...

    def _handle_start(self, event: tk.Event = None):
        self._parent.update()
        self._parent.event_generate(
            sequence=pydarts.gui.pregame.Event.OVERVIEW_TAB_FINISHED.value
        )

    def _handle_mode_id_write(self, *args, **kwargs):
        self._toggle_start()

    def _handle_players_write(self, *args, **kwargs):
        self._toggle_start()

    def _toggle_start(self):
        if not pydarts.gui.pregame.Vars.mode_id.get() or not pydarts.gui.pregame.Vars.players.get():
            self._start.state(["disabled"])
        else:
            self._start.state(["!disabled"])
