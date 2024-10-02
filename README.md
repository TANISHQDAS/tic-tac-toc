Hello, friends! 😊

In this project, I built a simple Tic-Tac-Toe game using Python and Tkinter. It features a user-friendly interface for two players to compete against each other!

Here's the code in brief:
Setup

We import the necessary modules: tkinter for creating the GUI and messagebox for displaying messages.
We define a class named TicTacToe to encapsulate all functionalities of our application.
Setting up the App

We create an instance of the TicTacToe class to set up the main window with the title "Tic-Tac-Toe" and a black background.
A label at the top indicates whose turn it is, with colors changing based on the player.
Creating Buttons

We dynamically create buttons for the Tic-Tac-Toe grid.
Each button handles player clicks and updates the game state accordingly.
The game checks for a win or a draw after each move and informs the players.
Game Logic

The check_winner method evaluates the game board to determine if there is a winner.
The check_draw method checks if the game ends in a draw.
Playing Again

After a win or a draw, players are prompted to play again or exit.
Running the App
Finally, we run the application with its GUI live and responsive by using window.mainloop()

