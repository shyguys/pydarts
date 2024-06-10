import tkinter as tk
import tkinter.ttk as ttk


class Root(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, padding="10")
        self.columnconfigure(index=0, weight=1)
        self.columnconfigure(index=2, weight=1)
        self.rowconfigure(index=0, weight=1)

        self.game = Game(self)
        self.game.grid_propagate(False)
        self.game.grid(column=0, row=0, sticky="NSWE")

        self.seperator = ttk.Separator(self, orient="vertical")
        self.seperator.grid(column=1, row=0, sticky="NSEW", padx=10)

        self.players = Players(self)
        self.players.grid_propagate(False)
        self.players.grid(column=2, row=0, sticky="NSWE")
        return None


class Game(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.columnconfigure(index=1, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.label = ttk.Label(self, text="Select a game mode: ")
        self.label.grid(column=0, row=0, sticky="NSWE")

        self.selection_value = tk.StringVar()
        self.selection = ttk.Combobox(self, textvariable=self.selection_value)
        self.selection.grid(column=1, row=0, sticky="NSWE")

        self.description = ttk.Label(self, anchor="nw", padding="0 5 0 0", wraplength=300)
        self.description.grid(column=0, row=1, columnspan=2, sticky="NSWE")
        return None


class Players(ttk.Frame):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=1, weight=1)

        self.entry_frame = ttk.Frame(self)
        self.entry_frame.columnconfigure(index=1, weight=1)
        self.entry_frame.grid(column=0, row=0, sticky="NSWE")
        self.label = ttk.Label(self.entry_frame, text="Provide a player name: ")
        self.label.grid(column=0, row=0, sticky="NSWE")
        self.entry_value = tk.StringVar()
        self.entry = ttk.Entry(self.entry_frame, textvariable=self.entry_value)
        self.entry.grid(column=1, row=0, sticky="NSWE")
        self.add = ttk.Button(self.entry_frame, text="+", width=5)
        self.add.grid(column=2, row=0, sticky="NSWE", padx=(5, 0))

        self.overview_frame = ttk.Frame(self)
        self.overview_frame.columnconfigure(index=0, weight=1)
        self.overview_frame.rowconfigure(index=0, weight=1)
        self.overview_frame.grid(column=0, row=1, sticky="NSWE", pady=10)
        self.overview = ttk.Treeview(self.overview_frame)
        self.overview.grid(column=0, row=0, sticky="NSWE")

        self.controls_frame = ttk.Frame(self)
        self.controls_frame.columnconfigure(index=0, weight=1)
        self.controls_frame.columnconfigure(index=1, weight=1)
        self.controls_frame.columnconfigure(index=2, weight=1)
        self.controls_frame.grid(column=0, row=2, sticky="NSWE")
        self.remove = ttk.Button(self.controls_frame, text="-")
        self.remove.grid(column=0, row=0, sticky="NSWE", padx=(0, 5))
        self.move_up = ttk.Button(self.controls_frame, text="∧")
        self.move_up.grid(column=1, row=0, sticky="NSWE", padx=(5, 5))
        self.move_down = ttk.Button(self.controls_frame, text="∨")
        self.move_down.grid(column=2, row=0, sticky="NSWE", padx=(5, 0))
        return None
