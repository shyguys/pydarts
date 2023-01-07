import logging
import tkinter as tk
import tkinter.ttk as ttk

from modules.games import METADATA


class App(tk.Tk):
    def __init__(self, enable_debugging: bool = False):
        super().__init__()
        self._build()

        self.pregame_window = PregameWindow(
            master=self, enable_debugging=enable_debugging
        )
        self._show_pregame_window()

    def _build(self):
        self.title(string="PyDarts")
        self.minsize(width=600, height=600)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

    def _show_pregame_window(self):
        self.pregame_window.grid(row=0, column=0, sticky="nsew")

class Window(ttk.Frame):
    def __init__(self, *args, enable_debugging: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_debugging_enabled = enable_debugging

    def walk_widget_hierarchy(self):
        children = self.winfo_children()
        while children:
            widget = children.pop()
            yield widget
            for child in reversed(widget.winfo_children()):
                children.append(child)

    def configure_debugging(self):
        for widget in self.walk_widget_hierarchy():
            try:
                # [TODO]: highlight additional way?
                widget.configure(borderwidth=1, relief="solid")
            except tk.TclError:
                # Widget has no 'borderwidth' option
                logging.warning(f"widget cannot be bordered: {widget!r}")
                

class PregameWindow(Window):
    """
    tbc
    """

    # The following constants for displayed texts are
    # defined here for now, because I don't how to properly
    # achieve language selection within my application.

    TEXTS = {
        "mode": {
            "title": "Modus wählen",
            "selection_columns": {
                "#0": "Modus",
                "description": "Beschreibung"
            },
            "goto_players_tab": ">>"
        },
        "players": {
            "title": "Spieler hinzufügen",
            "prompt": {
                "label": "Gib einen Namen ein:",
                "entry": "",
                "button": "Hinzufügen"
            },
            "goto_mode_tab": "<<",
            "goto_overview_tab": ">>"
        },
        "overview": {
            "title": "Spiel starten",
            "label": "Du hast konfiguriert:",
            "goto_players_tab": "<<",
            "start_game": "Start!"
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, padding=5, **kwargs)

        # --- root --- #

        self.root: ttk.Notebook = None

        # --- mode_tab --- #

        self.mode_tab: ttk.Frame = None

        self.mode_tab_content: ttk.Frame = None
        self.mode_tab_selection: ttk.Treeview = None

        self.mode_tab_bottom_bar: ttk.Frame = None
        self.mode_tab_goto_players_tab: ttk.Button = None

        # --- players_tab --- #

        self.players_tab: ttk.Frame = None

        self.players_tab_content: ttk.Frame = None
        self.players_tab_prompt: ttk.Frame = None
        self.players_tab_prompt_label: ttk.Label = None
        self.players_tab_prompt_entry: ttk.Entry = None
        self.players_tab_prompt_add: ttk.Button = None

        self.players_tab_bottom_bar: ttk.Frame = None
        self.players_tab_goto_mode_tab: ttk.Button = None
        self.players_tab_goto_overview_tab: ttk.Button = None

        # --- overview_tab --- #

        self.overview_tab: ttk.Frame = None

        self.overview_tab_content: ttk.Frame = None
        self.overview_tab_label: ttk.Label = None

        self.overview_tab_bottom_bar: ttk.Frame = None
        self.overview_tab_goto_players_tab: ttk.Button = None
        self.overview_tab_start_game: ttk.Button = None  

        self._build()
        self._configure()

        if self.is_debugging_enabled:
            self.configure_debugging()

    def _build(self):
            self.rowconfigure(index=0, weight=1)
            self.columnconfigure(index=0, weight=1)
            self._build_root(self)

    def _build_root(self, parent: ttk.Frame):
        self.root = ttk.Notebook(master=parent)
        self.root.grid(row=0, column=0, sticky="nsew")
        self._build_mode_tab(parent=self.root)
        self._build_players_tab(parent=self.root)
        self._build_overview_tab(parent=self.root)

    def _build_mode_tab(self, parent: ttk.Notebook):
        text = PregameWindow.TEXTS["mode"]["title"]
        self.mode_tab = ttk.Frame(master=parent, padding=5)
        self.mode_tab.rowconfigure(index=0, weight=1)
        self.mode_tab.columnconfigure(index=0, weight=1)
        parent.add(child=self.mode_tab, text=text)
        self._build_mode_tab_content(parent=self.mode_tab)
        self._build_mode_tab_bottom_bar(parent=self.mode_tab)

    def _build_mode_tab_content(self, parent: ttk.Frame):
        self.mode_tab_content = ttk.Frame(master=parent, padding=5)
        self.mode_tab_content.grid(row=0, column=0, sticky="nsew")
        self.mode_tab_content.rowconfigure(index=0, weight=1)
        self.mode_tab_content.columnconfigure(index=0, weight=1)
        self._build_mode_tab_selection(parent=self.mode_tab_content)

    # [TODO]:
    # - dynamically add/configure columns if it makes sense
    # - calculate minwidth for '#0' based on longest 'display_name'
    def _build_mode_tab_selection(self, parent: ttk.Frame):
        column_texts = PregameWindow.TEXTS["mode"]["selection_columns"]
        self.mode_tab_selection = ttk.Treeview(
            master=parent, columns=["description"], selectmode="browse"
        )
        self.mode_tab_selection.grid(row=0, column=0, sticky="nsew")
        self.mode_tab_selection.column(column="#0", stretch=tk.NO)
        self.mode_tab_selection.column(column="description", anchor="w")
        self.mode_tab_selection.heading(column="#0", text=column_texts["#0"])
        self.mode_tab_selection.heading(
            column="description", text=column_texts["description"]
        )
        for game in METADATA.games:
            self.mode_tab_selection.insert(
                parent="", index=tk.END, text=game.display_name,
                values=(game.description,)
            )
    
    def _build_mode_tab_bottom_bar(self, parent: ttk.Frame):
        self.mode_tab_bottom_bar = ttk.Frame(master=parent, padding=5)
        self.mode_tab_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.mode_tab_bottom_bar.rowconfigure(index=0, weight=1)
        self.mode_tab_bottom_bar.columnconfigure(index=0, weight=1)
        self._build_mode_tab_goto_players_tab(parent=self.mode_tab_bottom_bar)

    def _build_mode_tab_goto_players_tab(self, parent: ttk.Frame):
        self.mode_tab_goto_players_tab = ttk.Button(master=parent, text=">>")
        self.mode_tab_goto_players_tab.grid(row=0, column=0, sticky="nse")
    
    def _build_players_tab(self, parent: ttk.Notebook):
        text = PregameWindow.TEXTS["players"]["title"]
        self.players_tab = ttk.Frame(master=parent, padding=5)
        self.players_tab.rowconfigure(index=0, weight=1)
        self.players_tab.columnconfigure(index=0, weight=1)
        parent.add(child=self.players_tab, text=text)
        self._build_players_tab_content(parent=self.players_tab)
        self._build_players_tab_bottom_bar(parent=self.players_tab)

    def _build_players_tab_content(self, parent: ttk.Frame):
        self.players_tab_content = ttk.Frame(master=parent, padding=5)
        self.players_tab_content.grid(row=0, column=0, sticky="nsew")
        self.players_tab_content.columnconfigure(index=0, weight=1)
        self.players_tab_content.rowconfigure(index=1, weight=1)
        self._build_players_tab_prompt(parent=self.players_tab_content)
        # self._build_players_tab_players_list(parent=self.players_tab_content)
        # self._build_players_tab_list_controls(parent=self.players_tab_content)
    
    def _build_players_tab_prompt(self, parent: ttk.Frame):
        self.players_tab_prompt = ttk.Frame(master=parent, padding=5)
        self.players_tab_prompt.grid(row=0, column=0, sticky="nsew")
        self.players_tab_prompt.rowconfigure(index=0, weight=1)
        self.players_tab_prompt.columnconfigure(index=0, weight=1)
        self.players_tab_prompt.columnconfigure(index=1, weight=2)
        self.players_tab_prompt.columnconfigure(index=2, weight=1)
        self._build_players_tab_prompt_label(parent=self.players_tab_prompt)
        self._build_players_tab_prompt_entry(parent=self.players_tab_prompt)
        self._build_players_tab_prompt_add(parent=self.players_tab_prompt)
    
    def _build_players_tab_prompt_label(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["players"]["prompt"]["label"]
        self.players_tab_prompt_label = ttk.Label(master=parent, text=text)
        self.players_tab_prompt_label.grid(row=0, column=0, sticky="nse")

    def _build_players_tab_prompt_entry(self, parent: ttk.Frame):
        self.players_tab_prompt_entry = ttk.Entry(master=parent)
        self.players_tab_prompt_entry.grid(
            row=0, column=1, sticky="nsew", padx=5
        )

    def _build_players_tab_prompt_add(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["players"]["prompt"]["button"]
        self.players_tab_prompt_add = ttk.Button(master=parent, text=text)
        self.players_tab_prompt_add.grid(row=0, column=2, sticky="nsw")

    def _build_players_tab_bottom_bar(self, parent: ttk.Frame):
        self.players_tab_bottom_bar = ttk.Frame(master=parent, padding=5)
        self.players_tab_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.players_tab_bottom_bar.rowconfigure(index=0, weight=1)
        self.players_tab_bottom_bar.columnconfigure(index=0, weight=1)
        self.players_tab_bottom_bar.columnconfigure(index=1, weight=1)
        self._build_players_tab_goto_mode_tab(
            parent=self.players_tab_bottom_bar
        )
        self._build_players_tab_goto_overview_tab(
            parent=self.players_tab_bottom_bar
        )

    def _build_players_tab_goto_mode_tab(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["players"]["goto_mode_tab"]
        self.players_tab_goto_mode_tab = ttk.Button(master=parent, text=text)
        self.players_tab_goto_mode_tab.grid(row=0, column=0, sticky="nsw")

    def _build_players_tab_goto_overview_tab(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["players"]["goto_overview_tab"]
        self.players_tab_goto_overview_tab = ttk.Button(
            master=parent, text=text
        )
        self.players_tab_goto_overview_tab.grid(row=0, column=1, sticky="nse")

    def _build_overview_tab(self, parent: ttk.Notebook):
        text = PregameWindow.TEXTS["overview"]["title"]
        self.overview_tab = ttk.Frame(master=parent, padding=5)
        self.overview_tab.rowconfigure(index=0, weight=1)
        self.overview_tab.columnconfigure(index=0, weight=1)
        parent.add(child=self.overview_tab, text=text)
        self._build_overview_tab_content(parent=self.overview_tab)
        self._build_overview_tab_bottom_bar(parent=self.overview_tab)

    def _build_overview_tab_content(self, parent: ttk.Frame):
        self.overview_tab_content = ttk.Frame(master=parent, padding=5)
        self.overview_tab_content.grid(row=0, column=0, sticky="nsew")
        self._build_overview_tab_label(parent=self.overview_tab_content)

    def _build_overview_tab_label(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["overview"]["label"]
        self.overview_tab_label = ttk.Label(master=parent, text=text)
        self.overview_tab_label.grid(row=0, column=0)

    def _build_overview_tab_bottom_bar(self, parent: ttk.Frame):
        self.overview_tab_bottom_bar = ttk.Frame(master=parent, padding=5)
        self.overview_tab_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.overview_tab_bottom_bar.rowconfigure(index=0, weight=1)
        self.overview_tab_bottom_bar.columnconfigure(index=0, weight=1)
        self.overview_tab_bottom_bar.columnconfigure(index=1, weight=1)
        self._build_overview_tab_goto_players_tab(
            parent=self.overview_tab_bottom_bar
        )
        self._build_overview_tab_start_game(
            parent=self.overview_tab_bottom_bar
        )

    def _build_overview_tab_goto_players_tab(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["overview"]["goto_players_tab"]
        self.overview_tab_goto_players_tab = ttk.Button(
            master=parent, text=text
        )
        self.overview_tab_goto_players_tab.grid(row=0, column=0, sticky="nsw")

    def _build_overview_tab_start_game(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["overview"]["start_game"]
        self.overview_tab_start_game = ttk.Button(master=parent, text=text)
        self.overview_tab_start_game.grid(row=0, column=1, sticky="nse")

    def _configure(self):
        self._configure_mode_tab()
        self._configure_players_tab()
        self._configure_overview_tab()
    
    def _configure_mode_tab(self):
        self.mode_tab_goto_players_tab.state(["disabled"])
        self.mode_tab_goto_players_tab.configure(
            command=self._handle_mode_tab_goto_players_tab
        )
        self.mode_tab_selection.bind(
            "<<TreeviewSelect>>", lambda e: self._handle_mode_tab_selection()
        )

    def _configure_players_tab(self):
        self.root.hide(tab_id=self.players_tab)
        self.players_tab_goto_overview_tab.state(["disabled"])
        # [TODO]: bind correct command
        self.players_tab_prompt_add.configure(
            command=self._handle_players_tab_done
        )
        self.players_tab_goto_mode_tab.configure(
            command=self._handle_players_tab_goto_mode_tab
        )
        self.players_tab_goto_overview_tab.configure(
            command=self._handle_players_tab_goto_overview_tab
        )

    def _configure_overview_tab(self):
        self.root.hide(tab_id=self.overview_tab)
        self.overview_tab_goto_players_tab.configure(
            command=self._handle_overview_tab_goto_players_tab
        )
        self.overview_tab_start_game.configure(
            command=self._handle_overview_tab_start_game
        )

    def _handle_mode_tab_goto_players_tab(self):
        self._goto_players_tab()

    def _handle_players_tab_goto_mode_tab(self):
        self._goto_mode_tab()

    def _handle_players_tab_goto_overview_tab(self):
        self._goto_overview_tab()

    def _handle_overview_tab_goto_players_tab(self):
        self._goto_players_tab()

    def _handle_overview_tab_start_game(self):
        self._start_game()

    def _goto_mode_tab(self):
        self.root.select(tab_id=self.mode_tab)

    def _goto_players_tab(self):
        self.root.select(tab_id=self.players_tab)

    def _goto_overview_tab(self):
        self.root.select(tab_id=self.overview_tab)

    def _start_game(self):
        print("Start!")

    def _handle_mode_tab_selection(self):
        self.root.add(child=self.players_tab)
        self.mode_tab_goto_players_tab.state(["!disabled"])

    # [TODO]: verify if this is correct
    def _handle_players_tab_done(self):
        self.root.add(child=self.overview_tab)
        self.players_tab_goto_overview_tab.state(["!disabled"])
