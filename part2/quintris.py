# Simple quintris program! v0.2
# D. Crandall, Sept 2021

from AnimatedQuintris import *
from SimpleQuintris import *
####### REMEMBER TO UNCOMMENT BELOW LINE #########
# from kbinput import *
import time, sys
import copy


class HumanPlayer:
    def get_moves(self, quintris):
        print("Type a sequence of moves using: \n  b for move left \n  m for move right \n  n for rotation\n  h for horizontal flip\nThen press enter. E.g.: bbbnn\n")
        moves = input()
        return moves

    def control_game(self, quintris):
        while 1:
            c = get_char_keyboard()
            commands = {"b": quintris.left, "h": quintris.hflip, "n": quintris.rotate, "m": quintris.right,
                        " ": quintris.down}
            commands[c]()


#####
# This is the part you'll want to modify!
# Replace our super simple algorithm with something better
#
class MYQuintrisSucessors:
    # PIECES = [[" x ", "xxx", " x "], ["xxxxx"], ["xxxx", "   x"], ["xxxx", "  x "], ["xxx", "x x"], ["xxx ", "  xx"]]
    BOARD_HEIGHT = 25
    BOARD_WIDTH = 15

    # initialize empty board. State is a pair with the board in first element and score in the second.
    def __init__(self, state, piece, row, col):
        self.state = state
        self.piece = piece
        self.row = row
        self.col = col

    # rotate a given piece by a given angle
    @staticmethod
    def rotate_piece(piece, rotation):
        rotated_90 = ["".join([str[i] for str in piece[::-1]]) for i in range(0, len(piece[0]))]
        return {0: piece, 90: rotated_90, 180: [str[::-1] for str in piece[::-1]],
                270: [str[::-1] for str in rotated_90[::-1]]}[rotation]

    @staticmethod
    def hflip_piece(piece):
        return [str[::-1] for str in piece]

        # print out current state to the screen

    @staticmethod
    def print_state(board, score):
        print("\n" * 3 + ("Score: %d \n" % score) + "|\n".join(board) + "|\n" + "-" * MYQuintrisSucessors.BOARD_WIDTH)

    # return true if placing a piece at the given row and column would overwrite an existing piece
    @staticmethod
    def check_collision(board, piece, row, col):
        # print("board in check collision",board)
        return col + len(piece[0]) > MYQuintrisSucessors.BOARD_WIDTH or row + len(
            piece) > MYQuintrisSucessors.BOARD_HEIGHT \
               or any(
            [any([(c != " " and board[i_r + row][col + i_c] != " ") for (i_c, c) in enumerate(r)]) for (i_r, r) in
             enumerate(piece)])

    # take "union" of two strings, e.g. compare each character of two strings and return non-space one if it exists
    @staticmethod
    def combine(str1, str2):
        return "".join([c if c != " " else str2[i] for (i, c) in enumerate(str1)])

    # place a piece on the board at the given row and column, and returns new (board, score) pair
    @staticmethod
    def place_piece(board, piece, row, col):
        return board[0:row] + \
               [(board[i + row][0:col] + MYQuintrisSucessors.combine(r, board[i + row][col:col + len(r)]) + board[
                                                                                                                i + row][
                                                                                                            col + len(
                                                                                                                r):])
                for (i, r) in enumerate(piece)] + \
               board[row + len(piece):]

    # remove any "full" rows from board, and increase score accordingly
    @staticmethod
    def remove_complete_lines(board, score):
        complete = [i for (i, s) in enumerate(board) if s.count(' ') == 0]
        return ([(" " * MYQuintrisSucessors.BOARD_WIDTH), ] * len(complete) + [s for s in board if s.count(' ') > 0],
                score + len(complete))

    # move piece left or right, if possible
    def move(self, col_offset, new_piece):
        new_col = max(0, min(MYQuintrisSucessors.BOARD_WIDTH - len(self.piece[0]), self.col + col_offset))
        (self.piece, self.col) = (new_piece, new_col) if not MYQuintrisSucessors.check_collision(self.state, new_piece,
                                                                                                 self.row,
                                                                                                 new_col) else (
            self.piece, self.col)

    def finish(self):
        self.state = MYQuintrisSucessors.place_piece(self.state, self.piece, self.row, self.col)

    def print_board(self, clear_screen):
        MYQuintrisSucessors.print_state(*MYQuintrisSucessors.place_piece(*self.state, self.piece, self.row, self.col))

    ######
    # These are the "public methods" that your code might want to call!
    #

    # move piece left, if possible, else do nothing
    def left(self):
        self.move(-1, self.piece)

    # move piece right, if possible, else do nothing
    def right(self):
        self.move(1, self.piece)

    # rotate piece one position if possible, else do nothing
    def rotate(self):
        self.move(0, MYQuintrisSucessors.rotate_piece(self.piece, 90))

    def hflip(self):
        self.move(0, MYQuintrisSucessors.hflip_piece(self.piece))

    # make piece go all the way down until it hits a collision
    def down(self):
        while not MYQuintrisSucessors.check_collision(self.state, self.piece, self.row + 1, self.col):
            self.row += 1
        self.finish()


class ComputerPlayer:
    def SucessorsNextPiece(self, piece, state):
        # print("inside SucessorsNextPiece")
        movesList = []
        row = 0
        col = 0

        # the piece can move "col" number of times to the left and width  - col number of times to the right or can falls straight.
        # each pieace can be either "rotate"d or "hflip"ped number of times.. but how many?? will that depend on the heuristic?
        # rotation 3 times or will remain same, hflip 1 time or will remian same
        # [" x ", "xxx", " x "], ["xxxxx"], ["xxxx", "   x"], ["xxxx", "  x "], ["xxx", "x x"], ["xxx ", "  xx"]

        if piece == [" x ", "xxx", " x "]:
            for i in range(0, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
        elif piece == ["xxxxx"] or piece == ['x', 'x', 'x', 'x', 'x']:
            for i in range(0, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
                movesList.append("m" * i + "n")
                # movesList.append("m" * i + "nn")
                # movesList.append("m" * i + "nnn")
        else:
            for i in range(0, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
                movesList.append("m" * i + "h")
                movesList.append("m" * i + "n")
                movesList.append("m" * i + "nn")
                movesList.append("m" * i + "nnn")
                movesList.append("m" * i + "nh")
                movesList.append("m" * i + "nnh")
                movesList.append("m" * i + "nnnh")

        # print("NextPiece Moves List",movesList)
        # print("Next Piece is",piece)
        # print("Current succ state",state)

        AllSucessors = []
        for move in movesList:
            succ = MYQuintrisSucessors(state, piece, row, col)
            # print(move)
            for c in move:
                # print(c)
                if c in "bnmh":
                    if c == "b":
                        succ.left()
                    if c == "n":
                        succ.rotate()
                    if c == "m":
                        succ.right()
                    if c == "h":
                        succ.hflip()
            succ.down()
            AllSucessors.append(succ.state)

        # print("AllSucessors for Next Piece: ")
        # for s_ in AllSucessors:
        #     MYQuintrisSucessors.print_state(s_,0)
        #     print("\n\n")

        return AllSucessors

    def Sucessors(self, quintris):
        # print("inside Sucessors")
        # print("quintris.get_piece() : ", quintris.get_piece())
        movesList = []
        row = quintris.row
        col = quintris.col
        # board = quintris.get_board()

        piece = quintris.get_piece()[0]

        # the piece can move "col" number of times to the left and width  - col number of times to the right or can falls straight.
        # each pieace can be either "rotate"d or "hflip"ped number of times.. but how many?? will that depend on the heuristic?
        # rotation 3 times or will remain same, hflip 1 time or will remian same
        # [" x ", "xxx", " x "], ["xxxxx"], ["xxxx", "   x"], ["xxxx", "  x "], ["xxx", "x x"], ["xxx ", "  xx"]

        if piece == [" x ", "xxx", " x "]:
            for i in range(0, col + 1):
                movesList.append("b" * i)
            for i in range(1, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
        elif piece == ["xxxxx"] or piece == ['x', 'x', 'x', 'x', 'x']:
            for i in range(0, col + 1):
                movesList.append("b" * i)
                movesList.append("b" * i + "n")
                # movesList.append("b" * i + "nn")
                # movesList.append("b" * i + "nnn")
            for i in range(1, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
                movesList.append("m" * i + "n")
                # movesList.append("m" * i + "nn")
                # movesList.append("m" * i + "nnn")
        else:
            for i in range(0, col + 1):
                movesList.append("b" * i)
                movesList.append("b" * i + "h")
                movesList.append("b" * i + "n")
                movesList.append("b" * i + "nn")
                movesList.append("b" * i + "nnn")
                movesList.append("b" * i + "nh")
                movesList.append("b" * i + "nnh")
                movesList.append("b" * i + "nnnh")
            for i in range(1, quintris.BOARD_WIDTH - col + 1 - len(piece[0])):
                movesList.append("m" * i)
                movesList.append("m" * i + "h")
                movesList.append("m" * i + "n")
                movesList.append("m" * i + "nn")
                movesList.append("m" * i + "nnn")
                movesList.append("m" * i + "nh")
                movesList.append("m" * i + "nnh")
                movesList.append("m" * i + "nnnh")

        # print(movesList)
        # print("Curren board state",quintris.state)
        # print("Current piece", quintris.get_piece())
        AllSucessors = []
        # COMMANDS = {"b": quintris.left, "n": quintris.rotate, "m": quintris.right, "h": quintris.hflip}
        state, score = quintris.state
        for move in movesList:
            succ = MYQuintrisSucessors(state, piece, row, col)
            # print(move)
            for c in move:
                # print(c)
                if c in "bnmh":
                    if c == "b":
                        succ.left()
                    if c == "n":
                        succ.rotate()
                    if c == "m":
                        succ.right()
                    if c == "h":
                        succ.hflip()
            succ.down()
            AllSucessors.append((succ.state, move))

        # print("AllSucessors",AllSucessors)
        return AllSucessors

    # This function should generate a series of commands to move the piece into the "optimal"
    # position. The commands are a string of letters, where b and m represent left and right, respectively,
    # and n rotates. quintris is an object that lets you inspect the board, e.g.:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def get_moves(self, quintris):
        # super simple current algorithm: just randomly move left, right, and rotate a few times

        sucessors = self.Sucessors(quintris)

        sucessors_nextpiece = []
        heuristic_value = []
        for s_, string in sucessors:
            sucessors_nextpiece.append((s_, self.SucessorsNextPiece(quintris.get_next_piece(), s_)))

        # print(sucessors_nextpiece)
        for cp, S in sucessors_nextpiece:
            for s_ in S:
                # print(s_)
                value = self.heuristic(quintris, s_)
                heuristic_value.append((value, cp))

        # print("HV",heuristic_value)

        result = min(heuristic_value)
        cp = result[1]
        for item, move in sucessors:
            if item == cp:
                return move

        # board, move  = random.choice(sucessors)
        # print("Move taken",move)
        # return final[1]
        # random.choice("mnbh") * random.randint(1, 10)

    def heuristic(self, quintris, successor):

        board_trial = successor
        # print("in heuristic",board_trial)
        first = []
        second = []
        third = []
        score = {}

        for col in range(1, quintris.BOARD_WIDTH):
            for row in range(0, quintris.BOARD_HEIGHT):
                if board_trial[row][col] == "x":
                    for j in range(row, quintris.BOARD_HEIGHT):
                        if board_trial[j][col - 1] == " ":
                            first.append((j, col - 1))
                        if col < quintris.BOARD_WIDTH - 1:
                            if board_trial[j][col + 1] == " ":
                                third.append((j, col + 1))
                        if board_trial[j][col] == " ":
                            second.append((j, col))
                    break

        col = 0

        for row in range(0, quintris.BOARD_HEIGHT):
            if board_trial[row][col] == "x":
                for j in range(row, quintris.BOARD_HEIGHT):
                    if board_trial[j][col] == " ":
                        second.append((j, col))
                    if board_trial[j][col + 1] == " ":
                        third.append((j, col + 1))

                break

        '''print("first",first)
        print("second",second)
        print("third",third)'''

        for element in first:
            if element not in score.keys():
                score[element] = 1

        for element in second:
            if element not in score.keys():
                score[element] = 25 - element[0]
            else:
                score[element] += 25 - element[0]

        for element in third:
            if element not in score.keys():
                score[element] = 1
            else:
                score[element] += 1

        # height=25*15
        # for i in successor:
        #    if ' ' in i:
        # BOARD_HEIGHT = 25
        # BOARD_WIDTH = 15
        #        counter=i.count(' ')
        #        height-=counter
        # column_heights = [ min([ r for r in range(len(successor)-1, 0, -1) if successor[r][c] == "x"] + [100,] ) for c in range(0, len(successor[0]) ) ]
        # index = column_heights.index(max(column_heights))
        # min_values=[999] * quintris.BOARD_WIDTH
        # for i,string in enumerate(successor):
        #    if 'x' in string:
        #       if i < min_values[i]:
        total_height = 0
        for col in range(len(successor[0])):

            # toal_height = 0
            for row in range(len(successor)):

                if successor[row][col] == 'x':
                    # if min < row:
                    total_height += (quintris.BOARD_HEIGHT - row)
                    break
        cleared_lines = 0
        for row in successor:
            if 'x' in row:
                if row.count('x') == quintris.BOARD_WIDTH:
                    cleared_lines += 1

            # total_height+=(quintris.BOARD_HEIGHT-min)
        average_height = total_height / quintris.BOARD_WIDTH
        # print(average_height)
        # print("score is",score)
        holes_score = sum(score.values())
        total_score = 2*holes_score + total_height - 30 * cleared_lines
        # print(total_score)

        return total_score

    '''
    #the following functions recommended a move using expectimin algorithm
    def get_moves(self, quintris):
        # super simple current algorithm: just randomly move left, right, and rotate a few times

        sucessors = self.Sucessors(quintris)

        sucessors_nextpiece = []
        heuristic_value = []
        expected_values_list=[]
        for s_, string in sucessors:
            sucessors_nextpiece.append((s_, self.SucessorsNextPiece(quintris.get_next_piece(), s_)))

        #create chance nodes at depth=2
        for cp, S in sucessors_nextpiece:
            for s_ in S:
                expected_values_list.append((cp,self.chance_nodes(quintris,cp,s_)))

        min_value=99999999
        for S_,expected_value in expected_values_list:
            if min_value > expected_value:
                min_value=expected_value
                min_state=S_

        for item, move in sucessors:
            if item == min_state:
              return move

    #calculate expected values of each of the six pieces in the chance nodes
    def chance_nodes(self,quintris,cp,state):
        successor_list=[]
        pieces_probab=[]
        min_list=[]
        pieces=[" x ", "xxx", " x "], ["xxxxx"], ["xxxx", "   x"], ["xxxx", "  x "], ["xxx", "x x"], ["xxx ", "  xx"]
        length_of_piece=len(pieces)
        for i in range(length_of_piece):
            successor_list=self.SucessorsNextPiece(pieces[i],state)
            min=99999999
            for successor in successor_list:
                value=self.heuristic(quintris,successor)
                if min > value:
                    min=value
            min_list.append(min)
            pieces_probab.append(self.calculate_probab_dist(quintris,i))
        for i in range(length_of_piece):
            expected_value=pieces_probab[i] * min_list[i]
        return expected_value


    #calculate probability of the piece using the probability distribution selected
    def calculate_probab_dist(self,quintris,piece_number):
        probab_dist_total=len(quintris.piece_dist)
        piece_count=quintris.piece_dist.count(piece_number)
        probability=piece_count/probab_dist_total
        return probability
    '''

    # This is the version that's used by the animted version. This is really similar to get_moves,
    # except that it runs as a separate thread and you should access various methods and data in
    # the "quintris" object to control the movement. In particular:
    #   - quintris.col, quintris.row have the current column and row of the upper-left corner of the
    #     falling piece
    #   - quintris.get_piece() is the current piece, quintris.get_next_piece() is the next piece after that
    #   - quintris.left(), quintris.right(), quintris.down(), and quintris.rotate() can be called to actually
    #     issue game commands
    #   - quintris.get_board() returns the current state of the board, as a list of strings.
    #
    def control_game(self, quintris):
        # another super simple algorithm: just move piece to the least-full column
        while 1:
            time.sleep(0.1)

            # board = quintris.get_board()
            # column_heights = [ min([ r for r in range(len(board)-1, 0, -1) if board[r][c] == "x"  ] + [100,] ) for c in range(0, len(board[0]) ) ]

            # index = column_heights.index(max(column_heights))
            #
            # if(index < quintris.col):
            #     quintris.left()
            # elif(index > quintris.col):
            #     quintris.right()
            # else:
            #     quintris.down()

            sucessors = self.Sucessors(quintris)

            sucessors_nextpiece = []
            heuristic_value = []
            for s_, string in sucessors:
                sucessors_nextpiece.append((s_, self.SucessorsNextPiece(quintris.get_next_piece(), s_)))

            # print(sucessors_nextpiece)
            for cp, S in sucessors_nextpiece:
                for s_ in S:
                    # print(s_)
                    value = self.heuristic(quintris, s_)
                    heuristic_value.append((value, cp))

            # print("HV",heuristic_value)
            finalmove = ""
            result = min(heuristic_value)
            cp = result[1]
            for item, move in sucessors:
                if item == cp:
                    finalmove = move
                    break
            for c in finalmove:
                # print(c)
                if c in "bnmh":
                    if c == "b":
                        quintris.left()
                    if c == "n":
                        quintris.rotate()
                    if c == "m":
                        quintris.right()
                    if c == "h":
                        quintris.hflip()


###################
#### main program

(player_opt, interface_opt) = sys.argv[1:3]

try:
    if player_opt == "human":
        player = HumanPlayer()
    elif player_opt == "computer":
        player = ComputerPlayer()
    else:
        print("unknown player!")

    if interface_opt == "simple":
        quintris = SimpleQuintris()
    elif interface_opt == "animated":
        quintris = AnimatedQuintris()
    else:
        print("unknown interface!")

    quintris.start_game(player)

except EndOfGame as s:
    print("\n\n\n", s)



