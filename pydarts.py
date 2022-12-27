import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.players = []

        # ------------------------------------------------------------------- #
        
        self.title("PyDarts")
        self.geometry("600x450")

        self.grid_rowconfigure(0)
        self.grid_columnconfigure((0, 1), weight=1)

        self.entry_add_player = ctk.CTkEntry(
            master=self,
            placeholder_text="Wer spielt?"
        )
        self.entry_add_player.grid(
            row=0, column=0,
            padx=20, pady=20,
            sticky="ew"
        )

        self.button_add_player = ctk.CTkButton(
            master=self,
            command=self.add_player,
            text="Hinzufügen"
        )
        self.button_add_player.grid(
            row=0, column=1,
            padx=20, pady=20,
            sticky="ew"
        )

        self.textbox_players = ctk.CTkTextbox(
            master=self,
            state="disabled"
        )
        self.textbox_players.grid(
            row=1, column=0,
            columnspan=2,
            padx=20, pady=0,
            sticky="nsew"
        )
    
    def add_player(self) -> None:
        player = self.entry_add_player.get().strip()
        self.entry_add_player.delete(0, len(player))
        if not self.is_valid_player(player):
            return None
        
        self.players.append(player)
        self.textbox_players.configure(state="normal")
        self.textbox_players.insert(
            "insert",
            f"{self.players[len(self.players)-1]}\n"
        )
        self.textbox_players.configure(state="disabled")
        return None

    def is_valid_player(self, player: str) -> bool:
        if not player:
            return False
        return True


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
