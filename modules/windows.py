import tkinter as tk
import tkinter.ttk as ttk

import modules.games as games


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
        },
        "goto_players_tab": "Weiter >"
    }

    def __init__(self, notebook: ttk.Notebook):
        self.parent = notebook
        self.root: ttk.Frame = None
        self.content: ttk.Frame = None
        self.view: ttk.Treeview = None
        self.bottom_bar: ttk.Frame = None
        self.goto_players_tab: ttk.Button = None
        self.mode: str = None

        self.build()
        self.configure()

    def build(self):
        text = ModesTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent, padding=5)
        self.parent.add(child=self.root, text=text)
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)
        self.build_content()
        self.build_bottom_bar()

    def build_content(self):
        self.content = ttk.Frame(master=self.root, padding=5)
        self.content.grid(row=0, column=0, sticky="nsew")
        self.content.rowconfigure(index=0, weight=1)
        self.content.columnconfigure(index=0, weight=1)
        self.build_view()
    
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

    def build_bottom_bar(self):
        self.bottom_bar = ttk.Frame(master=self.root, padding=5)
        self.bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.bottom_bar.rowconfigure(index=0, weight=1)
        self.bottom_bar.columnconfigure(index=0, weight=1)
        self.build_goto_players_tab()

    def build_goto_players_tab(self):
        text = ModesTab.TEXTS["goto_players_tab"]
        self.goto_players_tab = ttk.Button(master=self.bottom_bar, text=text)
        self.goto_players_tab.grid(row=0, column=0, sticky="nse")

    def configure(self):
        ...

    # def _configure_mode_tab(self):
    #     self._configure_mode_tab_content()
    #     self._configure_mode_tab_bottom_bar()

    # def _configure_mode_tab_content(self):
    #     self._configure_mode_tab_selection()

    # def _configure_mode_tab_selection(self):
    #     self.mode_tab_selection.bind(
    #         "<<TreeviewSelect>>", lambda e: self._handle_mode_tab_selection()
    #     )

    # def _configure_mode_tab_bottom_bar(self):
    #     self._configure_mode_tab_goto_players_tab()

    # def _configure_mode_tab_goto_players_tab(self):
    #     self.mode_tab_goto_players_tab.state(["disabled"])
    #     self.mode_tab_goto_players_tab.configure(
    #         command=self._handle_mode_tab_goto_players_tab
    #     )

    # def _handle_mode_tab(self):
    #     print(self.mode_tab_selection.selection())
    #     ...

    # def _handle_mode_tab_selection(self):
    #     self.mode = self.mode_tab_selection.item(
    #         item=self.mode_tab_selection.selection()[0], option="text"
    #     )
    #     self.root.add(child=self.players_tab)
    #     self.mode_tab_goto_players_tab.state(["!disabled"])

    # def _handle_mode_tab_goto_players_tab(self):
    #     self._goto_players_tab()

    # def _goto_players_tab(self):
    #     self.root.select(tab_id=self.players_tab)

    ...

# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #

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
            "delete": "Löschen"
        },
        "goto_mode_tab": "< Zurück",
        "goto_overview_tab": "Weiter >"
    }

    def __init__(self, notebook: ttk.Notebook):
        self.parent = notebook
        self.root: ttk.Frame = None
        # self.player_to_add: tk.StringVar = tk.StringVar()
        # self.players: list[str] = []
        # self.players_tab: ttk.Frame = None
        # self.players_tab_content: ttk.Frame = None
        # self.players_tab_prompt: ttk.Frame = None
        # self.players_tab_prompt_label: ttk.Label = None
        # self.players_tab_prompt_entry: ttk.Entry = None
        # self.players_tab_prompt_add: ttk.Button = None
        # self.players_tab_players: ttk.Frame = None
        # self.players_tab_players_view: ttk.Treeview = None
        # self.players_tab_controls: ttk.Frame = None
        # self.players_tab_controls_move_top: ttk.Button = None
        # self.players_tab_controls_move_up: ttk.Button = None
        # self.players_tab_controls_move_down: ttk.Button = None
        # self.players_tab_controls_move_bottom: ttk.Button = None
        # self.players_tab_controls_delete: ttk.Button = None
        # self.players_tab_bottom_bar: ttk.Frame = None
        # self.players_tab_goto_mode_tab: ttk.Button = None
        # self.players_tab_goto_overview_tab: ttk.Button = None

        self.build()
        self.configure()

    def build(self):
        text = PlayersTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent, padding=5)
        self.parent.add(child=self.root, text=text)
        ...

    # def _build_players_tab(self, parent: ttk.Notebook):
    #     text = PregameWindow.TEXTS["players"]["title"]
    #     self.players_tab = ttk.Frame(master=parent, padding=5)
    #     self.players_tab.rowconfigure(index=0, weight=1)
    #     self.players_tab.columnconfigure(index=0, weight=1)
    #     parent.add(child=self.players_tab, text=text)
    #     self._build_players_tab_content(parent=self.players_tab)
    #     self._build_players_tab_bottom_bar(parent=self.players_tab)

    # def _build_players_tab_content(self, parent: ttk.Frame):
    #     self.players_tab_content = ttk.Frame(master=parent)
    #     self.players_tab_content.grid(row=0, column=0, sticky="nsew")
    #     self.players_tab_content.columnconfigure(index=0, weight=1)
    #     self.players_tab_content.rowconfigure(index=1, weight=1)
    #     self._build_players_tab_prompt(parent=self.players_tab_content)
    #     self._build_players_tab_players(parent=self.players_tab_content)
    #     self._build_players_tab_controls(parent=self.players_tab_content)
    
    # def _build_players_tab_prompt(self, parent: ttk.Frame):
    #     self.players_tab_prompt = ttk.Frame(master=parent, padding=5)
    #     self.players_tab_prompt.grid(row=0, column=0, sticky="nsew")
    #     self.players_tab_prompt.rowconfigure(index=0, weight=1)
    #     self.players_tab_prompt.columnconfigure(index=0, weight=1)
    #     self.players_tab_prompt.columnconfigure(index=1, weight=2)
    #     self.players_tab_prompt.columnconfigure(index=2, weight=1)
    #     self._build_players_tab_prompt_label(parent=self.players_tab_prompt)
    #     self._build_players_tab_prompt_entry(parent=self.players_tab_prompt)
    #     self._build_players_tab_prompt_add(parent=self.players_tab_prompt)
    
    # def _build_players_tab_prompt_label(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["prompt"]["label"]
    #     self.players_tab_prompt_label = ttk.Label(master=parent, text=text)
    #     self.players_tab_prompt_label.grid(row=0, column=0, sticky="nse")

    # def _build_players_tab_prompt_entry(self, parent: ttk.Frame):
    #     self.players_tab_prompt_entry = ttk.Entry(master=parent)
    #     self.players_tab_prompt_entry.grid(
    #         row=0, column=1, sticky="nsew", padx=5
    #     )

    # def _build_players_tab_prompt_add(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["prompt"]["button"]
    #     self.players_tab_prompt_add = ttk.Button(master=parent, text=text)
    #     self.players_tab_prompt_add.grid(row=0, column=2, sticky="nsw")

    # def _build_players_tab_players(self, parent: ttk.Frame):
    #     self.players_tab_players = ttk.Frame(master=parent, padding=5)
    #     self.players_tab_players.grid(row=1, column=0, sticky="nsew")
    #     self.players_tab_players.rowconfigure(index=0, weight=1)
    #     self.players_tab_players.columnconfigure(index=0, weight=1)
    #     self._build_players_tab_players_view(parent=self.players_tab_players)
    
    # def _build_players_tab_players_view(self, parent: ttk.Frame):
    #     column_texts = PregameWindow.TEXTS["players"]["view_columns"]
    #     self.players_tab_players_view = ttk.Treeview(
    #         master=parent, columns=["player"], selectmode="browse"
    #     )
    #     self.players_tab_players_view.grid(row=0, column=0, sticky="nsew")
    #     self.players_tab_players_view.column(column="#0", stretch=tk.NO)
    #     self.players_tab_players_view.column(column="player", anchor="w")
    #     self.players_tab_players_view.heading(
    #         column="#0", text=column_texts["#0"]
    #     )
    #     self.players_tab_players_view.heading(
    #         column="player", text=column_texts["player"]
    #     )

    # def _build_players_tab_controls(self, parent: ttk.Frame):
    #     self.players_tab_controls = ttk.Frame(master=parent, padding=5)
    #     self.players_tab_controls.grid(row=2, column=0, sticky="nsew")
    #     self.players_tab_controls.rowconfigure(index=0, weight=1)
    #     self.players_tab_controls.columnconfigure(index=0, weight=1)
    #     self.players_tab_controls.columnconfigure(index=1, weight=1)
    #     self.players_tab_controls.columnconfigure(index=2, weight=1)
    #     self.players_tab_controls.columnconfigure(index=3, weight=1)
    #     self.players_tab_controls.columnconfigure(index=4, weight=1)
    #     self._build_players_tab_controls_move_top(
    #         parent=self.players_tab_controls
    #     )
    #     self._build_players_tab_controls_move_up(
    #         parent=self.players_tab_controls
    #     )
    #     self._build_players_tab_controls_move_down(
    #         parent=self.players_tab_controls
    #     )
    #     self._build_players_tab_controls_move_bottom(
    #         parent=self.players_tab_controls
    #     )
    #     self._build_players_tab_controls_delete(
    #         parent=self.players_tab_controls
    #     )

    # def _build_players_tab_controls_move_top(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["controls"]["move_top"]
    #     self.players_tab_controls_move_top = ttk.Button(
    #         master = parent, text=text
    #     )
    #     self.players_tab_controls_move_top.grid(row=0, column=0, sticky="nsew")

    # def _build_players_tab_controls_move_up(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["controls"]["move_up"]
    #     self.players_tab_controls_move_up = ttk.Button(
    #         master = parent, text=text
    #     )
    #     self.players_tab_controls_move_up.grid(row=0, column=1, sticky="nsew")

    # def _build_players_tab_controls_move_down(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["controls"]["move_down"]
    #     self.players_tab_controls_move_down = ttk.Button(
    #         master = parent, text=text
    #     )
    #     self.players_tab_controls_move_down.grid(
    #         row=0, column=2, sticky="nsew"
    #     )

    # def _build_players_tab_controls_move_bottom(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["controls"]["move_bottom"]
    #     self.players_tab_controls_move_bottom = ttk.Button(
    #         master = parent, text=text
    #     )
    #     self.players_tab_controls_move_bottom.grid(
    #         row=0, column=3, sticky="nsew"
    #     )

    # def _build_players_tab_controls_delete(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["controls"]["delete"]
    #     self.players_tab_controls_delete = ttk.Button(
    #         master = parent, text=text
    #     )
    #     self.players_tab_controls_delete.grid(row=0, column=4, sticky="nsew")

    # def _build_players_tab_bottom_bar(self, parent: ttk.Frame):
    #     self.players_tab_bottom_bar = ttk.Frame(master=parent, padding=5)
    #     self.players_tab_bottom_bar.grid(row=1, column=0, sticky="nsew")
    #     self.players_tab_bottom_bar.rowconfigure(index=0, weight=1)
    #     self.players_tab_bottom_bar.columnconfigure(index=0, weight=1)
    #     self.players_tab_bottom_bar.columnconfigure(index=1, weight=1)
    #     self._build_players_tab_goto_mode_tab(
    #         parent=self.players_tab_bottom_bar
    #     )
    #     self._build_players_tab_goto_overview_tab(
    #         parent=self.players_tab_bottom_bar
    #     )

    # def _build_players_tab_goto_mode_tab(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["goto_mode_tab"]
    #     self.players_tab_goto_mode_tab = ttk.Button(master=parent, text=text)
    #     self.players_tab_goto_mode_tab.grid(row=0, column=0, sticky="nsw")

    # def _build_players_tab_goto_overview_tab(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["players"]["goto_overview_tab"]
    #     self.players_tab_goto_overview_tab = ttk.Button(
    #         master=parent, text=text
    #     )
    #     self.players_tab_goto_overview_tab.grid(row=0, column=1, sticky="nse")

    def configure(self):
        ...

    # def _configure_players_tab(self):
    #     self.root.hide(tab_id=self.players_tab)
    #     self._configure_players_tab_content()

    # def _configure_players_tab_content(self):
    #     self._configure_players_tab_prompt()
    #     self._configure_players_tab_players()
    #     self._configure_players_tab_controls()
    #     self._configure_players_tab_bottom_bar()

    # def _configure_players_tab_prompt(self):
    #     self._configure_players_tab_prompt_entry()
    #     self._configure_players_tab_prompt_add()

    # def _configure_players_tab_prompt_entry(self):
    #     self.players_tab_prompt_entry.configure(
    #         textvariable=self.player_to_add
    #     )
    #     # self.players_tab_prompt_entry.bind(
    #     #     "<Key-Return>",
    #     #     lambda e: self._handle_players_tab_prompt_entry_return()
    #     # )

    # def _configure_players_tab_prompt_add(self):
    #     self.players_tab_prompt_add.configure(
    #         command=self._handle_players_tab_prompt_add
    #     )

    # def _configure_players_tab_players(self):
    #     self._configure_players_tab_players_view()

    # # [TODO]: bind losing focus
    # def _configure_players_tab_players_view(self):
    #     self.players_tab_players_view.bind(
    #         "<<TreeviewSelect>>",
    #         lambda e: self._handle_players_tab_players_view_select()
    #     )
    #     self.players_tab_players_view.bind(
    #         "<Key-Delete>",
    #         lambda e: self._handle_players_tab_players_view_delete()
    #     )

    # def _configure_players_tab_controls(self):
    #     self._configure_players_tab_controls_move_top()
    #     self._configure_players_tab_controls_move_up()
    #     self._configure_players_tab_controls_move_down()
    #     self._configure_players_tab_controls_move_bottom()
    #     self._configure_players_tab_controls_delete()

    # def _configure_players_tab_controls_move_top(self):
    #     self.players_tab_controls_move_top.state(["disabled"])
    #     self.players_tab_controls_move_top.configure(
    #         command=self._handle_players_tab_controls_move_top
    #     )

    # def _configure_players_tab_controls_move_up(self):
    #     self.players_tab_controls_move_up.state(["disabled"])
    #     self.players_tab_controls_move_up.configure(
    #         command=self._handle_players_tab_controls_move_up
    #     )

    # def _configure_players_tab_controls_move_down(self):
    #     self.players_tab_controls_move_down.state(["disabled"])
    #     self.players_tab_controls_move_down.configure(
    #         command=self._handle_players_tab_controls_move_down
    #     )

    # def _configure_players_tab_controls_move_bottom(self):
    #     self.players_tab_controls_move_bottom.state(["disabled"])
    #     self.players_tab_controls_move_bottom.configure(
    #         command=self._handle_players_tab_controls_move_bottom
    #     )

    # def _configure_players_tab_controls_delete(self):
    #     self.players_tab_controls_delete.state(["disabled"])
    #     self.players_tab_controls_delete.configure(
    #         command=self._handle_players_tab_controls_delete
    #     )

    # def _configure_players_tab_bottom_bar(self):
    #     self._configure_players_tab_goto_mode_tab()
    #     self._configure_players_tab_goto_overview_tab()
    
    # def _configure_players_tab_goto_mode_tab(self):
    #     self.players_tab_goto_mode_tab.configure(
    #         command=self._handle_players_tab_goto_mode_tab
    #     )

    # def _configure_players_tab_goto_overview_tab(self):
    #     self.players_tab_goto_overview_tab.state(["disabled"])
    #     self.players_tab_goto_overview_tab.configure(
    #         command=self._handle_players_tab_goto_overview_tab
    #     )

    # def _handle_players_tab_prompt_entry_return(self):
    #     self.players_tab_prompt_add.invoke()

    # def _handle_players_tab_prompt_entry_up(self) -> None:
    #     if not self.players:
    #         return None
    #     self.players_tab_players_view.selection_set(self.players_tab_players_view.get_children()[0])
    #     return None

    # def _handle_players_tab_prompt_entry_down(self) -> None:
    #     if not self.players:
    #         return None
    #     self.players_tab_players_view.selection_set(self.players_tab_players_view.get_children()[0])
    #     return None

    # # [TODO]: notify player somehow on failure, i.e. invalid (on success too?)
    # def _handle_players_tab_prompt_add(self) -> None:
    #     self.players_tab_prompt_entry.focus_set()
    #     player_to_add = self.player_to_add.get().strip()
    #     self.player_to_add.set("")
    #     if not self._is_valid_player_name(name=player_to_add):
    #         return None
    #     self.players.append(player_to_add)
    #     self._update_players_tab_players_view()
    #     self.root.add(child=self.overview_tab)
    #     self.players_tab_goto_overview_tab.state(["!disabled"])
    #     return None

    # def _handle_players_tab_players_view_select(self) -> None:
    #     if not self.players:
    #         return None
    #     self.players_tab_controls_move_top.state(["!disabled"])
    #     self.players_tab_controls_move_up.state(["!disabled"])
    #     self.players_tab_controls_move_down.state(["!disabled"])
    #     self.players_tab_controls_move_bottom.state(["!disabled"])
    #     self.players_tab_controls_delete.state(["!disabled"])
    #     self.players_tab_players_view.focus_set()
    #     return None

    # def _handle_players_tab_players_view_delete(self) -> None:
    #     if not self.players_tab_players_view.selection():
    #         return None
    #     self.players_tab_controls_delete.invoke()
    #     return None

    # def _handle_players_tab_controls_move_top(self) -> None:
    #     selection = self.players_tab_players_view.selection()
    #     if not selection:
    #         return None
    #     item = self.players_tab_players_view.selection()[0]
    #     old_index = self.players_tab_players_view.item(
    #         item=item, option="text"
    #     )-1
    #     new_index = 0
    #     self.players.insert(new_index, self.players.pop(old_index))
    #     self._update_players_tab_players_view()
    #     item = self.players_tab_players_view.get_children()[0]
    #     self.players_tab_players_view.selection_set(item)
    #     return None

    # def _handle_players_tab_controls_move_up(self) -> None:
    #     selection = self.players_tab_players_view.selection()
    #     if not selection:
    #         return None
    #     item = self.players_tab_players_view.selection()[0]
    #     old_index = self.players_tab_players_view.item(
    #         item=item, option="text"
    #     )-1
    #     new_index = old_index-1 if old_index>0 else 0
    #     self.players.insert(new_index, self.players.pop(old_index))
    #     self._update_players_tab_players_view()
    #     item = self.players_tab_players_view.get_children()[new_index]
    #     self.players_tab_players_view.selection_set(item)
    #     return None

    # def _handle_players_tab_controls_move_down(self) -> None:
    #     selection = self.players_tab_players_view.selection()
    #     if not selection:
    #         return None
    #     item = self.players_tab_players_view.selection()[0]
    #     old_index = self.players_tab_players_view.item(
    #         item=item, option="text"
    #     )-1
    #     new_index = old_index+1 if old_index<len(self.players)-1 else old_index
    #     self.players.insert(new_index, self.players.pop(old_index))
    #     self._update_players_tab_players_view()
    #     item = self.players_tab_players_view.get_children()[new_index]
    #     self.players_tab_players_view.selection_set(item)
    #     return None

    # def _handle_players_tab_controls_move_bottom(self) -> None:
    #     selection = self.players_tab_players_view.selection()
    #     if not selection:
    #         return None
    #     item = self.players_tab_players_view.selection()[0]
    #     old_index = self.players_tab_players_view.item(
    #         item=item, option="text"
    #     )-1
    #     new_index = len(self.players)-1
    #     self.players.insert(new_index, self.players.pop(old_index))
    #     self._update_players_tab_players_view()
    #     item = self.players_tab_players_view.get_children()[new_index]
    #     self.players_tab_players_view.selection_set(item)
    #     return None

    # def _handle_players_tab_controls_delete(self) -> None:
    #     selection = self.players_tab_players_view.selection()
    #     if not selection:
    #         return None
    #     item = self.players_tab_players_view.selection()[0]
    #     index = self.players_tab_players_view.item(
    #         item=item, option="text"
    #     )-1
    #     self.players.pop(index)
    #     self._update_players_tab_players_view()
    #     if not self.players:
    #         self.root.hide(tab_id=self.overview_tab)
    #         self.players_tab_controls_move_top.state(["disabled"])
    #         self.players_tab_controls_move_up.state(["disabled"])
    #         self.players_tab_controls_move_down.state(["disabled"])
    #         self.players_tab_controls_move_bottom.state(["disabled"])
    #         self.players_tab_controls_delete.state(["disabled"])
    #         self.players_tab_goto_overview_tab.state(["disabled"])
    #         self.players_tab_prompt_entry.focus_set()
    #         return None
    #     if index == len(self.players):
    #         index = index-1
    #     item = self.players_tab_players_view.get_children()[index]
    #     self.players_tab_players_view.selection_set(item)
    #     return None

    # def _is_valid_player_name(self, name: str) -> bool:
    #     if not name:
    #         return False
    #     if name in self.players:
    #         return False
    #     if len(self.players) == PregameWindow.PLAYER_LIMIT:
    #         return False
    #     return True

    # def _handle_players_tab_goto_mode_tab(self):
    #     self._goto_mode_tab()

    # def _handle_players_tab_goto_overview_tab(self):
    #     self._goto_overview_tab()

    # def _update_players_tab_players_view(self):
    #     for item in self.players_tab_players_view.get_children():
    #         self.players_tab_players_view.delete(item)
    #     for position, player in enumerate(self.players, start=1):
    #         self.players_tab_players_view.insert(
    #             parent="", index=tk.END, text=position, values=(player,)
    #         )

    # def _goto_mode_tab(self):
    #     self.root.select(tab_id=self.mode_tab)
    
    # def _goto_overview_tab(self):
    #     self.root.select(tab_id=self.overview_tab)

    ...

# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #

class OverviewTab():
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    TEXTS = {
        "title": "Spiel starten",
        "label": "Du hast konfiguriert:",
        "goto_players_tab": "< Zurück",
        "start_game": "Start!"
    }

    def __init__(self, notebook: ttk.Notebook):
        self.parent = notebook
        self.root: ttk.Frame = None
        # self.overview_tab_content: ttk.Frame = None
        # self.overview_tab_label: ttk.Label = None

        # self.overview_tab_bottom_bar: ttk.Frame = None
        # self.overview_tab_goto_players_tab: ttk.Button = None
        # self.overview_tab_start_game: ttk.Button = None  

        self.build()
        self.configure()

    def build(self):
        text = OverviewTab.TEXTS["title"]
        self.root = ttk.Frame(master=self.parent, padding=5)
        self.parent.add(child=self.root, text=text)
        ...

    # def _build_overview_tab(self, parent: ttk.Notebook):
    #     text = PregameWindow.TEXTS["overview"]["title"]
    #     self.overview_tab = ttk.Frame(master=parent, padding=5)
    #     self.overview_tab.rowconfigure(index=0, weight=1)
    #     self.overview_tab.columnconfigure(index=0, weight=1)
    #     parent.add(child=self.overview_tab, text=text)
    #     self._build_overview_tab_content(parent=self.overview_tab)
    #     self._build_overview_tab_bottom_bar(parent=self.overview_tab)

    # def _build_overview_tab_content(self, parent: ttk.Frame):
    #     self.overview_tab_content = ttk.Frame(master=parent, padding=5)
    #     self.overview_tab_content.grid(row=0, column=0, sticky="nsew")
    #     self._build_overview_tab_label(parent=self.overview_tab_content)

    # def _build_overview_tab_label(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["overview"]["label"]
    #     self.overview_tab_label = ttk.Label(master=parent, text=text)
    #     self.overview_tab_label.grid(row=0, column=0)

    # def _build_overview_tab_bottom_bar(self, parent: ttk.Frame):
    #     self.overview_tab_bottom_bar = ttk.Frame(master=parent, padding=5)
    #     self.overview_tab_bottom_bar.grid(row=1, column=0, sticky="nsew")
    #     self.overview_tab_bottom_bar.rowconfigure(index=0, weight=1)
    #     self.overview_tab_bottom_bar.columnconfigure(index=0, weight=1)
    #     self.overview_tab_bottom_bar.columnconfigure(index=1, weight=1)
    #     self._build_overview_tab_goto_players_tab(
    #         parent=self.overview_tab_bottom_bar
    #     )
    #     self._build_overview_tab_start_game(
    #         parent=self.overview_tab_bottom_bar
    #     )

    # def _build_overview_tab_goto_players_tab(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["overview"]["goto_players_tab"]
    #     self.overview_tab_goto_players_tab = ttk.Button(
    #         master=parent, text=text
    #     )
    #     self.overview_tab_goto_players_tab.grid(row=0, column=0, sticky="nsw")

    # def _build_overview_tab_start_game(self, parent: ttk.Frame):
    #     text = PregameWindow.TEXTS["overview"]["start_game"]
    #     self.overview_tab_start_game = ttk.Button(master=parent, text=text)
    #     self.overview_tab_start_game.grid(row=0, column=1, sticky="nse")

    def configure(self):
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

    ...

# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #
# ########################################################################### #

class PregameWindow():
    """
    tbc
    """

    # Temporary, to be defined somewhere/-how else once I know a better way.
    PLAYER_LIMIT = 8

    def __init__(self, parent = tk.Tk):
        self.parent = parent
        self.root: ttk.Notebook = None

        self.build()

        self.modes_tab = ModesTab(notebook=self.root)
        self.players_tab = PlayersTab(notebook=self.root)
        self.overview_tab = OverviewTab(notebook=self.root)

        self.configure()

    def build(self):
        self.root = ttk.Notebook(master=self.parent, padding=5)
        self.root.grid(row=0, column=0, sticky="nsew")
        self.root.rowconfigure(index=0, weight=1)
        self.root.columnconfigure(index=0, weight=1)
        ...

    def configure(self):
        self.root.bind("<<NotebookTabChanged>>", self.handle_tab_changed)
        ...

    def handle_tab_changed(self, event: tk.Event) -> None:
        current_tab_index = self.root.index("current")
        if current_tab_index == self.root.index(self.modes_tab.root):
            self.modes_tab.view.focus_set()
            return None
        # if current_tab_index == self.root.index(self.players_tab.root):
        #     self.players_tab.entry.focus_set()
        #     return None

    ...
