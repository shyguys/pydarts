import tkinter as tk
import tkinter.ttk as ttk

import modules.games as games
import modules.tkhelper as tkh


class PregameWindow():
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

    # Temporary, to be defined somewhere/-how else once I know a better way.
    PLAYER_LIMIT = 8

    def __init__(self, parent = tk.Tk):
        self.parent = parent
        self.root = self.build_root()
        self.notebook = self.build_notebook()
        self.modes_tab = ModesTab(parent=self)
        self.players_tab = PlayersTab(parent=self)
        self.overview_tab = OverviewTab(parent=self)
        self.bottom_bar = self.build_bottom_bar()
        self.go_to_previous_tab = self.build_go_to_previous_tab()
        self.go_to_next_tab = self.build_go_to_next_tab()

    def build_root(self) -> ttk.Frame:
        widget = ttk.Frame(master=self.parent, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        return widget

    def build_notebook(self) -> ttk.Notebook:
        widget = ttk.Notebook(master=self.root, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        return widget
    
    def build_bottom_bar(self) -> ttk.Frame:
        widget = ttk.Frame(master=self.root, padding=5, takefocus=0)
        widget.grid(row=1, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)
        return widget

    def build_go_to_previous_tab(self) -> ttk.Button:
        text = PregameWindow.TEXTS["go_to_previous_tab"]["title"]
        widget = ttk.Button(master=self.bottom_bar, text=text)
        widget.grid(row=0, column=0, sticky="nsw")
        return widget

    def build_go_to_next_tab(self) -> ttk.Button:
        text = PregameWindow.TEXTS["go_to_next_tab"]["title"]
        widget = ttk.Button(master=self.bottom_bar, text=text)
        widget.grid(row=0, column=1, sticky="nse")
        return widget

    def build(self):
        self.modes_tab.build()
        self.players_tab.build()
        self.overview_tab.build()

    def bind(self):
        self.bind_root()
        self.bind_go_to_previous_tab()
        self.bind_go_to_next_tab()
        self.modes_tab.bind()
        self.players_tab.bind()
        self.overview_tab.bind()

    def bind_root(self):
        self.root.bind("<<NotebookTabChanged>>", self.handle_tab_changed)

    def bind_go_to_previous_tab(self):
        widget = self.go_to_previous_tab
        widget.configure(command=self.handle_go_to_previous_tab)

    def bind_go_to_next_tab(self):
        widget = self.go_to_next_tab
        widget.configure(command=self.handle_go_to_next_tab)

    def handle_tab_changed(self, event: tk.Event = None) -> None:
        current_tab_index = self.notebook.index("current")
        if current_tab_index == self.notebook.index(self.modes_tab.root):
            self.modes_tab.handle_change_to_self(event)
            return None
        if current_tab_index == self.notebook(self.players_tab.root):
            self.players_tab.handle_change_to_self(event)
            return None
        if current_tab_index == self.notebook(self.overview_tab.root):
            self.overview_tab.handle_change_to_self(event)
            return None

    def handle_go_to_previous_tab(self, event: tk.Event = None):
        self.change_to_previous_tab()

    def handle_go_to_next_tab(self, event: tk.Event = None):
        self.change_to_next_tab()

    def change_to_previous_tab(self) -> None:
        current_index = self.notebook.index("current")
        if current_index == 0 or len(self.notebook.tabs()) == 1:
            return None
        self.change_to_tab(current_index-1)

    def change_to_next_tab(self) -> None:
        current_index = self.notebook.index("current")
        last_index = len(self.notebook.tabs())-1
        if current_index == last_index or last_index == 0:
            return None
        self.change_to_tab(current_index+1)

    def change_to_tab(self, tab_id):
        self.notebook.select(tab_id)

    # [TODO]: define BaseTab
    # def get_tabs(self):
    #     return [self.modes_tab, self.players_tab, self.overview_tab]


class ModesTab():
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Modus wählen",
        "columns": {
            "#0": "Modus",
            "description": "Beschreibung"
        }
    }

    def __init__(self, parent: PregameWindow):
        self.parent = parent
        self.root: ttk.Frame = None
        self.content: ttk.Frame = None
        self.view: ttk.Treeview = None
        self.selected_mode: str = None

    def build(self):
        self.build_root()
        self.build_content()
        self.build_view()

    def build_root(self):
        text = ModesTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent.notebook, padding=5, takefocus=0)
        self.parent.notebook.add(child=self.root, text=text)
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)

    def build_content(self):
        self.content = ttk.Frame(master=self.root, takefocus=0)
        self.content.grid(row=0, column=0, sticky="nsew")
        self.content.rowconfigure(index=0, weight=1)
        self.content.columnconfigure(index=0, weight=1)  
    
    # [TODO]: calculate width for '#0' based on longest 'display_name'?
    def build_view(self):
        texts: dict[str, dict[str, str]] = ModesTab.TEXTS["columns"]
        self.view = ttk.Treeview(
            master=self.content, columns=list(texts.keys())[1:],
            selectmode="browse"
        )
        self.view.grid(row=0, column=0, sticky="nsew")
        self.view.column(column="#0", stretch=tk.NO)
        self.view.column(column="description", anchor="w")
        for key, value in texts.items():
            self.view.heading(column=key, text=value)
        for game in games.METADATA.games:
            self.view.insert(
                parent="", index=tk.END, text=game.display_name,
                values=(game.description,)
            )

    def bind(self):
        self.bind_root()
        self.bind_view()

    def bind_root(self):
        tkh.bind_children(
            self.root, "<KeyRelease-Up>", self.handle_key_release_up,
            [self.view]
        )
        tkh.bind_children(
            self.root, "<KeyRelease-Down>", self.handle_key_release_down,
            [self.view]
        )

    def bind_view(self):
        self.view.bind("<<TreeviewSelect>>", self.handle_selection)

    def handle_change_to_self(self, event: tk.Event = None):
        ...

    def handle_key_release_down(self, event: tk.Event = None):
        """
        Interpret DOWN as if it was RELEASED inside the view, i.e. select the
        next item. Focus remains on the widget that caught this event.
        """
        children = self.view.get_children()
        selected_items = self.view.selection()
        if not selected_items:
            self.view.selection_set(children[0])
            return None

        selected_item = selected_items[0]
        index = self.view.index(selected_item)
        if index != self.view.index(children[-1]):
            self.view.selection_set(children[index+1])
        return None

    def handle_key_release_up(self, event: tk.Event = None) -> None:
        """
        Interpret UP as if it was RELEASED inside the view, i.e. select the
        previous item. Focus remains on the widget that caught this event.
        """
        children = self.view.get_children()
        selected_items = self.view.selection()
        if not selected_items:
            self.view.selection_set(children[-1])
            return None

        selected_item = selected_items[0]
        index = self.view.index(selected_item)
        if index != 0:
            self.view.selection_set(children[index-1])
        return None

    def handle_selection(self, event: tk.Event = None):
        """
        Save the new selection.
        """
        self.selected_mode = self.view.item(
            self.view.selection()[0], option="text"
        )

    def handle_goto_players_tab(self):
        self.parent.change_to_tab(self.parent.players_tab.root)


class PlayersTab():
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Spieler hinzufügen",
        "prompt": {
            "label": "Gib einen Namen ein:",
            "entry": "",
            "add": "Hinzufügen"
        },
        "columns": {
            "#0": "Position",
            "player": "Spieler"
        },
        "controls": {
            "move_top": "⊼",
            "move_up": "∧",
            "move_down": "∨",
            "move_bottom": "⊻",
            "remove": "Entfernen"
        }
    }

    def __init__(self, parent: PregameWindow):
        self.parent = parent
        self.root: ttk.Frame = None
        self.content: ttk.Frame = None
        self.prompt: ttk.Frame = None
        self.label: ttk.Label = None
        self.entry: ttk.Entry = None
        self.player_to_add = tk.StringVar()
        self.add: ttk.Button = None
        self.view: ttk.Treeview = None
        self.controls: ttk.Frame = None
        self.move_top: ttk.Button = None
        self.move_up: ttk.Button = None
        self.move_down: ttk.Button = None
        self.move_bottom: ttk.Button = None
        self.remove: ttk.Button = None
        self.players: list[str] = []
        self.selected_player: str = None

    def build(self):
        self.build_root()
        self.build_content()
        self.build_prompt()
        self.build_label()
        self.build_entry()
        self.build_add()
        self.build_view()
        self.build_controls()
        self.build_move_top()
        self.build_move_up()
        self.build_move_down()
        self.build_move_bottom()
        self.build_remove()

    def build_root(self):
        text = PlayersTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent.notebook, padding=5, takefocus=0)
        self.parent.notebook.add(child=self.root, text=text)
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)

    def build_content(self):
        self.content = ttk.Frame(master=self.root, takefocus=0)
        self.content.grid(row=0, column=0, sticky="nsew")
        self.content.columnconfigure(index=0, weight=1)
        self.content.rowconfigure(index=1, weight=1)

    def build_prompt(self):
        self.prompt = ttk.Frame(master=self.content, padding=5, takefocus=0)
        self.prompt.grid(row=0, column=0, sticky="nsew")
        self.prompt.rowconfigure(index=0, weight=1)
        self.prompt.columnconfigure(index=0, weight=1)
        self.prompt.columnconfigure(index=1, weight=2)
        self.prompt.columnconfigure(index=2, weight=1)

    def build_label(self):
        text = PlayersTab.TEXTS["prompt"]["label"]
        self.label = ttk.Label(master=self.prompt, text=text, takefocus=0)
        self.label.grid(row=0, column=0, sticky="nse")

    def build_entry(self):
        self.entry = ttk.Entry(master=self.prompt)
        self.entry.grid(row=0, column=1, sticky="nsew", padx=5)

    def build_add(self):
        text = PlayersTab.TEXTS["prompt"]["add"]
        self.add = ttk.Button(master=self.prompt, text=text)
        self.add.grid(row=0, column=2, sticky="nsw")

    def build_view(self):
        texts: dict[str, dict[str, str]] = PlayersTab.TEXTS["columns"]
        self.view = ttk.Treeview(
            master=self.content, columns=["player"], selectmode="browse"
        )
        self.view.grid(row=1, column=0, sticky="nsew")
        self.view.column(column="#0", stretch=tk.NO)
        self.view.column(column="player", anchor="w")
        for key, value in texts.items():
            self.view.heading(column=key, text=value)
    
    def build_controls(self):
        self.controls = ttk.Frame(master=self.content, padding=(0, 5, 0, 0), takefocus=0)
        self.controls.grid(row=2, column=0, sticky="nsew")
        self.controls.rowconfigure(index=0, weight=1)
        self.controls.columnconfigure(index=0, weight=1)
        self.controls.columnconfigure(index=1, weight=1)
        self.controls.columnconfigure(index=2, weight=1)
        self.controls.columnconfigure(index=3, weight=1)
        self.controls.columnconfigure(index=4, weight=1)

    def build_move_top(self):
        text: str = PlayersTab.TEXTS["controls"]["move_top"]
        self.move_top = ttk.Button(master=self.controls, text=text)
        self.move_top.grid(row=0, column=0, sticky="nsew")

    def build_move_up(self):
        text: str = PlayersTab.TEXTS["controls"]["move_up"]
        self.move_up = ttk.Button(master=self.controls, text=text)
        self.move_up.grid(row=0, column=1, sticky="nsew")

    def build_move_down(self):
        text: str = PlayersTab.TEXTS["controls"]["move_down"]
        self.move_down = ttk.Button(master=self.controls, text=text)
        self.move_down.grid(row=0, column=2, sticky="nsew")

    def build_move_bottom(self):
        text: str = PlayersTab.TEXTS["controls"]["move_bottom"]
        self.move_bottom = ttk.Button(master=self.controls, text=text)
        self.move_bottom.grid(row=0, column=3, sticky="nsew")

    def build_remove(self):
        text: str = PlayersTab.TEXTS["controls"]["remove"]
        self.remove = ttk.Button(master=self.controls, text=text)
        self.remove.grid(row=0, column=4, sticky="nsew")

    def bind(self):
        self.bind_root()
        self.bind_entry()
        self.bind_add()
        self.bind_view()
        self.bind_move_top()
        self.bind_move_up()
        self.bind_move_down()
        self.bind_move_bottom()
        self.bind_remove()

    def bind_root(self):
        tkh.bind_children(
            self.root, "<KeyRelease-Up>", self.handle_key_release_up,
            [self.view]
        )
        self.root.bind
        tkh.bind_children(
            self.root, "<KeyRelease-Down>", self.handle_key_release_down,
            [self.view]
        )
        tkh.bind_children(
            self.root, "<Shift-Control-KeyRelease-Up>",
            self.handle_shift_control_key_release_up, [self.view]
        )
        tkh.bind_children(
            self.root, "<Control-KeyRelease-Up>",
            self.handle_control_key_release_up, [self.view]
        )
        tkh.bind_children(
            self.root, "<Control-KeyRelease-Down>",
            self.handle_control_key_release_down, [self.view]
        )
        tkh.bind_children(
            self.root, "<Shift-Control-KeyRelease-Down>",
            self.handle_shift_control_key_release_down, [self.view]
        )
        tkh.bind_children(
            self.root, "<Control-KeyRelease-Delete>",
            self.handle_control_key_release_delete, [self.view]
        )

    def bind_entry(self):
        self.entry.configure(textvariable=self.player_to_add)
        self.entry.bind(
            "<KeyRelease-Return>", self.handle_key_release_return_in_entry
        )

    def bind_add(self):
        self.add.configure(command=self.handle_add)

    # [TODO]: bind losing focus
    def bind_view(self):
        self.view.bind("<<TreeviewSelect>>", self.handle_selection)

    def bind_move_top(self):
        self.move_top.configure(command=self.handle_move_top)

    def bind_move_up(self):
        self.move_up.configure(command=self.handle_move_up)

    def bind_move_down(self):
        self.move_down.configure(command=self.handle_move_down)

    def bind_move_bottom(self):
        self.move_bottom.configure(command=self.handle_move_bottom)

    def bind_remove(self):
        self.remove.configure(command=self.handle_remove)

    def handle_change_to_self(self, event: tk.Event = None):
        """
        Focus on the player entry.
        """
        self.entry.focus_set()

    def handle_key_release_up(self, event: tk.Event = None) -> None:
        """
        Interpret UP as if it was RELEASED inside the view, i.e. select the
        previous item. Focus remains on the widget that caught this event.
        """
        children = self.view.get_children()
        if not children:
            return None

        selected_items = self.view.selection()
        if not selected_items:
            self.view.selection_set(children[-1])
            return None

        selected_item = selected_items[0]
        index = self.view.index(selected_item)
        if index != 0:
            self.view.selection_set(children[index-1])
        return None

    def handle_key_release_down(self, event: tk.Event = None):
        """
        Interpret DOWN as if it was RELEASED inside the view, i.e. select the
        next item. Focus remains on the widget that caught this event.
        """
        children = self.view.get_children()
        if not children:
            return None
        
        selected_items = self.view.selection()
        if not selected_items:
            self.view.selection_set(children[0])
            return None

        selected_item = selected_items[0]
        index = self.view.index(selected_item)
        if index != self.view.index(children[-1]):
            self.view.selection_set(children[index+1])
        return None

    def handle_shift_control_key_release_up(self, event: tk.Event = None):
        self.move_top.invoke()

    def handle_control_key_release_up(self, event: tk.Event = None):
        self.move_up.invoke()

    def handle_control_key_release_down(self, event: tk.Event = None):
        self.move_down.invoke()

    def handle_shift_control_key_release_down(self, event: tk.Event = None):
        self.move_bottom.invoke()

    def handle_control_key_release_delete(self, event: tk.Event = None):
        self.remove.invoke()

    def handle_add(self, event: tk.Event = None) -> None:
        self.entry.focus_set()
        player_name = self.player_to_add.get().strip()
        self.player_to_add.set("")
        if not self.is_valid_player_name(player_name):
            # [TODO] notify user somehow
            return None
        self.players.append(player_name)
        self.update_view()
        self.view.selection_set(self.view.get_children()[-1])
        return None

    def handle_key_release_return_in_entry(self, event: tk.Event = None):
        self.add.invoke()

    def handle_selection(self, event: tk.Event = None) -> None:
        selection = self.view.selection()
        if not selection:
            self.selected_player = None
            return None
        
        self.selected_player = self.view.item(selection[0], option="text")
        return None

    def handle_move_top(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        selected_item = self.view.selection()[0]
        if selected_item == self.view.get_children()[0]:
            return None

        selected_index = self.view.index(selected_item)
        self.players.insert(0, self.players.pop(selected_index))
        self.update_view()
        self.view.selection_set(self.view.get_children()[0])
        return None

    def handle_move_up(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        selected_item = self.view.selection()[0]
        if selected_item == self.view.get_children()[0]:
            return None

        selected_index = self.view.index(selected_item)
        new_index = selected_index-1
        self.players.insert(new_index, self.players.pop(selected_index))
        self.update_view()
        self.view.selection_set(self.view.get_children()[new_index])
        return None

    def handle_move_down(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        selected_item = self.view.selection()[0]
        if selected_item == self.view.get_children()[-1]:
            return None

        selected_index = self.view.index(selected_item)
        new_index = selected_index+1
        self.players.insert(new_index, self.players.pop(selected_index))
        self.update_view()
        self.view.selection_set(self.view.get_children()[new_index])
        return None

    def handle_move_bottom(self, event: tk.Event = None):
        selection = self.view.selection()
        if not selection:
            return None

        selected_item = self.view.selection()[0]
        if selected_item == self.view.get_children()[-1]:
            return None

        self.players.append(self.players.pop(self.view.index(selected_item)))
        self.update_view()
        self.view.selection_set(self.view.get_children()[-1])
        return None

    def handle_remove(self, event: tk.Event = None) -> None:
        selection = self.view.selection()
        if not selection:
            return None

        selected_item = self.view.selection()[0]
        selected_index = self.view.index(selected_item)
        self.players.pop(selected_index)
        self.update_view()

        if not self.view.get_children():
            return None
        
        new_index = selected_index
        if new_index > len(self.view.get_children())-1:
            new_index = new_index-1
        self.view.selection_set(self.view.get_children()[new_index])

    def is_valid_player_name(self, player_name: str) -> bool:
        if not player_name:
            return False
        if player_name in self.players:
            return False
        if len(self.players) == PregameWindow.PLAYER_LIMIT:
            return False
        return True

    def update_view(self):
        for item in self.view.get_children():
            self.view.delete(item)
        for position, player in enumerate(self.players, start=1):
            self.view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )


class OverviewTab():
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Spiel starten",
        "mode": {
            "title": "Modus",
            "edit": "Bearbeiten"
        },
        "players": {
            "title": "Spieler",
            "edit": "Bearbeiten"
        }
    }

    def __init__(self, parent: PregameWindow):
        self.parent = parent
        self.root: ttk.Frame = None
        self.content: ttk.Frame = None
        self.mode: ttk.Labelframe = None
        self.players: ttk.Labelframe = None
        self.players_view: ttk.Treeview = None
        self.players_edit: ttk.Button = None

    def build(self):
        self.build_root()
        self.build_content()
        self.build_mode()
        self.build_players()
        self.build_players_view()
        self.build_players_edit()

    def build_root(self):
        text = OverviewTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent.notebook, padding=5, takefocus=0)
        self.parent.notebook.add(child=self.root, text=text)
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)

    def build_content(self):
        self.content = ttk.Frame(master=self.root, padding=5, takefocus=0)
        self.content.grid(row=0, column=0, sticky="nsew")
        self.content.rowconfigure(index=0, weight=1)
        self.content.rowconfigure(index=1, weight=1)
        self.content.columnconfigure(index=0, weight=1)

    def build_mode(self):
        text = OverviewTab.TEXTS["mode"]["title"]
        self.mode = ttk.Labelframe(
            master=self.content, padding=5, text=text, takefocus=0
        )
        self.mode.grid(row=0, column=0, sticky="nsew")

    def build_players(self):
        text = OverviewTab.TEXTS["players"]["title"]
        self.players = ttk.Labelframe(
            master=self.content, padding=5, text=text, takefocus=0
        )
        self.players.grid(row=1, column=0, sticky="nsew")

    def build_players_view(self):
        ...
    
    def build_players_edit(self):
        ...

    def bind(self):
        self.bind_root()

    def bind_root(self):
        ...

    def handle_change_to_self(self, event: tk.Event = None):
        ...

    # def _configure_overview_tab(self):
    #     self.root.hide(tab_id=self.overview_tab)
    #     self.overview_tab_goto_players_tab.configure(
    #         command=self._handle_overview_tab_goto_players_tab
    #     )
    #     self.overview_tab_start_game.configure(
    #         command=self._handle_overview_tab_start_game
    #     )

    # def _handle_overview_tab_goto_players_tab(self):
    #     self._goto_players_tab()

    # def _handle_overview_tab_start_game(self):
    #     self._start_game()

    # def _goto_players_tab(self):
    #     self.root.select(tab_id=self.players_tab)

    # def _start_game(self):
    #     print("Start!")
