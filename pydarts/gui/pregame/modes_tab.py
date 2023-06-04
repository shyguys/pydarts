import tkinter as tk
import tkinter.ttk as ttk

import pydarts.core.metadata as metadata
import pydarts.gui.pregame.texts


class Root():
    def __init__(self, parent: ttk.Notebook):
        self._parent = parent
        self._root = ttk.Frame(master=self._parent)
        self._view = ttk.Treeview(master=self._root)
        self._texts = pydarts.gui.pregame.texts.MODES_TAB["root"]
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
        widget.rowconfigure(index=0, weight=1)
        widget.columnconfigure(index=0, weight=1)

    # [TODO]: calculate width for '#0' based on longest 'name'?
    def _build_view(self):
        widget = self._view
        texts: dict[str, str] = self._texts["view"]["columns"]

        widget.configure(
            columns=list(texts)[1:], selectmode="browse", takefocus=0
        )
        widget.grid(row=0, column=0, sticky="nsew")
        widget.column(column="#0", stretch=tk.NO)
        widget.column(column="description", anchor="w")

        for key, value in texts.items():
            widget.heading(column=key, text=value)

        for mode in metadata.Modes.get_modes():
            widget.insert(
                parent="", index=tk.END, text=mode.name,
                values=(mode.description,)
            )

    def _bind(self):
        self._bind_view()

    def _bind_view(self):
        self._view.bind("<<TreeviewSelect>>", self._handle_selection)

    def _handle_selection(self, event: tk.Event = None):
        item = self._view.selection()[0]
        index = self._view.index(item)
        mode_id = metadata.Modes.get_modes()[index].id
        pydarts.gui.pregame.Vars.mode_id.set(mode_id)
