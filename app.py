from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout

class TicTacToe(App):
    def build(self):
        self.result_label = Label(text="Tic-Tac-Toe", font_size=32)
        self.board = [""] * 9
        self.active_player = 'X'
        self.buttons = []
        self.game_over = False  # Flag to indicate whether the game is over

        layout = GridLayout(cols=3)
        for i in range(9):
            button = Button()
            button.bind(on_release=lambda button=button: self.on_button_click(button))
            self.buttons.append(button)
            layout.add_widget(button)
        
        self.reset_button = Button(text="Next Game", size_hint=(None, None), size=(200, 50))
        self.reset_button.bind(on_release=self.reset_game)

        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='bottom')
        anchor_layout.add_widget(self.reset_button)

        main_layout = BoxLayout(orientation="vertical")
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(layout)
        main_layout.add_widget(anchor_layout)

        return main_layout
    
    def on_button_click(self, button):
        if not self.game_over:  # Check if the game is not over
            index = self.buttons.index(button)
            if self.board[index] == "":
                self.board[index] = self.active_player
                button.text = self.active_player
                if self.check_winner() or self.is_board_full():
                    self.result_label.text = "Game Over You Won"
                    self.game_over = True  # Set the game over flag

                    # Disable further input by making all buttons disabled
                    for button in self.buttons:
                        button.disabled = True
                else:
                    self.active_player = 'O' if self.active_player == 'X' else 'X'

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # vertical
            [0, 4, 8], [2, 4, 6]              # diagonal
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and (self.board[combo[0]] != ""):
                self.result_label.text = f"{self.active_player} wins!"
                return True
        return False
    
    def is_board_full(self):
        return "" not in self.board

    def reset_game(self, button):
        for i in range(9):
            self.board[i] = ""
            self.buttons[i].text = ""
            self.buttons[i].disabled = False  # Enable all buttons
        self.active_player = 'X'
        self.result_label.text = "Tic-Tac-Toe"
        self.game_over = False  # Reset the game over flag

if __name__ == "__main__":
    TicTacToe().run()
