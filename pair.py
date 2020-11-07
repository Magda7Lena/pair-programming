# Memory Game - Pair programming
import string
import random
import os


def chose_level():
    # printing main menu
    levels = ["1","2","3"]
    print(" 1 - easy \n 2 - medium \n 3 - hard")
    level = input("Chose level: ")
    if not level in levels:
        print("Invalind input")
        chose_level()
    return level
         
           
def init_table(level):
    level = int(level)
    if level == 1:
        x = 5
        y = 4
    elif level == 2:
        x = 5
        y = 6
    elif level == 3:
        x = 5
        y = 10
   
    board = ["#" for x in range(x*y)]
    return board
 
 
def print_table(board):
    if len(board) == 20:
        print("     1     2     3     4     5  \n---------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |\n---------------------------------")
        print(f"B |  {board[5]}  |  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}  |\n---------------------------------")
        print(f"C |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |\n---------------------------------")
        print(f"D |  {board[15]}  |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |\n---------------------------------")
    if len(board) == 30:
        print("     1     2     3     4     5  \n---------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |\n---------------------------------")
        print(f"B |  {board[5]}  |  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}  |\n---------------------------------")
        print(f"C |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |\n---------------------------------")
        print(f"D |  {board[15]}  |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |\n---------------------------------")
        print(f"E |  {board[20]}  |  {board[21]}  |  {board[22]}  |  {board[23]}  |  {board[24]}  |\n---------------------------------")
        print(f"F |  {board[25]}  |  {board[26]}  |  {board[27]}  |  {board[28]}  |  {board[29]}  |\n---------------------------------")
    if len(board) == 50:
        print("     1     2     3     4     5  \n---------------------------------")
        print(f"A |  {board[0]}  |  {board[1]}  |  {board[2]}  |  {board[3]}  |  {board[4]}  |\n---------------------------------")
        print(f"B |  {board[5]}  |  {board[6]}  |  {board[7]}  |  {board[8]}  |  {board[9]}  |\n---------------------------------")
        print(f"C |  {board[10]}  |  {board[11]}  |  {board[12]}  |  {board[13]}  |  {board[14]}  |\n---------------------------------")
        print(f"D |  {board[15]}  |  {board[16]}  |  {board[17]}  |  {board[18]}  |  {board[19]}  |\n---------------------------------")
        print(f"E |  {board[20]}  |  {board[21]}  |  {board[22]}  |  {board[23]}  |  {board[24]}  |\n---------------------------------")
        print(f"F |  {board[25]}  |  {board[26]}  |  {board[27]}  |  {board[28]}  |  {board[29]}  |\n---------------------------------")
        print(f"G |  {board[30]}  |  {board[31]}  |  {board[32]}  |  {board[33]}  |  {board[34]}  |\n---------------------------------")
        print(f"H |  {board[35]}  |  {board[36]}  |  {board[37]}  |  {board[38]}  |  {board[39]}  |\n---------------------------------")
        print(f"I |  {board[40]}  |  {board[41]}  |  {board[42]}  |  {board[43]}  |  {board[44]}  |\n---------------------------------")
        print(f"J |  {board[45]}  |  {board[46]}  |  {board[47]}  |  {board[48]}  |  {board[49]}  |\n---------------------------------")
 
 
def main():
    #controler
    level = chose_level()
    players_table = init_table(level)
 
    hide_table = get_random_letters(players_table)
    # print_table(hide_table)
    while check_win(players_table) == False:
        game_logic(players_table, hide_table)
        os.system("cls")
 
 
def get_valid_move(board):
    if len(board) == 20:
        valid_move = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5"]
        players_move = input("Please choose a position on the board: ")
        while players_move not in valid_move:
            print("Invalid move")
            get_valid_move(board)
        return players_move
    if len(board) == 30:
        valid_move = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5","e1", "e2", "e3", "e4", "e5","f1", "f2", "f3", "f4", "f5"]
        players_move = input("Please choose a position on the board: ")
        while players_move not in valid_move:
            print("Invalid move")
            get_valid_move(board)
        return players_move
    if len(board) == 50:
        valid_move = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5","e1", "e2", "e3", "e4", "e5","f1", "f2", "f3", "f4", "f5","g1", "g2", "g3", "g4", "g5","h1", "h2", "h3", "h4", "h5","i1", "i2", "i3", "i4", "i5","j1", "j2", "j3", "j4", "j5"]
        players_move = input("Please choose a position on the board: ")
        while players_move not in valid_move:
            print("Invalid move")
            get_valid_move(board)
        return players_move
       
 
def game_logic(players_table, hide_table):
    print_table(players_table)
    player_move1 = get_valid_move(players_table)
    player_move2 = get_valid_move(players_table)
    index_move1 = locate_field(player_move1, hide_table)
    index_move2 = locate_field(player_move2, hide_table)
    if hide_table[index_move1] == hide_table[index_move2]:
        players_table[index_move1] = hide_table[index_move1]
        players_table[index_move2] = hide_table[index_move2]
        print_table(players_table)
    else:
        game_logic(players_table, hide_table)
 
 
def check_win(players_table):
    if "#" in players_table:
        return False
    elif not "#" in players_table:
        print("You have won!")
        return True
 
   
def locate_field(field, board):
    if len(board) == 20:
        comparative_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5"]
        i = comparative_list.index(field)
        return i
    if len(board) == 30:
        comparative_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5","e1", "e2", "e3", "e4", "e5","f1", "f2", "f3", "f4", "f5"]
        i = comparative_list.index(field)
        return i
    if len(board) == 50:
        comparative_list = ["a1", "a2", "a3", "a4", "a5", "b1", "b2", "b3", "b4", "b5", "c1", "c2", "c3", "c4", "c5", "d1", "d2", "d3", "d4", "d5","e1", "e2", "e3", "e4", "e5","f1", "f2", "f3", "f4", "f5","g1", "g2", "g3", "g4", "g5","h1", "h2", "h3", "h4", "h5","i1", "i2", "i3", "i4", "i5","j1", "j2", "j3", "j4", "j5"]
        i = comparative_list.index(field)
        return i
 
 
def get_random_letters(board):
    size = len(board)
    alphabet = list(string.ascii_lowercase)
    letters = []
    while len(letters) < size / 2:
        letter = random.choice(alphabet)
        if not letter in letters:
            letters.append(letter)
    letters += letters
    letters = random.sample(letters, k = size)
    return letters
 
 
if __name__ == '__main__':
    main()
