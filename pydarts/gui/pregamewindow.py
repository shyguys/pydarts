import tkinter as tk
import tkinter.ttk as ttk
from enum import Enum

import pydarts.core.metadata as metadata
import pydarts.help.tkh as tkh


class Event(Enum):
    BOTTOM_BAR_GO_BACK_REQUESTED = "<<BottomBarGoBackRequested>>"
    BOTTOM_BAR_GO_NEXT_REQUESTED = "<<BottomBarGoNextRequested>>"
    OVERVIEW_TAB_FINISHED = "<<OverviewTabFinished>>"
    PREGAME_WINDOW_FINISHED = "<<PregameWindowFinished>>"


class _Vars():
    """
    tbc
    """

    mode_id: tk.StringVar
    player_limit: tk.IntVar
    players: tkh.ListVar
    is_first_tab_active: tk.BooleanVar
    is_last_tab_active: tk.BooleanVar

    @classmethod
    def init(cls):
        """
        Inititalizes variables. Has do be called
        after the root window has been created.
        """

        cls.mode_id = tk.StringVar()
        cls.player_limit = tk.IntVar()
        cls.players = tkh.ListVar()
        cls.is_first_tab_active = tk.BooleanVar()
        cls.is_last_tab_active = tk.BooleanVar()


class _ModesTab():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Select mode",
        "view": {
            "columns": {
                "#0": "Mode",
                "description": "Description"
            }
        }
    }

    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._view = ttk.Treeview(master=self._root)

    @property
    def parent(self) -> ttk.Notebook:
        return self._parent 

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def build(self):
        self._build_root()
        self._build_view()

    def _build_root(self):
        text: str = _ModesTab.TEXTS["title"]
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        self._parent.add(child=widget, text=text)
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
    
    # [TODO]: calculate width for '#0' based on longest 'name'?
    def _build_view(self):
        texts: dict[str, str] = _ModesTab.TEXTS["view"]["columns"]
        widget = self._view

        widget.configure(
            columns=list(texts)[1:], selectmode="browse", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="description", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

        for mode in metadata.Modes.get_modes():
            widget.insert(
                parent="", index=tk.END, text=mode.name,
                values=(mode.description,)
            )

    def bind(self):
        self._bind_view()

    def _bind_view(self):
        self._view.bind("<<TreeviewSelect>>", self._handle_selection)

    def _handle_selection(self, event: tk.Event = None):
        item = self._view.selection()[0]
        index = self._view.index(item)
        mode_id = metadata.Modes.get_modes()[index].id
        _Vars.mode_id.set(mode_id)


class _PlayersTab():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Add players",
        "prompt": {
            "label": {
                "title": "Provide a name:"
            },
            "entry": {},
            "add": {
                "title": "Add"
            }
        },
        "view": {
            "columns": {
                "#0": "Position",
                "player": "Player"
            }
        },
        "controls": {
            "move_top": {
                "title": "⊼"
            },
            "move_up": {
                "title": "∧"
            },
            "move_down": {
                "title": "∨"
            },
            "move_bottom": {
                "title": "⊻"
            },
            "remove": {
                "title": "Remove"
            }
        }
    }

    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)

        self._prompt = ttk.Frame(master=self._root)
        self._label = ttk.Label(master=self._prompt)
        self._entry = ttk.Entry(master=self._prompt)
        self._add = ttk.Button(master=self._prompt)
        self._player_to_add = tk.StringVar()

        self.view = ttk.Treeview(master=self._root)

        self._controls = ttk.Frame(master=self._root)
        self._move_top = ttk.Button(master=self._controls)
        self._move_up = ttk.Button(master=self._controls)
        self._move_down = ttk.Button(master=self._controls)
        self._move_bottom = ttk.Button(master=self._controls)
        self._remove = ttk.Button(master=self._controls)

    @property
    def parent(self) -> ttk.Notebook:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def build(self):
        self._build_root()
        self._build_prompt()
        self._build_label()
        self._build_entry()
        self._build_add()
        self._build_view()
        self._build_controls()
        self._build_move_top()
        self._build_move_up()
        self._build_move_down()
        self._build_move_bottom()
        self._build_remove()

    def _build_root(self):
        text: str = _PlayersTab.TEXTS["title"]
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        self._parent.add(child=widget, text=text)
        widget.rowconfigure(index=1, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_prompt(self):
        widget = self._prompt
        widget.configure(padding=5, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)
        widget.columnconfigure(index=2, weight=1)

    def _build_label(self):
        text: str = _PlayersTab.TEXTS["prompt"]["label"]["title"]
        widget = self._label
        widget.configure(text=text, takefocus=0)
        widget.grid(row=0, column=0, sticky="nse")

    def _build_entry(self):
        widget = self._entry
        widget.grid(row=0, column=1, sticky="nsew", padx=5)

    def _build_add(self):
        text: str = _PlayersTab.TEXTS["prompt"]["add"]["title"]
        widget = self._add
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsw")

    def _build_view(self):
        texts: dict[str, str] = _PlayersTab.TEXTS["view"]["columns"]
        widget = self.view

        widget.configure(
            columns=list(texts)[1:], selectmode="browse", takefocus=0
        )
        widget.grid(row=1, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="player", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)
    
    def _build_controls(self):
        widget = self._controls
        widget.configure(takefocus=0)
        widget.grid(row=2, column=0, sticky="nsew", pady=(5, 0))
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)
        widget.columnconfigure(index=2, weight=1)
        widget.columnconfigure(index=3, weight=1)
        widget.columnconfigure(index=4, weight=1)

    def _build_move_top(self):
        text: str = _PlayersTab.TEXTS["controls"]["move_top"]["title"]
        widget = self._move_top
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsew")

    def _build_move_up(self):
        text: str = _PlayersTab.TEXTS["controls"]["move_up"]["title"]
        widget = self._move_up
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nsew")

    def _build_move_down(self):
        text: str = _PlayersTab.TEXTS["controls"]["move_down"]["title"]
        widget = self._move_down
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsew")

    def _build_move_bottom(self):
        text: str = _PlayersTab.TEXTS["controls"]["move_bottom"]["title"]
        widget = self._move_bottom
        widget.configure(text=text)
        widget.grid(row=0, column=3, sticky="nsew")

    def _build_remove(self):
        text: str = _PlayersTab.TEXTS["controls"]["remove"]["title"]
        widget = self._remove
        widget.configure(text=text)
        widget.grid(row=0, column=4, sticky="nsew")

    def bind(self):
        self._bind_players_var()
        self._bind_entry()
        self._bind_add()
        self._bind_move_top()
        self._bind_move_up()
        self._bind_move_down()
        self._bind_move_bottom()
        self._bind_remove()

    def _bind_players_var(self):
        _Vars.players.trace_add("write", self._handle_players_write)

    def _bind_entry(self):
        self._entry.configure(textvariable=self._player_to_add)
        self._entry.bind(
            "<KeyRelease-Return>", self._handle_key_release_return_in_entry
        )
    
    def _bind_add(self):
        self._add.configure(command=self._handle_add)
    
    def _bind_move_top(self):
        self._move_top.configure(command=self._handle_move_top)
    
    def _bind_move_up(self):
        self._move_up.configure(command=self._handle_move_up)
    
    def _bind_move_down(self):
        self._move_down.configure(command=self._handle_move_down)
        
    def _bind_move_bottom(self):
        self._move_bottom.configure(command=self._handle_move_bottom)
        
    def _bind_remove(self):
        self._remove.configure(command=self._handle_remove)

    def handle_change_to_self(self, event: tk.Event = None):
        self._toggle_controls()
        self._entry.focus_set()

    def _handle_key_release_return_in_entry(self, event: tk.Event = None):
        self._add.invoke()

    def _handle_players_write(self, *args, **kwargs):
        self._update_view()
        self._toggle_controls()

    def _handle_add(self, event: tk.Event = None) -> None:
        self._entry.focus_set()
        player_name = self._player_to_add.get().strip()
        self._player_to_add.set("")

        if not self._is_valid_player_name(player_name):
            # [TODO] notify user somehow
            return None

        players = _Vars.players.get()
        players.append(player_name)
        _Vars.players.set(players)
        return None

    def _handle_move_top(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        index = self.view.index(self.view.selection()[0])
        if index == 0:
            return None

        self._move_player(index, 0)
        return None

    def _handle_move_up(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        index = self.view.index(self.view.selection()[0])
        if index == 0:
            return None

        self._move_player(index, index-1)
        return None

    def _handle_move_down(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        index = self.view.index(self.view.selection()[0])
        if index == len(self.view.get_children())-1:
            return None

        self._move_player(index, index+1)
        return None

    def _handle_move_bottom(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        index = self.view.index(self.view.selection()[0])
        last_index = len(self.view.get_children())-1
        if index == last_index:
            return None

        self._move_player(index, last_index)
        return None

    def _handle_remove(self, event: tk.Event = None) -> None:
        selection = self.view.selection()
        if not selection:
            return None

        index = self.view.index(self.view.selection()[0])
        players = _Vars.players.get()
        players.pop(index)
        _Vars.players.set(players)

        if not self.view.get_children():
            self._entry.focus_set()
            return None
        
        if index == len(self.view.get_children()):
            new_index = index-1
        else:
            new_index = index

        self.view.selection_set(self.view.get_children()[new_index])
        return None

    def _is_valid_player_name(self, player_name: str) -> bool:
        if not player_name:
            return False

        players = _Vars.players.get()
        if player_name in players:
            return False

        if len(players) == _Vars.player_limit.get():
            return False
        return True

    def _move_player(self, current_index: int, new_index: int):
        players = _Vars.players.get()
        players.insert(new_index, players.pop(current_index))
        _Vars.players.set(players)
        self.view.selection_set(self.view.get_children()[new_index])

    def _toggle_controls(self):
        controls = [
            control for control in vars(self).values()
            if
                isinstance(control, ttk.Button)
                and control.master is self._controls
        ]

        if len(_Vars.players.get()) == 0:
            for control in controls:
                control.state(["disabled"])
        else:
            for control in controls:
                control.state(["!disabled"])

    def _update_view(self):
        for item in self.view.get_children():
            self.view.delete(item)

        for position, player in enumerate(_Vars.players.get(), start=1):
            self.view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )


class _ModeOverview():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Mode",
    }

    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Labelframe(master=self._parent)
        self._name = ttk.Label(master=self._root)
        self._separator = ttk.Separator(master=self._root)
        self._description = ttk.Label(master=self._root)

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Labelframe:
        return self._root

    def build(self):
        self._build_root()
        self._build_name()
        self._build_separator()
        self._build_description()

    def _build_root(self):
        text: str = _ModeOverview.TEXTS["title"]
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

    def bind(self):
        self._bind_mode_id_var()

    def _bind_mode_id_var(self):
        _Vars.mode_id.trace_add("write", self._handle_mode_id_write)
    
    def _handle_mode_id_write(self, *args, **kwargs):
        mode = metadata.Modes.get_mode(_Vars.mode_id.get())
        self._name.configure(text=mode.name)
        self._description.configure(text=mode.description)


class _PlayersOverview():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Players"
    }

    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Labelframe(master=self._parent)
        self._view = ttk.Treeview(master=self._root)

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Labelframe:
        return self._root

    def build(self):
        self._build_root()
        self._build_view()

    def _build_root(self):
        text: str = _PlayersOverview.TEXTS["title"]
        widget = self._root
        widget.configure(padding=5, text=text, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew", pady=10)
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_view(self):
        texts: dict[str, str] = _PlayersTab.TEXTS["view"]["columns"]
        widget = self._view

        widget.configure(
            columns=list(texts)[1:], selectmode="none", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="player", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

    def bind(self):
        self._bind_players_var()
        
    def _bind_players_var(self):
        _Vars.players.trace_add("write", self._handle_players_write)

    def _handle_players_write(self, *args, **kwargs):
        self._update_players_view()

    def _update_players_view(self):
        for item in self._view.get_children():
            self._view.delete(item)

        for position, player in enumerate(_Vars.players.get(), start=1):
            self._view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )


class _OverviewTab():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Start",
        "start": {
            "title": "Start!"
        }
    }

    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._mode = _ModeOverview(parent=self._root)
        self._players = _PlayersOverview(parent=self._root)
        self._start = ttk.Button(master=self._root)

    @property
    def parent(self) -> ttk.Notebook:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def build(self):
        self._build_root()
        self._mode.build()
        self._players.build()
        self._build_start()

    def _build_root(self):
        text: str = _OverviewTab.TEXTS["title"]
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        self._parent.add(child=widget, text=text)
        widget.rowconfigure(index=0, weight=1)
        widget.rowconfigure(index=1, weight=3)
        widget.columnconfigure(index=0, weight=1)

    def _build_start(self):
        text: str = _OverviewTab.TEXTS["start"]["title"]
        widget = self._start
        widget.configure(padding=5, text=text)
        widget.grid(row=2, column=0, sticky="nsew")

    def bind(self):
        self._mode.bind()
        self._players.bind()
        self._bind_mode_id_var()
        self._bind_players_var()
        self._bind_start()

    def _bind_mode_id_var(self):
        _Vars.mode_id.trace_add("write", self._handle_mode_id_write)
        
    def _bind_players_var(self):
        _Vars.players.trace_add("write", self._handle_players_write)
        
    def _bind_start(self):
        self._start.configure(command=self._handle_start)

    def handle_change_to_self(self, event: tk.Event = None):
        self._toggle_start()
        self._start.focus_set()
        ...
    
    def _handle_start(self, event: tk.Event = None):
        self._parent.update()
        self._parent.event_generate(
            sequence=Event.OVERVIEW_TAB_FINISHED.value
        )

    def _handle_mode_id_write(self, *args, **kwargs):
        self._toggle_start()

    def _handle_players_write(self, *args, **kwargs):
        self._toggle_start()

    def _toggle_start(self):
        if not _Vars.mode_id.get() or not _Vars.players.get():
            self._start.state(["disabled"])
        else:
            self._start.state(["!disabled"])


class _Notebook():
    def __init__(self, parent: ttk.Frame):       
        self._parent = parent
        self._root = ttk.Notebook(master=self._parent)
        self._modes_tab = _ModesTab(self._root)
        self._players_tab = _PlayersTab(self._root)
        self._overview_tab = _OverviewTab(self._root)

    @property
    def parent(self) -> ttk.Frame:
        return self._parent
    
    @property
    def root(self) -> ttk.Notebook:
        return self._root

    def build(self):
        self._build_root()
        self._modes_tab.build()
        self._players_tab.build()
        self._overview_tab.build()

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def bind(self):
        self._bind_root()
        self._modes_tab.bind()
        self._players_tab.bind()
        self._overview_tab.bind()

    def _bind_root(self):
        widget = self._root
        widget.bind("<<NotebookTabChanged>>", self._handle_tab_changed)
        widget.bind_all(
            Event.BOTTOM_BAR_GO_BACK_REQUESTED.value,
            self._handle_change_to_previous_tab_requested
        )
        widget.bind_all(
            Event.BOTTOM_BAR_GO_NEXT_REQUESTED.value,
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
            _Vars.is_first_tab_active.set(True)
        else:
            _Vars.is_first_tab_active.set(False)

        if index == self._root.index("end")-1:
            _Vars.is_last_tab_active.set(True)
        else:
            _Vars.is_last_tab_active.set(False)
        
        tabs = [self._players_tab, self._overview_tab]
        for tab in tabs:
            if index == self._root.index(tab.root):
                tab.handle_change_to_self()
                break

    def _change_to_tab(self, index: int):
        self._root.select(index)

class _BottomBar():
    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "go_back": {
            "title": "< Back"
        },
        "go_next": {
            "title": "Next >"
        }
    }

    def __init__(self, parent: ttk.Frame):     
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._go_back = ttk.Button(master=self._root)
        self._go_next = ttk.Button(master=self._root)

    @property
    def parent(self) -> ttk.Frame:
        return self._parent
    
    @property
    def root(self) -> ttk.Frame:
        return self._root

    def build(self):
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
        text: str = _BottomBar.TEXTS["go_back"]["title"]
        widget = self._go_back
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsw")

    def _build_go_next(self):
        text: str = _BottomBar.TEXTS["go_next"]["title"]
        widget = self._go_next
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nse")

    def bind(self):
        self._bind_go_back()
        self._bind_go_next()

    def _bind_is_first_tab_write(self):
        var = _Vars.is_first_tab_active
        var.trace_add("write", self._handle_is_first_tab_write)

    def _bind_is_last_tab_write(self):
        var = _Vars.is_last_tab_active
        var.trace_add("write", self._handle_is_last_tab_write)

    def _bind_go_back(self):
        widget = self._go_back
        widget.configure(command=self._handle_go_back)

    def _bind_go_next(self):
        widget = self._go_next
        widget.configure(command=self._handle_go_next)

    def _handle_is_first_tab_write(self, event: tk.Event = None):
        if _Vars.is_first_tab_active.get():
            state = ["disabled"]
        else:
            state = ["!disabled"]
        self._go_back.state(state)

    def _handle_is_last_tab_write(self, event: tk.Event = None):
        if _Vars.is_last_tab_active.get():
            state = ["disabled"]
        else:
            state = ["!disabled"]
        self._go_next.state(state)

    def _handle_go_back(self, event: tk.Event = None):
        self._go_back.event_generate(
            Event.BOTTOM_BAR_GO_BACK_REQUESTED.value
        )

    def _handle_go_next(self, event: tk.Event = None):
        self._go_next.event_generate(
            Event.BOTTOM_BAR_GO_NEXT_REQUESTED.value
        )


class PregameWindow():
    """
    tbc
    """

    def __init__(self, parent: ttk.Frame):
        _Vars.init()
        _Vars.player_limit.set(8)

        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._notebook = _Notebook(parent=self._root)
        self._bottom_bar = _BottomBar(parent=self._root)

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root 

    def build(self):
        self._build_root()
        self._notebook.build()
        self._bottom_bar.build()

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def bind(self):
        self._bind_root()
        self._notebook.bind()
        self._bottom_bar.bind()

    def _bind_root(self):
        self._root.bind_all(
            Event.OVERVIEW_TAB_FINISHED.value,
            self._handle_overview_tab_finished
        )

    def _handle_overview_tab_finished(self, event: tk.Event = None):
        self._root.event_generate(
            sequence=Event.PREGAME_WINDOW_FINISHED.value
        )
