import logging
import tkinter as tk
import tkinter.ttk as ttk

from modules.games import METADATA


class App(tk.Tk):
    def __init__(self, enable_debugging: bool = False):
        super().__init__()
        self._configure_self()

        self.pregame_window = PregameWindow(
            master=self, enable_debugging=enable_debugging
        )
        self._show_pregame_window()

    def _configure_self(self):
        self.title(string="PyDarts")
        self.minsize(width=800, height=600)
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
        "mode_tab": {
            "header": "Modus wählen",
            "selection_columns": {
                "#0": "Modus",
                "description": "Beschreibung"
            }
        },
        "players_tab": {
            "header": "Spieler hinzufügen",
            "label": "Bitte Spieler hinzufügen:"
        },
        "overview_tab": {
            "header": "Spiel starten",
            "label": "Du hast konfiguriert:"
        }
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, padding=5, **kwargs)

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.root: ttk.Notebook = None
        self.mode_tab: ttk.Frame = None
        self.mode_tab_content: ttk.Frame = None
        self.mode_tab_selection: ttk.Treeview = None
        self.mode_tab_bottom_bar: ttk.Frame = None
        self.mode_tab_goto_players_tab: ttk.Button = None
        self.players_tab: ttk.Frame = None
        self.players_tab_content: ttk.Frame = None
        self.players_tab_label: ttk.Label = None
        self.players_tab_bottom_bar: ttk.Frame = None
        self.players_tab_goto_mode_tab: ttk.Button = None
        self.players_tab_goto_overview_tab: ttk.Button = None
        self.overview_tab: ttk.Frame = None
        self.overview_tab_content: ttk.Frame = None
        self.overview_tab_label: ttk.Label = None
        self.overview_tab_bottom_bar: ttk.Frame = None
        self.overview_tab_goto_players_tab: ttk.Button = None
        self.overview_tab_start_game: ttk.Button = None  

        self._build_root(self)
        self._configure_logic()

        if self.is_debugging_enabled:
            self.configure_debugging()

    def _build_root(self, parent: ttk.Frame):
        self.root = ttk.Notebook(master=parent)
        self.root.grid(row=0, column=0, sticky="nsew")
        self._build_mode_tab(parent=self.root)
        self._build_players_tab(parent=self.root)
        self._build_overview_tab(parent=self.root)

    def _build_mode_tab(self, parent: ttk.Notebook):
        text = PregameWindow.TEXTS["mode_tab"]["header"]
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
    # - lock user on tab until a selection is made
    # - save selected mode
    # - dynamically add/configure columns if it makes sense
    # - calculate minwidth for 'Modus' based on longest 'display_name'
    def _build_mode_tab_selection(self, parent: ttk.Frame):
        column_texts = PregameWindow.TEXTS["mode_tab"]["selection_columns"]
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
        text = PregameWindow.TEXTS["players_tab"]["header"]
        self.players_tab = ttk.Frame(master=parent, padding=5)
        self.players_tab.rowconfigure(index=0, weight=1)
        self.players_tab.columnconfigure(index=0, weight=1)
        parent.add(child=self.players_tab, text=text)
        self._build_players_tab_content(parent=self.players_tab)
        self._build_players_tab_bottom_bar(parent=self.players_tab)

    def _build_players_tab_content(self, parent: ttk.Frame):
        self.players_tab_content = ttk.Frame(master=parent, padding=5)
        self.players_tab_content.grid(row=0, column=0, sticky="nsew")
        self._build_players_tab_label(parent=self.players_tab_content)

    def _build_players_tab_label(self, parent: ttk.Frame):
        text = PregameWindow.TEXTS["players_tab"]["label"]
        self.players_tab_label = ttk.Label(master=parent, text=text)
        self.players_tab_label.grid(row=0, column=0)

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
        self.players_tab_goto_mode_tab = ttk.Button(master=parent, text="<<")
        self.players_tab_goto_mode_tab.grid(row=0, column=0, sticky="nsw")

    def _build_players_tab_goto_overview_tab(self, parent: ttk.Frame):
        self.players_tab_goto_overview_tab = ttk.Button(
            master=parent, text=">>"
        )
        self.players_tab_goto_overview_tab.grid(row=0, column=1, sticky="nse")

    def _build_overview_tab(self, parent: ttk.Notebook):
        text = PregameWindow.TEXTS["overview_tab"]["header"]
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
        text = PregameWindow.TEXTS["overview_tab"]["label"]
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
        self.overview_tab_goto_players_tab = ttk.Button(
            master=parent, text="<<"
        )
        self.overview_tab_goto_players_tab.grid(row=0, column=0, sticky="nsw")

    def _build_overview_tab_start_game(self, parent: ttk.Frame):
        self.overview_tab_start_game = ttk.Button(master=parent, text="Start!")
        self.overview_tab_start_game.grid(row=0, column=1, sticky="nse")

    def _configure_logic(self):
        self.mode_tab_goto_players_tab.configure(
            command=self._handle_mode_tab_goto_players_tab
        )
        self.players_tab_goto_mode_tab.configure(
            command=self._handle_players_tab_goto_mode_tab
        )
        self.players_tab_goto_overview_tab.configure(
            command=self._handle_players_tab_goto_overview_tab
        )
        self.overview_tab_goto_players_tab.configure(
            command=self._handle_overview_tab_goto_players_tab
        )
        self.overview_tab_start_game.configure(
            command=self._handle_overview_tab_start_game
        )
        self.root.hide(tab_id=self.players_tab)
        self.root.hide(tab_id=self.overview_tab)
        self.mode_tab_goto_players_tab.state(["disabled"])
        self.mode_tab_selection.bind(
            "<<TreeviewSelect>>", lambda e: self._handle_mode_tab_selection()
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
        self._enable_players_tab()
        self._enable_overview_tab()

    def _enable_players_tab(self):
        self.root.add(child=self.players_tab)
        self.mode_tab_goto_players_tab.state(["!disabled"])

    def _enable_overview_tab(self):
        self.root.add(child=self.overview_tab)
