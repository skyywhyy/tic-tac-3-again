import tkinter as tk

counter = 0
current_player = None
cell_size = 100
cell_otst = 5
game_board = [[" " for x in range(3)] for y in range(3)]

def check_winner():
    winner_found = False
    for i in range(3):
        # Проверка горизонтальных линий
        if game_board[i][0] == game_board[i][1] == game_board[i][2] != " ":
            winner(game_board[i][0])
            winner_found = True
            break
        # Проверка вертикальных линий
        if game_board[0][i] == game_board[1][i] == game_board[2][i] != " ":
            winner(game_board[0][i])
            winner_found = True
            break
    # Проверка диагоналей
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != " ":
        winner(game_board[0][0])
        winner_found = True
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] != " ":
        winner(game_board[0][2])
        winner_found = True

    # Проверка на ничью, если все ячейки заполнены и победителя нет
    if not winner_found and counter == 9:
        end_game("Ничья...")
    
def winner(player):
    if player == "X":
        winner_label.config(text="Игрок X победил!")
    elif player == "O":
        winner_label.config(text="Игрок O победил!")
    end_game(player)

def end_game(winner):
    board.unbind("<Button-1>")  # Отключаем клики по полю
    endgame_window = tk.Toplevel(window) 
    endgame_window.title("Игра окончена")
    label = tk.Label(endgame_window, text=f"Победитель: {winner}" if winner != "Ничья..." else "Ничья...", font=("Arial", 18))
    label.pack()
    close_button = tk.Button(endgame_window, text="Закрыть", command=window.quit)
    close_button.pack()

def start_game(player):
    global current_player, counter
    current_player = player
    # counter = 0
    main_menu.destroy()


def draw_symbol(row, col):
    x_center = col * cell_size + cell_size // 2
    y_center = row * cell_size + cell_size // 2
    symbol = game_board[row][col]
    if symbol == "X":
        board.create_text(x_center, y_center, text="X", font=("Arial", 24), fill="blue")
    elif symbol == "O":
        board.create_text(x_center, y_center, text="O", font=("Arial", 24), fill="red")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def on_cell(event):
    global counter
    x, y = event.x, event.y
    col = x // cell_size
    row = y // cell_size
    if game_board[row][col] == " ":
        game_board[row][col] = current_player
        draw_symbol(row, col)
        counter += 1
        switch_player()

def choose_player():
    main_menu.title("Выберите начинающего игрока")
    label = tk.Label(main_menu, text="Выберите начинающего игрока:")
    label.pack()
    btn_x = tk.Button(main_menu, text="Игрок X", command=lambda: start_game("X"))
    btn_o = tk.Button(main_menu, text="Игрок O", command=lambda: start_game("O")) 
    btn_x.pack()
    btn_o.pack()
    main_menu.mainloop()


#окно игры
window = tk.Tk()
main_menu = tk.Tk()
choose_player()
winner_label = tk.Label(window, text="", font=("Arial", 18))
winner_label.pack()

main_menu = tk.Menu(window)
window.config(menu=main_menu)
window = tk.Tk()
window.title("tic-tac-toe")

#игровое поле (пустая сетка)
cell_size = 100
cell_otst = 5
board = tk.Canvas(window, width=300, height=300)
board.pack()

# Создание пустой сетки
for row in range(3):
    for col in range(3):
        x1 = col * cell_size + cell_otst 
        y1 = row * cell_size + cell_otst 
        x2 = x1 + cell_size - cell_otst 
        y2 = y1 + cell_size - cell_otst 
        board.create_rectangle(x1, y1, x2, y2)

window.mainloop()

board.bind("<Button-1>", on_cell)

