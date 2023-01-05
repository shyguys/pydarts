import argparse
import logging
import tkinter as tk
import tkinter.ttk as ttk

import games


_PROG = "pydarts"


class App(tk.Tk):
    def __init__(self, debug: bool = False):
        super().__init__()

        self.enable_debugging()

        self.title(string="PyDarts")
        self.minsize(width=800, height=600)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.pregame_window = PregameWindow(master=self, debug=debug)
        # self.game = Game()
        # self.game_window = GameWindow(master=self, debug=debug)
        # self.postgame_window = PostgameWindow(master=self, debug=debug)

        self.show_pregame_window()

    def enable_debugging(self):
        logging.basicConfig(
            level=logging.DEBUG,
            format="[%(asctime)s - %(levelname)s] %(message)s",
            datefmt="%H:%M:%S"
        )

    def show_pregame_window(self):
        self.pregame_window.grid(row=0, column=0, sticky="nsew")


class Window(ttk.Frame):
    def __init__(self, *args, debug: bool = False, **kwargs):
        super().__init__(*args, **kwargs)
        self.debug = debug

    def walk_widget_hierarchy(self):
        children = self.winfo_children()
        while children:
            widget = children.pop()
            yield widget
            for child in reversed(widget.winfo_children()):
                children.append(child)

    def enable_debugging(self):
        for widget in self.walk_widget_hierarchy():
            try:
                # [TODO]: highlight additional way?
                widget.configure(borderwidth=1, relief="solid")
            except tk.TclError:
                # Widget has no 'borderwidth' option
                logging.warning(f"widget cannot be bordered: {widget!r}")
                

class PregameWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, padding=5, **kwargs)

        # --- window --- #

        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # --- namespace --- #

        self.tab_texts = {
            "mode": "Modus wählen",
            "players": "Spieler hinzufügen",
            "overview": "Spiel starten"
        }

        self.mode_selection_columns = {
            "#0": "Modus",
            "description": "Beschreibung"
        }

        self.selected_mode = tk.StringVar()

        # --- root notebook --- #

        self.root = ttk.Notebook(master=self)
        self.root.grid(row=0, column=0, sticky="nsew")

        # --- mode tab --- #

        self.mode_tab = ttk.Frame(master=self.root, padding=5)
        self.mode_tab.rowconfigure(index=0, weight=1)
        self.mode_tab.columnconfigure(index=0, weight=1)
        self.root.add(child=self.mode_tab, text=self.tab_texts["mode"])

        # --- mode tab: content frame --- #

        self.mode_content_frame = ttk.Frame(master=self.mode_tab, padding=5)
        self.mode_content_frame.grid(row=0, column=0, sticky="nsew")
        self.mode_content_frame.rowconfigure(index=0, weight=1)
        self.mode_content_frame.columnconfigure(index=0, weight=1)

        # WTF?!
        # [TODO]:
        # - lock user on tab until a selection is made
        # - save selected mode
        # - dynamically add/configure columns if it makes sense
        # - calculate minwidth for 'Modus' based on longest 'display_name'
        self.mode_select_mode_tre = ttk.Treeview(
            master=self.mode_content_frame, columns=("description"),
            selectmode="browse"
        )
        self.mode_select_mode_tre.column(column="#0", stretch=tk.NO)
        self.mode_select_mode_tre.column(column="description", anchor="w")
        self.mode_select_mode_tre.heading(
            column="#0", text=self.mode_selection_columns["#0"]
        )
        self.mode_select_mode_tre.heading(
            column="description",
            text=self.mode_selection_columns["description"]
        )
        for game in games.METADATA.games:
            self.mode_select_mode_tre.insert(
                parent="", index=tk.END, text=game.display_name,
                values=(game.description,)
            )
        self.mode_select_mode_tre.grid(row=0, column=0, sticky="nsew")

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

        if self.debug:
            self.enable_debugging()

        # --- logic --- #

        self.root.hide(tab_id=self.players_tab)
        self.root.hide(tab_id=self.overview_tab)
        self.goto_players_tab_btn.state(["disabled"])
        self.mode_select_mode_tre.bind(
            "<<TreeviewSelect>>", lambda e: self.handle_mode_selection()
        )


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

class GameWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PostgameWindow(Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Game():
    def __init__(self):
        pass


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog=_PROG)
    parser.add_argument(
        "-d", "--debug", action="store_true", default=False, dest="debug",
        help="highlight widgets and be verbose"
    )
    return parser.parse_args()

def main():
    args = parse_args()
    app = App(debug=args.debug)
    app.mainloop()

if __name__ == "__main__":
    main()
