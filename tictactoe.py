# 0,0 0,1 0,2
# 1,0 1,1 1,2
# 2,0 2,1 2,2
import random
table = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]



#turns
def turns():
    print_table(table)
    available_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    possible_win = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],
                    [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],
                    [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)] ]
    user_made_moves = []
    computer_made_moves = []
    while True:
        user_coordinates = user_turn()
        user_made_moves = assign_coordinates(user_coordinates, user_made_moves, "x", available_moves)
        user_win = check_win(user_made_moves, possible_win)
        print_table(table)
        if user_win:
            print("You won!")
            break
        tie = check_tie(available_moves)
        if tie:
            print("It's a tie!")
            break
        print("Computer turn")
        computer_coordinates = computer_turn(available_moves)
        assign_coordinates(computer_coordinates, computer_made_moves, "o", available_moves)
        computer_win = check_win(computer_made_moves, possible_win)
        print_table(table)
        if computer_win:
            print("Computer won!")
            break
        tie = check_tie(available_moves)
        if tie:
            print("It's a tie!")
            break
#check if game over / write who won
def check_win(chosen_coordinates, win_coordinations):
    for win_combination in win_coordinations:
        if set(win_combination).issubset(set(chosen_coordinates)):
            return True
    return False

#check tie
def check_tie(available_moves):
    return not available_moves


#user turn
def user_turn():
    user_input = input("Your turn (x, y): ")
    (x, y) = user_input.split(", ")
    return (int(x), int(y))

#computer turn
def computer_turn(existing_coordinations):
    random_coordinates = random.choice(existing_coordinations)
    return random_coordinates

#assignment
def assign_coordinates(coordinates, made_moves, mark, possible_moves):
    made_moves.append(coordinates)
    table[coordinates[0]][coordinates[1]] = mark
    possible_moves.remove(coordinates)
    return made_moves
def print_table(table):
    print("+---|---|---+")
    for row in table:
        print("|", end="")
        for cell in row:
            print(f" {cell} |", end="")
        print("\n+---|---|---+")
turns()
