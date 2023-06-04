import tkinter as tk
import tkinter.ttk as ttk

import pydarts.gui.pregame
import pydarts.gui.pregame.texts
import pydarts.gui.pregame.modes_tab
import pydarts.gui.pregame.players_tab
import pydarts.gui.pregame.overview_tab


class _Tabs():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Notebook(master=self._parent)
        self._modes_tab = pydarts.gui.pregame.modes_tab.Root(self._root)
        self._players_tab = pydarts.gui.pregame.players_tab.Root(self._root)
        self._overview_tab = pydarts.gui.pregame.overview_tab.Root(self._root)
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Notebook:
        return self._root

    def _build(self):
        self._build_root()

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _bind(self):
        self._bind_root()

    def _bind_root(self):
        widget = self._root
        widget.bind("<<NotebookTabChanged>>", self._handle_tab_changed)
        widget.bind_all(
            pydarts.gui.pregame.Event.TAB_GO_BACK_REQUESTED.value,
            self._handle_change_to_previous_tab_requested
        )
        widget.bind_all(
            pydarts.gui.pregame.Event.TAB_GO_NEXT_REQUESTED.value,
            self._handle_change_to_next_tab_requested
        )

    def _handle_change_to_previous_tab_requested(self, event: tk.Event = None) -> None:
        index: int = self._root.index("current")
        if index == 0 or self._root.index("end") == 1:
            return None
        self._change_to_tab(index-1)

    def _handle_change_to_next_tab_requested(self, event: tk.Event = None):
        index: int = self._root.index("current")
        last_index: int = self._root.index("end")-1
        if index == last_index or last_index == 0:
            return None
        self._change_to_tab(index+1)

    def _handle_tab_changed(self, event: tk.Event = None):
        index = self._root.index("current")

        if index == 0:
            pydarts.gui.pregame.Vars.is_first_tab_active.set(True)
        else:
            pydarts.gui.pregame.Vars.is_first_tab_active.set(False)

        if index == self._root.index("end")-1:
            pydarts.gui.pregame.Vars.is_last_tab_active.set(True)
        else:
            pydarts.gui.pregame.Vars.is_last_tab_active.set(False)

        tabs = [self._players_tab, self._overview_tab]
        for tab in tabs:
            if index == self._root.index(tab.root):
                tab.handle_change_to_self()
                break

    def _change_to_tab(self, index: int):
        self._root.select(index)


class _BottomBar():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._go_back = ttk.Button(master=self._root)
        self._go_next = ttk.Button(master=self._root)
        self._texts = pydarts.gui.pregame.texts.ROOT["bottom_bar"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()
        self._build_go_back()
        self._build_go_next()

    def _build_root(self):
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)

    def _build_go_back(self):
        text: str = self._texts["go_back"]["title"]
        widget = self._go_back
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsw")

    def _build_go_next(self):
        text: str = self._texts["go_next"]["title"]
        widget = self._go_next
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nse")

    def _bind(self):
        self._bind_go_back()
        self._bind_go_next()

    def _bind_is_first_tab_write(self):
        var = pydarts.gui.pregame.Vars.is_first_tab_active
        var.trace_add("write", self._handle_is_first_tab_write)

    def _bind_is_last_tab_write(self):
        var = pydarts.gui.pregame.Vars.is_last_tab_active
        var.trace_add("write", self._handle_is_last_tab_write)

    def _bind_go_back(self):
        widget = self._go_back
        widget.configure(command=self._handle_go_back)

    def _bind_go_next(self):
        widget = self._go_next
        widget.configure(command=self._handle_go_next)

    def _handle_is_first_tab_write(self, event: tk.Event = None):
        if pydarts.gui.pregame.Vars.is_first_tab_active.get():
            state = ["disabled"]
        else:
            state = ["!disabled"]
        self._go_back.state(state)

    def _handle_is_last_tab_write(self, event: tk.Event = None):
        if pydarts.gui.pregame.Vars.is_last_tab_active.get():
            state = ["disabled"]
        else:
            state = ["!disabled"]
        self._go_next.state(state)

    def _handle_go_back(self, event: tk.Event = None):
        self._go_back.event_generate(
            pydarts.gui.pregame.Event.TAB_GO_BACK_REQUESTED.value
        )

    def _handle_go_next(self, event: tk.Event = None):
        self._go_next.event_generate(
            pydarts.gui.pregame.Event.TAB_GO_NEXT_REQUESTED.value
        )


class Root():
    """Root window of pregame phase."""

    def __init__(self, parent: ttk.Frame):
        pydarts.gui.pregame.Vars.init()
        pydarts.gui.pregame.Vars.player_limit.set(8)

        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._notebook = _Tabs(parent=self._root)
        self._bottom_bar = _BottomBar(parent=self._root)
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _bind(self):
        self._bind_root()

    def _bind_root(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.OVERVIEW_TAB_FINISHED.value,
            self._handle_overview_tab_finished
        )

    def _handle_overview_tab_finished(self, event: tk.Event = None):
        self._root.event_generate(
            sequence=pydarts.gui.pregame.Event.PREGAME_WINDOW_FINISHED.value
        )
