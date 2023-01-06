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
    def __init__(self, *args, **kwargs):
        # --- window --- #
        super().__init__(*args, padding=5, **kwargs)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # --- root notebook --- #

        self.tab_texts = {
            "mode": "Modus wählen",
            "players": "Spieler hinzufügen",
            "overview": "Spiel starten"
        }

        self.root = self._build_root(self)

        # --- mode tab --- #

        self.mode_tab = self._build_mode_tab(
            parent=self.root, text=self.tab_texts["mode"]
        )

        self.mode_tab_content_frame = self._build_mode_tab_content_frame(
            parent=self.mode_tab
        )

        self.mode_selection_columns = {
            "#0": "Modus",
            "description": "Beschreibung"
        }
        
        # [TODO]:
        # - lock user on tab until a selection is made
        # - save selected mode
        # - dynamically add/configure columns if it makes sense
        # - calculate minwidth for 'Modus' based on longest 'display_name'
        self.mode_select_mode_tre = self._build_mode_select_mode_tre(
            parent=self.mode_tab_content_frame,
            columns=self.mode_selection_columns
        )

        # --- mode tab: bottom bar --- #

        self.mode_bottom_bar = ttk.Frame(master=self.mode_tab, padding=5)
        self.mode_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.mode_bottom_bar.rowconfigure(index=0, weight=1)
        self.mode_bottom_bar.columnconfigure(index=0, weight=1)

        self.goto_players_tab_btn = ttk.Button(
            master=self.mode_bottom_bar, text=">>",
            command=self.goto_players_tab
        )
        self.goto_players_tab_btn.grid(row=0, column=0, sticky="nse")

        # --- players tab --- #

        self.players_tab = ttk.Frame(master=self.root, padding=5)
        self.players_tab.rowconfigure(index=0, weight=1)
        self.players_tab.columnconfigure(index=0, weight=1)
        self.root.add(child=self.players_tab, text=self.tab_texts["players"])

        # --- players tab: content frame --- #

        self.players_content_frame = ttk.Frame(
            master=self.players_tab, padding=5
        )
        self.players_content_frame.grid(row=0, column=0, sticky="nsew")

        self.players_add_players_lbl = ttk.Label(
            master=self.players_content_frame, text="Bitte füge Spieler hinzu:"
        )
        self.players_add_players_lbl.grid(row=0, column=0)

        # --- players tab: bottom bar --- #

        self.players_bottom_bar = ttk.Frame(master=self.players_tab, padding=5)
        self.players_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.players_bottom_bar.rowconfigure(index=0, weight=1)
        self.players_bottom_bar.columnconfigure(index=0, weight=1)
        self.players_bottom_bar.columnconfigure(index=1, weight=1)

        self.goto_mode_tab_btn = ttk.Button(
            master=self.players_bottom_bar, text="<<",
            command=self.goto_mode_tab
        )
        self.goto_mode_tab_btn.grid(row=0, column=0, sticky="nsw")

        self.goto_overview_tab_btn = ttk.Button(
            master=self.players_bottom_bar, text=">>",
            command=self.goto_overview_tab
        )
        self.goto_overview_tab_btn.grid(row=0, column=1, sticky="nse")


        # --- overview tab --- #

        self.overview_tab = ttk.Frame(master=self.root, padding=5)
        self.overview_tab.rowconfigure(index=0, weight=1)
        self.overview_tab.columnconfigure(index=0, weight=1)
        self.root.add(child=self.overview_tab, text=self.tab_texts["overview"])

        # --- overview tab: content frame --- #

        self.overview_content_frame = ttk.Frame(
            master=self.overview_tab, padding=5
        )
        self.overview_content_frame.grid(row=0, column=0, sticky="nsew")

        self.overview_add_overview_lbl = ttk.Label(
            master=self.overview_content_frame, text="Du hast konfiguriert:"
        )
        self.overview_add_overview_lbl.grid(row=0, column=0)

        # --- overview tab: bottom bar --- #

        self.overview_bottom_bar = ttk.Frame(
            master=self.overview_tab, padding=5
        )
        self.overview_bottom_bar.grid(row=1, column=0, sticky="nsew")
        self.overview_bottom_bar.rowconfigure(index=0, weight=1)
        self.overview_bottom_bar.columnconfigure(index=0, weight=1)
        self.overview_bottom_bar.columnconfigure(index=1, weight=1)

        self.goto_mode_tab_btn = ttk.Button(
            master=self.overview_bottom_bar, text="<<",
            command=self.goto_players_tab
        )
        self.goto_mode_tab_btn.grid(row=0, column=0, sticky="nsw")

        self.goto_overview_tab_btn = ttk.Button(
            master=self.overview_bottom_bar, text="Start!",
            command=self.start_game
        )
        self.goto_overview_tab_btn.grid(row=0, column=1, sticky="nse")

        # --- debug --- #

        if self.is_debugging_enabled:
            self.configure_debugging()

        # --- logic --- #

        self.root.hide(tab_id=self.players_tab)
        self.root.hide(tab_id=self.overview_tab)
        self.goto_players_tab_btn.state(["disabled"])
        self.mode_select_mode_tre.bind(
            "<<TreeviewSelect>>", lambda e: self.handle_mode_selection()
        )

    def _build_root(self, parent: ttk.Frame) -> ttk.Notebook:
        root = ttk.Notebook(master=parent)
        root.grid(row=0, column=0, sticky="nsew")
        return root

    def _build_mode_tab(self, parent: ttk.Notebook, text: str) -> ttk.Frame:
        mode_tab = ttk.Frame(master=parent, padding=5)
        mode_tab.rowconfigure(index=0, weight=1)
        mode_tab.columnconfigure(index=0, weight=1)
        parent.add(child=mode_tab, text=text)
        return mode_tab

    def _build_mode_tab_content_frame(self, parent: ttk.Frame) -> ttk.Frame:
        mode_content_frame = ttk.Frame(master=parent, padding=5)
        mode_content_frame.grid(row=0, column=0, sticky="nsew")
        mode_content_frame.rowconfigure(index=0, weight=1)
        mode_content_frame.columnconfigure(index=0, weight=1)
        return mode_content_frame

    def _build_mode_select_mode_tre(
        self, parent: ttk.Frame, columns: dict[str, str]
    ) -> ttk.Treeview:
        mode_select_mode_tre = ttk.Treeview(
            master=parent, columns=("description"), selectmode="browse"
        )
        mode_select_mode_tre.column(column="#0", stretch=tk.NO)
        mode_select_mode_tre.column(column="description", anchor="w")
        mode_select_mode_tre.heading(
            column="#0", text=columns["#0"]
        )
        mode_select_mode_tre.heading(
            column="description",
            text=columns["description"]
        )
        for game in METADATA.games:
            mode_select_mode_tre.insert(
                parent="", index=tk.END, text=game.display_name,
                values=(game.description,)
            )
        mode_select_mode_tre.grid(row=0, column=0, sticky="nsew")
        return mode_select_mode_tre

    def start_game(self):
        print("Start!")

    def handle_mode_selection(self):
        self.enable_players_tab()
        self.enable_overview_tab()

    def enable_players_tab(self):
        self.root.add(child=self.players_tab)
        self.goto_players_tab_btn.state(["!disabled"])

    def enable_overview_tab(self):
        self.root.add(child=self.overview_tab)

    def goto_mode_tab(self):
        self.root.select(tab_id=self.mode_tab)

    def goto_players_tab(self):
        self.root.select(tab_id=self.players_tab)

    def goto_overview_tab(self):
        self.root.select(tab_id=self.overview_tab)
