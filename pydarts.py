import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(string="PyDarts")
        self.minsize(width=800, height=600)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.game = Game()
        self.pregame_window = PregameWindow(parent=self)
        self.game_window = GameWindow(parent=self)
        self.postgame_window = PostgameWindow(parent=self)

        self.show_pregame_window()

    def show_pregame_window(self):
        self.pregame_window.grid(row=0, column=0, sticky="nsew")


class PregameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        # --- window --- #

        super().__init__(master=parent, padding=5)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # --- namespace --- #

        self.tab_texts = {
            "mode":"Modus", "players":"Spieler", "overview": "Übersicht"
        }

        # --- root notebook --- #
        self.root = ttk.Notebook(master=self)
        self.root.grid(row=0, column=0, sticky="nsew")

        # --- mode tab --- #

        self.tab_mode = ttk.Frame(master=self.root, padding=5)
        self.tab_mode.rowconfigure(index=0, weight=1)
        self.tab_mode.columnconfigure(index=0, weight=1)
        self.root.add(
            child=self.tab_mode,
            text=self.tab_texts["mode"]
        )

        self.btn_goto_players_tab = ttk.Button(
            master=self.tab_mode,
            text=">>",
            command=self.goto_players_tab
        )
        self.btn_goto_players_tab.grid(
            row=1, column=1,
            sticky="se"
        )

        # --- players tab --- #

        self.tab_players = ttk.Frame(master=self.root, padding=5)
        self.tab_players.rowconfigure(0, weight=1)
        self.tab_players.columnconfigure(index=0, weight=1)
        self.root.add(
            child=self.tab_players,
            text=self.tab_texts["players"]
        )

        self.btn_goto_mode_tab = ttk.Button(
            master=self.tab_players,
            text="<<",
            command=self.goto_mode_tab
        )
        self.btn_goto_mode_tab.grid(
            row=1, column=0,
            sticky="sw"
        )

        self.btn_goto_overview_tab = ttk.Button(
            master=self.tab_players,
            text=">>",
            command=self.goto_overview_tab
        )
        self.btn_goto_overview_tab.grid(
            row=1, column=1,
            sticky="se"
        )

        # --- overview tab --- #

        self.tab_overview = ttk.Frame(master=self.root, padding=5)
        self.tab_overview.rowconfigure(0, weight=1)
        self.tab_overview.columnconfigure(index=0, weight=1)
        self.root.add(
            child=self.tab_overview,
            text=self.tab_texts["overview"]
        )

        self.btn_goto_players_tab = ttk.Button(
            master=self.tab_overview,
            text="<<",
            command=self.goto_players_tab
        )
        self.btn_goto_players_tab.grid(
            row=1, column=0,
            sticky="sw"
        )

        self.btn_start_game = ttk.Button(
            master=self.tab_overview,
            text="Start!",
            command=self.start_game
        )
        self.btn_start_game.grid(
            row=1, column=1,
            sticky="se"
        )

    def start_game(self):
        print(self)

    def goto_mode_tab(self):
        self.root.select(self.tab_mode)

    def goto_players_tab(self):
        self.root.select(self.tab_players)

    def goto_overview_tab(self):
        self.root.select(self.tab_overview)

class GameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(master=parent, padding=5)


class PostgameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(master=parent, padding=5)


class Game():
    def __init__(self):
        pass


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
