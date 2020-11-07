# Memory Game - Pair programming
import string
import random

def chose_level():
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


def main():
    level = chose_level()
    players_table = init_table(level)

    hide_table = get_random_letters(players_table)
    print_table(hide_table)




def get_random_letters(board):
    size = len(board)
    alphabet = list(string.ascii_uppercase) 
    letters = []
    while len(letters) < size / 2:
        letter = random.choice(alphabet)
        if not letter in letters:
            letters.append(letter)
    letters += letters
    # letters = random.shuffle(letters)
    letters = random.sample(letters, k = size)
    # letters = list(letters)
    print(letters)
    return letters



main()