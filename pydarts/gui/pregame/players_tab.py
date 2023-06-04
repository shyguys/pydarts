import tkinter as tk
import tkinter.ttk as ttk

import pydarts.gui.pregame.texts


class _Prompt():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._label = ttk.Label(master=self._root)
        self._entry = ttk.Entry(master=self._root)
        self._add = ttk.Button(master=self._root)
        self._player_to_add = tk.StringVar()
        self._texts = pydarts.gui.pregame.texts.PLAYERS_TAB["prompt"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()
        self._build_label()
        self._build_entry()
        self._build_add()

    def _build_root(self):
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        widget.grid(row=0, column=0, sticky="nsew")
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)
        widget.columnconfigure(index=2, weight=1)

    def _build_label(self):
        text: str = self._texts["label"]["title"]
        widget = self._label
        widget.configure(text=text, takefocus=0)
        widget.grid(row=0, column=0, sticky="nse")

    def _build_entry(self):
        widget = self._entry
        widget.grid(row=0, column=1, sticky="nsew", padx=5)

    def _build_add(self):
        text: str = self._texts["add"]["title"]
        widget = self._add
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsw")

    def _bind(self):
        self._bind_players_var()
        self._bind_entry()
        self._bind_add()

    def _bind_players_var(self):
        pydarts.gui.pregame.Vars.players.trace_add(
            "write", self._handle_players_write)

    def _bind_entry(self):
        self._entry.configure(textvariable=self._player_to_add)
        self._entry.bind(
            "<KeyRelease-Return>", self._handle_key_release_return_in_entry
        )

    def _bind_add(self):
        self._add.configure(command=self._handle_add)

    def _handle_players_write(self, *args, **kwargs):
        if pydarts.gui.pregame.Vars.players.get() == 0:
            self._entry.focus_set()

    def _handle_key_release_return_in_entry(self, event: tk.Event = None):
        self._add.invoke()

    def _handle_add(self, event: tk.Event = None) -> None:
        self._entry.focus_set()
        player_name = self._player_to_add.get().strip()
        self._player_to_add.set("")

        if not self._is_valid_player_name(player_name):
            # [TODO] notify user somehow
            return None

        players = pydarts.gui.pregame.Vars.players.get()
        players.append(player_name)
        pydarts.gui.pregame.Vars.players.set(players)
        return None

    def _is_valid_player_name(self, player_name: str) -> bool:
        if not player_name:
            return False

        players = pydarts.gui.pregame.Vars.players.get()
        if player_name in players:
            return False

        if len(players) == pydarts.gui.pregame.Vars.player_limit.get():
            return False
        return True


class _Controls():
    def __init__(self, parent: ttk.Frame):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._move_top = ttk.Button(master=self._root)
        self._move_up = ttk.Button(master=self._root)
        self._move_down = ttk.Button(master=self._root)
        self._move_bottom = ttk.Button(master=self._root)
        self._remove = ttk.Button(master=self._root)
        self._texts = pydarts.gui.pregame.texts.PLAYERS_TAB["controls"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Frame:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()
        self._build_move_top()
        self._build_move_up()
        self._build_move_down()
        self._build_move_bottom()
        self._build_remove()

    def _build_root(self):
        widget = self._root
        widget.configure(takefocus=0)
        widget.grid(row=2, column=0, sticky="nsew", pady=(5, 0))
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)
        widget.columnconfigure(index=1, weight=1)
        widget.columnconfigure(index=2, weight=1)
        widget.columnconfigure(index=3, weight=1)
        widget.columnconfigure(index=4, weight=1)

    def _build_move_top(self):
        text: str = self._texts["move_top"]["title"]
        widget = self._move_top
        widget.configure(text=text)
        widget.grid(row=0, column=0, sticky="nsew")

    def _build_move_up(self):
        text: str = self._texts["move_up"]["title"]
        widget = self._move_up
        widget.configure(text=text)
        widget.grid(row=0, column=1, sticky="nsew")

    def _build_move_down(self):
        text: str = self._texts["move_down"]["title"]
        widget = self._move_down
        widget.configure(text=text)
        widget.grid(row=0, column=2, sticky="nsew")

    def _build_move_bottom(self):
        text: str = self._texts["move_bottom"]["title"]
        widget = self._move_bottom
        widget.configure(text=text)
        widget.grid(row=0, column=3, sticky="nsew")

    def _build_remove(self):
        text: str = self._texts["remove"]["title"]
        widget = self._remove
        widget.configure(text=text)
        widget.grid(row=0, column=4, sticky="nsew")

    def _bind(self):
        self._bind_players_var()
        self._bind_move_top()
        self._bind_move_up()
        self._bind_move_down()
        self._bind_move_bottom()
        self._bind_remove()

    def _bind_players_var(self):
        pydarts.gui.pregame.Vars.players.trace_add(
            "write", self._handle_players_write)

    def _bind_move_top(self):
        self._move_top.configure(command=self._handle_move_top)

    def _bind_move_up(self):
        self._move_up.configure(command=self._handle_move_up)

    def _bind_move_down(self):
        self._move_down.configure(command=self._handle_move_down)

    def _bind_move_bottom(self):
        self._move_bottom.configure(command=self._handle_move_bottom)

    def _bind_remove(self):
        self._remove.configure(command=self._handle_remove)

    def _handle_players_write(self, *args, **kwargs):
        self._toggle_controls()

    def _handle_move_top(self, event: tk.Event = None):
        self._root.event_generate(
            pydarts.gui.pregame.Event.PLAYER_MOVE_TOP_REQUESTED.value)

    def _handle_move_up(self, event: tk.Event = None):
        self._root.event_generate(
            pydarts.gui.pregame.Event.PLAYER_MOVE_UP_REQUESTED.value)

    def _handle_move_down(self, event: tk.Event = None):
        self._root.event_generate(
            pydarts.gui.pregame.Event.PLAYER_MOVE_DOWN_REQUESTED.value)

    def _handle_move_bottom(self, event: tk.Event = None):
        self._root.event_generate(
            pydarts.gui.pregame.Event.PLAYER_MOVE_BOTTOM_REQUESTED.value)

    def _handle_remove(self, event: tk.Event = None):
        self._root.event_generate(
            pydarts.gui.pregame.Event.PLAYER_REMOVE_REQUESTED.value)

    def _toggle_controls(self):
        controls = [
            self._move_top, self._move_up, self._move_down, self._move_bottom,
            self._remove
        ]

        if len(pydarts.gui.pregame.Vars.players.get()) == 0:
            state = ["disabled"]
        else:
            state = ["!disabled"]

        for control in controls:
            control.state(state)


class Root():
    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._prompt = _Prompt(parent=self.root)
        self._view = ttk.Treeview(master=self._root)
        self._controls = _Controls(parent=self._root)
        self._texts = pydarts.gui.pregame.texts.PLAYERS_TAB["root"]
        self._build()
        self._bind()

    @property
    def parent(self) -> ttk.Notebook:
        return self._parent

    @property
    def root(self) -> ttk.Frame:
        return self._root

    def _build(self):
        self._build_root()
        self._build_view()

    def _build_root(self):
        text: str = self._texts["title"]
        widget = self._root
        widget.configure(padding=5, takefocus=0)
        self._parent.add(child=widget, text=text)
        widget.rowconfigure(index=1, weight=1)
        widget.columnconfigure(index=0, weight=1)

    def _build_view(self):
        texts: dict[str, str] = self._texts["view"]["columns"]
        widget = self._view

        widget.configure(
            columns=list(texts)[1:], selectmode="browse", takefocus=0
        )
        widget.grid(row=1, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="player", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

    def _bind(self):
        self._bind_players_var()
        self._bind_move_top_request()
        self._bind_move_up_request()
        self._bind_move_down_request()
        self._bind_move_bottom_request()
        self._bind_remove_requested()

    def _bind_players_var(self):
        pydarts.gui.pregame.Vars.players.trace_add(
            "write", self._handle_players_write)

    def _bind_move_top_request(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PLAYER_MOVE_TOP_REQUESTED.value,
            self._handle_move_top_request
        )

    def _bind_move_up_request(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PLAYER_MOVE_UP_REQUESTED.value,
            self._handle_move_up_request
        )

    def _bind_move_down_request(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PLAYER_MOVE_DOWN_REQUESTED.value,
            self._handle_move_down_request
        )

    def _bind_move_bottom_request(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PLAYER_MOVE_BOTTOM_REQUESTED.value,
            self._handle_move_bottom_request
        )

    def _bind_remove_requested(self):
        self._root.bind_all(
            pydarts.gui.pregame.Event.PLAYER_REMOVE_REQUESTED.value,
            self._handle_remove_requested
        )

    def handle_change_to_self(self, event: tk.Event = None):
        ...

    def _handle_players_write(self, *args, **kwargs):
        self._update_view()

    def _handle_move_top_request(self, event: tk.Event = None):
        selection = self._view.selection()
        if not selection:
            return None

        index = self._view.index(self._view.selection()[0])
        if index == 0:
            return None

        self._move_player(index, 0)
        return None

    def _handle_move_up_request(self, event: tk.Event = None):
        selection = self._view.selection()
        if not selection:
            return None

        index = self._view.index(self._view.selection()[0])
        if index == 0:
            return None

        self._move_player(index, index-1)
        return None

    def _handle_move_down_request(self, event: tk.Event = None):
        selection = self._view.selection()
        if not selection:
            return None

        index = self._view.index(self._view.selection()[0])
        if index == len(self._view.get_children())-1:
            return None

        self._move_player(index, index+1)
        return None

    def _handle_move_bottom_request(self, event: tk.Event = None):
        selection = self._view.selection()
        if not selection:
            return None

        index = self._view.index(self._view.selection()[0])
        last_index = len(self._view.get_children())-1
        if index == last_index:
            return None

        self._move_player(index, last_index)
        return None

    def _handle_remove_requested(self, event: tk.Event = None) -> None:
        selection = self._view.selection()
        if not selection:
            return None

        index = self._view.index(self._view.selection()[0])
        players = pydarts.gui.pregame.Vars.players.get()
        players.pop(index)
        pydarts.gui.pregame.Vars.players.set(players)

        if not self._view.get_children():
            return None

        if index == len(self._view.get_children()):
            new_index = index-1
        else:
            new_index = index

        self._view.selection_set(self._view.get_children()[new_index])
        return None

    def _is_valid_player_name(self, player_name: str) -> bool:
        if not player_name:
            return False

        players = pydarts.gui.pregame.Vars.players.get()
        if player_name in players:
            return False

        if len(players) == pydarts.gui.pregame.Vars.player_limit.get():
            return False
        return True

    def _move_player(self, current_index: int, new_index: int):
        players = pydarts.gui.pregame.Vars.players.get()
        players.insert(new_index, players.pop(current_index))
        pydarts.gui.pregame.Vars.players.set(players)
        self._view.selection_set(self._view.get_children()[new_index])

    def _update_view(self):
        for item in self._view.get_children():
            self._view.delete(item)

        for position, player in enumerate(pydarts.gui.pregame.Vars.players.get(), start=1):
            self._view.insert(
                parent="", index=tk.END, text=position, values=(player,)
            )
