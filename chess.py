board_size = 8
def main():
    new_board = make_new_board(board_size)
    print_board(new_board)

    #white pieces are handled
    white_player_move, piece =  white_pieces()
    assign_coordinates(white_player_move, piece, new_board)
    print_board(new_board)

    #black pieces
    black_pieces(new_board)

    #bring the taken pieces and convert to chess coordinates, finally - print
    pieces, taken_pieces_coordinates = white_piece_takes(white_player_move, new_board)
    print_final_taken_pieces(pieces, taken_pieces_coordinates)


#create a board
def make_new_board(size):
    board = []
    for i in range(size):
        row = []
        for j in range(size):
            if (i + j)% 2 == 0:
                row.append("□")
            else:
                row.append("■")
        board.append(row)
    return board

#printing board
def print_board(board):
    for row in board:
        print (" ".join(row))


#convert coordinates
def convert_coordinates(coordinates):
    if len(coordinates) != 2 or not coordinates[0].isalpha() or not coordinates[1].isnumeric():
        return None
    col = ord(coordinates[0].lower()) - ord("a")
    row = 8 - int(coordinates[1])
    if col < 0 or col > 7 or row > 7:
        return None
    return row, col


#validate input
def validate_input(validate_coordinates, piece, pieces):
    if validate_coordinates is None:
            print("Invalid coordinates, please choose within a1 - h8 range")
            return False
    if piece.lower() not in pieces:
            print("Invalid piece, please choose between pawn and rook")
            return False
    return True

#user input (white)
# choose one piece (pawn or rook) and coordinates (pawn a5)
def white_pieces():
    valid_input = False
    pieces = ["pawn", "rook"]
    while not valid_input:
        try:
            white_piece = input("Choose one white piece (pawn or rook) and it's coordinates (for ex.: pawn a5): ")
            piece, piece_coordinates = white_piece.split(" ")
            valid_coordinates = convert_coordinates(piece_coordinates)
            is_valid = validate_input(valid_coordinates, piece, pieces)
            if not is_valid:
                continue
            valid_input = True
        except:
            print("Invalid input")
        print("Piece added successfully:")
    return (valid_coordinates, piece[0].upper())



#user input (black)
def black_pieces(board):
    pieces_coordinates = []
    count = 0
    pieces = ["pawn", "rook"]
    while count < 16:

        black_piece = input("Enter 1 - 16 black pawns or rooks with their coordinates (e.g., 'pawn a5'), pressing Enter after each, or type 'done' to finish early: ")
        if black_piece.lower() == "done":
            if count == 0:
                print("You must place at least one black piece")
                continue
            break
        try:
            piece, piece_coordinates = black_piece.split(" ")
            valid_coordinates = convert_coordinates(piece_coordinates)
            is_valid = validate_input(valid_coordinates, piece, pieces)
            if not is_valid:
                continue
            if assign_coordinates(valid_coordinates, piece[0].lower(), board):
                count += 1
                pieces_coordinates.append(valid_coordinates)
                print("Piece added successfully:")
            else:
                print("This spot is already occupied")
                continue
        except:
            print("Invalid input")
        print_board(board)
    return pieces_coordinates


#assigning piece coordinates to board
def assign_coordinates(coordinates, piece, board):
    row, col = coordinates
    if board[row][col] in ['□', '■']:
        board[row][col] = piece
        return True
    return False

# check what black pieces can a white piece take
def white_piece_takes(white_coordinates, board):
    taken_black_mark = []
    taken_black_coordinates = []
    pieces = ["r", "p"]
    row, col = white_coordinates
    white_piece = board[row][col]
    if white_piece == "P":


        if board[row - 1][col + 1] in pieces:
            taken_black_mark.append([board[row - 1][col + 1]])
            taken_black_coordinates.append((row - 1, col + 1))
        if board[row - 1][col - 1] in pieces:
            taken_black_mark.append([board[row - 1][col - 1]])
            taken_black_coordinates.append((row - 1, col - 1))
    else:
        up = 1
        while (row - up) >= 0:
            if board[row - up][col] in pieces:
              taken_black_mark.append([board[row - up][col]])
              taken_black_coordinates.append((row - up, col))
              break
            up += 1
        down = 1
        while (row + down) <= 7:
            if board[row + down][col] in pieces:
              taken_black_mark.append([board[row + down][col]])
              taken_black_coordinates.append((row + down, col))
              break
            down += 1
        left = 1
        while (col - left) >= 0:
            if board[row][col - left] in pieces:
              taken_black_mark.append([board[row][col - left]])
              taken_black_coordinates.append((row, col - left))
              break
            left += 1
        right = 1
        while (col + right) <= 7:
            if board[row][col + right] in pieces:
              taken_black_mark.append([board[row][col + right]])
              taken_black_coordinates.append((row, col + right))
              break
            right += 1
    taken_black_chess_coordinates = convert_to_chess_coordinates(taken_black_coordinates)
    return taken_black_mark, taken_black_chess_coordinates

def convert_to_chess_coordinates(taken_pieces_coordinates):
    chess_coordinates = []
    for row, col in taken_pieces_coordinates:
        chess_col = chr(col + 97)
        chess_row = str(8 - row)
        chess_coordinates.append(f"{chess_col}{chess_row}")
    return chess_coordinates

#jesus pagaliau
def print_final_taken_pieces(taken_black_mark, taken_black_chess_coordinates):
    if not taken_black_mark:
        print("No pieces were taken.")
    else:
        print("Here's the black piece/pieces that white can take:")
        for mark, coord in zip(taken_black_mark, taken_black_chess_coordinates):
            piece = mark[0]
            print(f"{piece} at {coord}")

#
#apsirasyti ka gali nuimti pawn. pawn coordinations col + 1 and row + and - 1
#rook row + 1 and -1 in available rows and + 1 and -1 in available col
#check if a black piece is in a spot (jeigu pirmas sutiktas black piece in the way - break)
#print the black pieces

if __name__ == "__main__":
    main()
#make sure user doesnt overwrite pieces
#when done write "done"
#check if the user input is not too early or too many pieces are pasted

#print("Piece added successfully")
    #else ("Error message")

# print out the black pieces that the white piece can take