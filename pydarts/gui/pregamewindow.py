import tkinter as tk
import tkinter.ttk as ttk

import pydarts.gui.tkhelper as tkh
from pydarts.core import games


class _Data():
    """
    tbc
    """

    def __init__(self):
        self._player_limit = 8
        self._players = tkh.ListVar()
        self._games_metadata = games.METADATA
        self._mode_id = tk.StringVar()
    
    @property
    def player_limit(self) -> int:
        return self._player_limit

    @property
    def players(self) -> tkh.ListVar:
        return self._players

    @property
    def games_metadata(self) -> games.Metadata:
        return self._games_metadata

    @property
    def mode_id(self) -> tk.StringVar:
        return self._mode_id


class ModesTab(tkh.BaseTab):
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Modus wählen",
        "view": {
            "columns": {
                "#0": "Modus",
                "description": "Beschreibung"
            }
        }
    }

    def __init__(self, data: _Data, parent: ttk.Notebook):
        super().__init__(parent)
        self.data = data

        self._view = ttk.Treeview(master=self.root)

    def build(self):
        self._build_root()
        self._build_view()

    def _build_root(self):
        text: str = ModesTab.TEXTS["title"]
        widget = self.root
        widget.configure(padding=5, takefocus=0)
        self.parent.add(child=widget, text=text)
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
    
    # [TODO]: calculate width for '#0' based on longest 'display_name'?
    def _build_view(self):
        texts: dict[str, str] = ModesTab.TEXTS["view"]["columns"]
        widget = self._view

        widget.configure(
            columns=list(texts)[1:], selectmode="browse", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="description", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

        for game in self.data._games_metadata.games:
            widget.insert(
                parent="", index=tk.END, text=game.display_name,
                values=(game.description,)
            )

    def bind(self):
        self._view.bind("<<TreeviewSelect>>", self._handle_selection)

    def handle_change_to_self(self, event: tk.Event = None):
        pass

    def _handle_selection(self, event: tk.Event = None):
        item = self._view.selection()[0]
        index = self._view.index(item)
        mode_id = self.data.games_metadata.games[index].id
        self.data.mode_id.set(mode_id)


class PlayersTab(tkh.BaseTab):
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Spieler hinzufügen",
        "prompt": {
            "label": {
                "title": "Gib einen Namen ein:"
            },
            "entry": {},
            "add": {
                "title": "Hinzufügen"
            }
        },
        "view": {
            "columns": {
                "#0": "Position",
                "player": "Spieler"
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
                "title": "Entfernen"
            }
        }
    }

    def __init__(self, data: _Data, parent: ttk.Notebook):
        super().__init__(parent)
        self.data = data

        self._prompt = ttk.Frame(master=self.root)
        self._label = ttk.Label(master=self._prompt)
        self._entry = ttk.Entry(master=self._prompt)
        self._add = ttk.Button(master=self._prompt)
        self._player_to_add = tk.StringVar()

        self.view = ttk.Treeview(master=self.root)

        self._controls = ttk.Frame(master=self.root)
        self._move_top = ttk.Button(master=self._controls)
        self._move_up = ttk.Button(master=self._controls)
        self._move_down = ttk.Button(master=self._controls)
        self._move_bottom = ttk.Button(master=self._controls)
        self._remove = ttk.Button(master=self._controls)

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
        text: str = PlayersTab.TEXTS["title"]
        widget = self.root
        widget.configure(padding=5, takefocus=0)
        self.parent.add(child=widget, text=text)
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
        text: str = PlayersTab.TEXTS["prompt"]["label"]["title"]
        widget = self._label
        widget.configure(text=text, takefocus=0)
        widget.grid(row=0, column=0, sticky="nse")

    def _build_entry(self):
        widget = self._entry
        widget.grid(row=0, column=1, sticky="nsew", padx=5)

    def _build_add(self):
        text: str = PlayersTab.TEXTS["prompt"]["add"]["title"]
        widget = self._add
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsw")

    def _build_view(self):
        texts: dict[str, str] = PlayersTab.TEXTS["view"]["columns"]
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
        text: str = PlayersTab.TEXTS["controls"]["move_top"]["title"]
        widget = self._move_top
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsew")

    def _build_move_up(self):
        text: str = PlayersTab.TEXTS["controls"]["move_up"]["title"]
        widget = self._move_up
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nsew")

    def _build_move_down(self):
        text: str = PlayersTab.TEXTS["controls"]["move_down"]["title"]
        widget = self._move_down
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsew")

    def _build_move_bottom(self):
        text: str = PlayersTab.TEXTS["controls"]["move_bottom"]["title"]
        widget = self._move_bottom
        widget.configure(text=text)
        widget.grid(row=0, column=3, sticky="nsew")

    def _build_remove(self):
        text: str = PlayersTab.TEXTS["controls"]["remove"]["title"]
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
        self.data.players.trace_add("write", self._handle_players_write)

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

    def _handle_players_write(self, *args):
        self._update_view()
        self._toggle_controls()

    def _handle_add(self, event: tk.Event = None) -> None:
        self._entry.focus_set()
        player_name = self._player_to_add.get().strip()
        self._player_to_add.set("")

        if not self._is_valid_player_name(player_name):
            # [TODO] notify user somehow
            return None

        players = self.data.players.get()
        players.append(player_name)
        self.data.players.set(players)
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
        players = self.data.players.get()
        players.pop(index)
        self.data.players.set(players)

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

        players = self.data.players.get()
        if player_name in players:
            return False

        if len(players) == self.data.player_limit:
            return False
        return True

    def _move_player(self, current_index: int, new_index: int):
        players = self.data.players.get()
        players.insert(new_index, players.pop(current_index))
        self.data.players.set(players)
        self.view.selection_set(self.view.get_children()[new_index])

    def _toggle_controls(self):
        controls = [
            control for control in vars(self).values()
            if
                isinstance(control, ttk.Button)
                and control.master is self._controls
        ]

        if len(self.data.players.get()) == 0:
            for control in controls:
                control.state(["disabled"])
        else:
            for control in controls:
                control.state(["!disabled"])

    def _update_view(self):
        for item in self.view.get_children():
            self.view.delete(item)
        for position, player in enumerate(self.data.players.get(), start=1):
            self.view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )


class OverviewTab(tkh.BaseTab):
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Spiel starten",
        "mode": {
            "title": "Modus",
        },
        "players": {
            "title": "Spieler",
            "edit": {
                "title": "Bearbeiten"
            }
        },
        "start": {
            "title": "Start!"
        }
    }

    def __init__(self, data: _Data, parent: ttk.Notebook):
        super().__init__(parent)
        self.data = data

        self._mode = ttk.Labelframe(master=self.root)
        self._mode_name_label = ttk.Label(master=self._mode)
        self._mode_separator = ttk.Separator(master=self._mode)
        self._mode_description_label = ttk.Label(master=self._mode)

        self._players = ttk.Labelframe(master=self.root)
        self._players_view = ttk.Treeview(master=self._players)

        self._start = ttk.Button(master=self.root)

    def build(self):
        self._build_root()
        self._build_mode()
        self._build_mode_name_label()
        self._build_mode_separator()
        self._build_mode_description_label()
        self._build_players()
        self._build_players_view()
        self._build_start()

    def _build_root(self):
        text: str = OverviewTab.TEXTS["title"]
        widget = self.root
        widget.configure(padding=5, takefocus=0)
        self.parent.add(child=widget, text=text)
        widget.rowconfigure(index=0, weight=1)
        widget.rowconfigure(index=1, weight=3)
        widget.columnconfigure(index=0, weight=1)

    def _build_mode(self):
        text: str = OverviewTab.TEXTS["mode"]["title"]
        widget = self._mode
        widget.configure(padding=5, text=text, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew", pady=10)
        widget.rowconfigure(index=0, weight=1)
        widget.rowconfigure(index=1, weight=1)
        widget.rowconfigure(index=2, weight=8)
        widget.columnconfigure(index=0, weight=1)

    def _build_mode_name_label(self):
        widget = self._mode_name_label
        widget.configure(
            padding=5, anchor="center", justify=tk.CENTER, takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")

    def _build_mode_separator(self):
        widget = self._mode_separator
        widget.configure(orient=tk.HORIZONTAL, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew")

    def _build_mode_description_label(self):
        widget = self._mode_description_label
        widget.configure(
            padding=5, anchor="center", justify=tk.CENTER, takefocus=0
        )
        widget.grid(row=2, column=0, sticky="nsew")

    def _build_players(self):
        text: str = OverviewTab.TEXTS["players"]["title"]
        widget = self._players
        widget.configure(padding=5, text=text, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew", pady=10)
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_players_view(self):
        texts: dict[str, str] = PlayersTab.TEXTS["view"]["columns"]
        widget = self._players_view

        widget.configure(
            columns=list(texts)[1:], selectmode="none", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="player", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

    def _build_start(self):
        text: str = OverviewTab.TEXTS["start"]["title"]
        widget = self._start
        widget.configure(padding=5, text=text)
        widget.grid(row=2, column=0, sticky="nsew")

    def bind(self):
        self._bind_mode_id_var()
        self._bind_players_var()
        self._bind_start()
    
    def _bind_mode_id_var(self):
        self.data.mode_id.trace_add("write", self._handle_mode_id_write)
        
    def _bind_players_var(self):
        self.data.players.trace_add("write", self._handle_players_write)
        
    def _bind_start(self):
        self._start.configure(command=self._handle_start)

    def handle_change_to_self(self, event: tk.Event = None):
        self._toggle_start()
        self._start.focus_set()
        ...
    
    def _handle_start(self, event: tk.Event = None):
        print(OverviewTab.TEXTS["start"]["title"])

    def _handle_mode_id_write(self, *args):
        game = self.data.games_metadata.get_game(self.data.mode_id.get())
        self._mode_name_label.configure(text=game.display_name)
        self._mode_description_label.configure(text=game.description)

    def _handle_players_write(self, *args):
        self._update_players_view()

    def _update_players_view(self):
        for item in self._players_view.get_children():
            self._players_view.delete(item)
        for position, player in enumerate(self.data.players.get(), start=1):
            self._players_view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )

    def _toggle_start(self):
        if not self.data.mode_id.get() or not self.data.players.get():
            self._start.state(["disabled"])
        else:
            self._start.state(["!disabled"])


class PregameWindow(tkh.BaseWidget):
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "go_to_previous_tab": {
            "title": "< Zurück"
        },
        "go_to_next_tab": {
            "title": "Weiter >"
        }
    }

    def __init__(self, parent: ttk.Frame):
        super().__init__(parent)
        self.data = _Data()

        self._notebook = ttk.Notebook(master=self.root)
        self._modes_tab = ModesTab(self.data, self._notebook)
        self._players_tab = PlayersTab(self.data, self._notebook)
        self._overview_tab = OverviewTab(self.data, self._notebook)

        self._bottom_bar = ttk.Frame(master=self.root)
        self._go_to_previous_tab = ttk.Button(master=self._bottom_bar)
        self._go_to_next_tab = ttk.Button(master=self._bottom_bar)

    @property
    def parent(self) -> ttk.Frame:
        return super().parent

    def build(self):
        self._build_root()
        self._build_notebook()
        self._modes_tab.build()
        self._players_tab.build()
        self._overview_tab.build()
        self._build_bottom_bar()
        self._build_go_to_previous_tab()
        self._build_go_to_next_tab()

    def _build_root(self):
        widget = self.root
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_notebook(self):
        widget = self._notebook
        widget.configure(takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
    
    def _build_bottom_bar(self):
        widget = self._bottom_bar
        widget.configure(padding=5, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)

    def _build_go_to_previous_tab(self):
        text: str = PregameWindow.TEXTS["go_to_previous_tab"]["title"]
        widget = self._go_to_previous_tab
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsw")

    def _build_go_to_next_tab(self):
        text: str = PregameWindow.TEXTS["go_to_next_tab"]["title"]
        widget = self._go_to_next_tab
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nse")

    def bind(self):
        self._bind_notebook()
        self._modes_tab.bind()
        self._players_tab.bind()
        self._overview_tab.bind()
        self._bind_go_to_previous_tab()
        self._bind_go_to_next_tab()

    def _bind_notebook(self):
        self._notebook.bind("<<NotebookTabChanged>>", self._handle_tab_changed)

    def _bind_go_to_previous_tab(self):
        widget = self._go_to_previous_tab
        widget.configure(command=self._handle_go_to_previous_tab)

    def _bind_go_to_next_tab(self):
        widget = self._go_to_next_tab
        widget.configure(command=self._handle_go_to_next_tab)

    def _handle_tab_changed(self, event: tk.Event = None):
        self._toggle_controls()
        for tab in self._get_tabs():
            if tab.is_active():
                tab.handle_change_to_self()
                break

    def _handle_go_to_previous_tab(self, event: tk.Event = None):
        self._change_to_previous_tab()

    def _handle_go_to_next_tab(self, event: tk.Event = None):
        self._change_to_next_tab()

    def _change_to_previous_tab(self) -> None:
        current_index = self._notebook.index("current")
        if current_index == 0 or len(self._notebook.tabs()) == 1:
            return None
        self._change_to_tab(current_index-1)

    def _change_to_next_tab(self) -> None:
        current_index = self._notebook.index("current")
        last_index = len(self._notebook.tabs())-1
        if current_index == last_index or last_index == 0:
            return None
        self._change_to_tab(current_index+1)

    def _change_to_tab(self, tab_id):
        self._notebook.select(tab_id)

    def _toggle_controls(self):
        index = self._notebook.index("current")

        if index == 0:
            self._go_to_previous_tab.state(["disabled"])
        else:
            self._go_to_previous_tab.state(["!disabled"])

        if index == len(self._notebook.winfo_children())-1:
            self._go_to_next_tab.state(["disabled"])
        else:
            self._go_to_next_tab.state(["!disabled"])

    def _get_tabs(self) -> list[tkh.BaseTab]:
        return [
            var
            for var in vars(self).values()
            if isinstance(var, tkh.BaseTab)
        ]
