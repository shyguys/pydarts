import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(string="PyDarts")
        self.minsize(width=400, height=300)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        # --- PREGAME --- #

        self.pregame_parent = ttk.Frame(master=self, padding=5)
        self.pregame_parent.grid(row=0, column=0, sticky=("n", "s", "e", "w"))

        self.pregame_notebook = ttk.Notebook(master=self.pregame_parent)
        self.pregame_notebook.grid(row=0, column=0, sticky=("n", "s", "e", "w"))

        self.pregame_game_parent = ttk.Frame(master=self.pregame_notebook)
        self.pregame_notebook.add(child=self.pregame_game_parent, text="Spiel")

        self.pregame_players_parent = ttk.Frame(master=self.pregame_notebook)
        self.pregame_notebook.add(child=self.pregame_players_parent, text="Spieler")

        self.pregame_overview_parent = ttk.Frame(master=self.pregame_notebook)
        self.pregame_notebook.add(child=self.pregame_overview_parent, text="Übersicht")

        # --- GAME --- #

        pass

        # --- POSTGAME --- #

        pass


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
