import tkinter as tk
import tkinter.ttk as ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title(string="PyDarts")
        self.minsize(width=400, height=300)
        self.rowconfigure(index=0, weight=1)
        self.columnconfigure(index=0, weight=1)

        self.pregame_window = PregameWindow(self)
        self.game_window = GameWindow(self)
        self.postgame = PostgameWindow(self)

        self.show_pregame_window()

    def show_pregame_window(self):
        self.pregame_window.grid(row=0, column=0, sticky=("n", "s", "e", "w"))


class PregameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(master=parent)

        self.notebook = ttk.Notebook(master=self)
        self.notebook.grid(row=0, column=0, sticky=("n", "s", "e", "w"))

        self.game_tab = ttk.Frame(master=self.notebook)
        self.notebook.add(child=self.game_tab, text="Spiel")

        self.players_tab = ttk.Frame(master=self.notebook)
        self.notebook.add(child=self.players_tab, text="Spieler")

        self.overview_tab = ttk.Frame(master=self.notebook)
        self.notebook.add(child=self.overview_tab, text="Übersicht")


class GameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(master=parent)


class PostgameWindow(ttk.Frame):
    def __init__(self, parent: tk.Tk):
        super().__init__(master=parent)



def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
