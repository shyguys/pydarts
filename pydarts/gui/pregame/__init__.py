import tkinter as tk
from enum import Enum

import pydarts.help.tkh as tkh
from pydarts.gui.pregame.root import Root


class Event(Enum):
    PLAYER_MOVE_TOP_REQUESTED = "<<PlayerControlsMoveTopRequested>>"
    PLAYER_MOVE_UP_REQUESTED = "<<PlayerControlsMoveUpRequested>>"
    PLAYER_MOVE_DOWN_REQUESTED = "<<PlayerControlsMoveDownRequested>>"
    PLAYER_MOVE_BOTTOM_REQUESTED = "<<PlayerControlsMoveBottomRequested>>"
    PLAYER_REMOVE_REQUESTED = "<<PlayerControlsRemoveRequested>>"
    TAB_GO_BACK_REQUESTED = "<<BottomBarGoBackRequested>>"
    TAB_GO_NEXT_REQUESTED = "<<BottomBarGoNextRequested>>"
    OVERVIEW_TAB_FINISHED = "<<OverviewTabFinished>>"
    PREGAME_WINDOW_FINISHED = "<<PregameWindowFinished>>"


class Vars():
    """Module level tk.Variable's for event control."""

    mode_id: tk.StringVar
    player_limit: tk.IntVar
    players: tkh.ListVar
    is_first_tab_active: tk.BooleanVar
    is_last_tab_active: tk.BooleanVar

    @classmethod
    def init(cls):
        """Inititalizes variables.

        Has do be called after the root window has been created.
        """

        cls.mode_id = tk.StringVar()
        cls.player_limit = tk.IntVar()
        cls.players = tkh.ListVar()
        cls.is_first_tab_active = tk.BooleanVar()
        cls.is_last_tab_active = tk.BooleanVar()
