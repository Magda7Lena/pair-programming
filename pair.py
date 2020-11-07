# Memory Game - Pair programming

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



def main():
    level = chose_level()
    players_table = init_table(level)
    hide_table = init_table(level)



main()