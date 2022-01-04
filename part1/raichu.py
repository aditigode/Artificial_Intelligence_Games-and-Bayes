#
# raichu.py : Play the game of Raichu
#
# Arpita Welling (aawellin), Sanika Paranjpe (sparanjp), Aditi Gode (adigode)
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import copy
import random

def board_to_string(board, N):
    return "\n".join(board[i:i + N] for i in range(0, len(board), N))


def get_pos(piece, board, N):
    positions = []
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == piece:
                positions.append([i, j])
    return positions


def parse_board(board, N):
    list2 = []
    for j in range(0, N * N, N):
        list1 = []
        for i in range(j, j + N):
            list1.append(board[i])
        list2.append(list1)

    return list2
    # return [board[i:i+N] for i in range(0, len(board), N)]




#calculate all successors of Pichu
def pichu_succ(board, N, player):
    # print("inside pichu succ")
    validmoves = []
    player_positions = get_pos(player, board, N)
    # print(player_positions)
    if player == 'w':
        for row, col in player_positions:
            if row + 1 <= N - 1 and col - 1 >= 0:
                if board[row + 1][col - 1] == '.':
                    temp = copy.deepcopy(board)
                    if row + 1 == N - 1:
                        temp[row + 1][col - 1] = '@'
                    else:
                        temp[row + 1][col - 1] = 'w'
                    temp[row][col] = '.'
                    validmoves.append(temp)
                if board[row + 1][col - 1] == 'b' and row + 2 <= N - 1 and col - 2 >= 0:
                    # print("killing1 black")
                    if board[row + 2][col - 2] == '.':
                        temp = copy.deepcopy(board)
                        if row + 2 == N - 1:
                            temp[row + 2][col - 2] = '@'
                        else:
                            temp[row + 2][col - 2] = 'w'
                        temp[row + 1][col - 1] = '.'
                        temp[row][col] = '.'
                        validmoves.append(temp)
            if row + 1 <= N - 1 and col + 1 < N:
                if board[row + 1][col + 1] == '.':
                    temp = copy.deepcopy(board)
                    if row + 1 == N - 1:
                        temp[row + 1][col + 1] = '@'
                    else:
                        temp[row + 1][col + 1] = 'w'
                    temp[row][col] = '.'
                    validmoves.append(temp)
                if board[row + 1][col + 1] == 'b' and row + 2 <= N - 1 and col + 2 < N:
                    # print("killing2 black")
                    if board[row + 2][col + 2] == '.':
                        temp = copy.deepcopy(board)
                        if row + 2 == N - 1:
                            temp[row + 2][col + 2] = '@'
                        else:
                            temp[row + 2][col + 2] = 'w'
                        temp[row + 1][col + 1] = '.'
                        temp[row][col] = '.'
                        validmoves.append(temp)
    if player == 'b':
        for row, col in player_positions:
            if row - 1 >= 0 and col - 1 >= 0:
                if board[row - 1][col - 1] == '.':
                    temp = copy.deepcopy(board)
                    if row - 1 == 0:
                        temp[row - 1][col - 1] = '$'
                    else:
                        temp[row - 1][col - 1] = 'b'
                    temp[row][col] = '.'
                    validmoves.append(temp)
                if board[row - 1][col - 1] == 'w' and row - 2 >= 0 and col - 2 >= 0:
                    # print("killing1 white")
                    if board[row - 2][col - 2] == '.':
                        temp = copy.deepcopy(board)
                        if row - 2 == 0:
                            temp[row - 2][col - 2] = '$'
                        else:
                            temp[row - 2][col - 2] = 'b'
                        temp[row - 1][col - 1] = '.'
                        temp[row][col] = '.'
                        validmoves.append(temp)
            if row - 1 >= 0 and col + 1 < N:
                if board[row - 1][col + 1] == '.':
                    temp = copy.deepcopy(board)
                    if row - 1 == 0:
                        temp[row - 1][col + 1] = '$'
                    else:
                        temp[row - 1][col + 1] = 'b'
                    temp[row][col] = '.'
                    validmoves.append(temp)
                if board[row - 1][col + 1] == 'w' and row - 2 >= 0 and col + 2 < N:
                    # print("killing2 white")
                    if board[row - 2][col + 2] == '.':
                        temp = copy.deepcopy(board)
                        if row - 2 == 0:
                            temp[row - 2][col + 2] = '$'
                        else:
                            temp[row - 2][col + 2] = 'b'
                        temp[row - 1][col + 1] = '.'
                        temp[row][col] = '.'
                        validmoves.append(temp)

    # print(validmoves)
    # print("len valid moves: {}".format(len(validmoves)))

    return validmoves





def pikachu_succ(board, N, player):
    if player == 'w':
        # print("here2")
        positions = get_pos('W', board, N)
        #print(positions)
        flag1 = -1
        # print(positions[0])
        successor_list = []

        for row, col in positions:
            if row != N - 1:
                for i in range(row + 1, row + 3):
                    if i != N and board[i][col] != 'w' and board[i][col] != 'W':
                        if (board[i][col] == 'B' or board[i][col] == 'b') and i + 1 != N and board[i + 1][col] == '.':
                            if i + 1 != N - 1:
                                successor = copy.deepcopy(board)
                                successor[row][col], successor[i][col], successor[i + 1][col] = '.', '.', 'W'
                                successor_list.append(successor)
                                break
                            else:
                                successor = copy.deepcopy(board)
                                successor[row][col], successor[i][col], successor[i + 1][col] = '.', '.', '@'
                                successor_list.append(successor)
                                break
                        elif board[i][col] == '.':
                            successor = copy.deepcopy(board)
                            if i != N - 1:
                                successor[row][col], successor[i][col] = '.', 'W'
                                successor_list.append(successor)
                            else:
                                successor[row][col], successor[i][col] = '.', '@'
                                successor_list.append(successor)
                        else:
                            break
                    else:
                        break
            # calculate successors to the right of pikachu
            if col != N - 1:
                for i in range(col + 1, col + 3):
                    if i != N:
                        if (board[row][i] == 'B' or board[row][i] == 'b') and i + 1 != N and board[row][i + 1] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i], successor[row][i + 1] = '.', '.', 'W'
                            successor_list.append(successor)
                            break
                        elif board[row][i] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i] = '.', 'W'
                            successor_list.append(successor)
                        else:
                            break

                    else:
                        break
            # calculate successors to the left of pikachu
            if col != 0:
                for i in range(col - 1, col - 3, -1):
                    if i != -1 and board[row][i] != 'W' and board[row][i] != 'w':
                        if (board[row][i] == 'B' or board[row][i] == 'b') and i - 1 != -1 and board[row][i - 1] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i], successor[row][i - 1] = '.', '.', 'W'
                            successor_list.append(successor)
                            break
                        elif board[row][i] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i] = '.', 'W'
                            successor_list.append(successor)
                        else:
                            break

                    else:
                        break
            

        # print("successor_list is:", successor_list)
    else:
        positions = get_pos('B', board, N)
        # print(positions)
        successor_list = []

        for row, col in positions:
            #calculate successors of Pikachu going straight
            if row != 0:
                for i in range(row - 1, row - 3, -1):
                    if i != -1 and board[i][col] != 'B' and board[i][col] != 'b':
                        if (board[i][col] == 'W' or board[i][col] == 'w') and i - 1 != -1 and board[i - 1][col] == '.':
                            if i - 1 != 0:
                                successor = copy.deepcopy(board)
                                successor[row][col], successor[i][col], successor[i - 1][col] = '.', '.', 'B'
                                successor_list.append(successor)
                                break
                            else:
                                successor = copy.deepcopy(board)
                                successor[row][col], successor[i][col], successor[i - 1][col] = '.', '.', '$'
                                successor_list.append(successor)
                                break
                        elif board[i][col] == '.':
                            successor = copy.deepcopy(board)
                            if i != 0:
                                successor[row][col], successor[i][col] = '.', 'B'
                                successor_list.append(successor)
                            else:
                                successor[row][col], successor[i][col] = '.', '$'
                                successor_list.append(successor)
                        else:
                            break
                    else:
                        break

            # calculate successors of pikachu going right
            
            if col != N - 1:
                for i in range(col + 1, col + 3):
                    if i != N:
                        if (board[row][i] == 'W' or board[row][i] == 'w') and i + 1 != N and board[row][i + 1] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i], successor[row][i + 1] = '.', '.', 'B'
                            successor_list.append(successor)
                            break
                        elif board[row][i] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i] = '.', 'B'
                            successor_list.append(successor)
                        else:
                            break

                    else:
                        break
            # calculate successors of Pikachu going left
            if col != 0:
                for i in range(col - 1, col - 3, -1):
                    if i != -1 and board[row][i] != 'B' and board[row][i] != 'b':
                        if (board[row][i] == 'W' or board[row][i] == 'w') and i - 1 != -1 and board[row][i - 1] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i], successor[row][i - 1] = '.', '.', 'B'
                            successor_list.append(successor)
                            break
                        elif board[row][i] == '.':
                            successor = copy.deepcopy(board)
                            successor[row][col], successor[row][i] = '.', 'B'
                            successor_list.append(successor)
                        else:
                            break

                    else:
                        break
            
    # print("successor_list is1234:", successor_list)
    return successor_list




#calculate all successors of Raichu
def raichu_succ(board, N, player):
    if (player == 'w'):
        # print("got raichu")
        raichu_sym = '@'
        opp_pichu = 'b'
        opp_pikachu = 'B'
        same_pichu = 'w'
        same_pikachu = 'W'
        opp_raichu='$'
    else:
        raichu_sym = '$'
        opp_pichu = 'w'
        opp_pikachu = 'W'
        same_pichu = 'b'
        same_pikachu = 'B'
        opp_raichu='@'
        
    #
    raichus_list = []
    for i in range(0, N):
        for j in range(0, N):
            if board[i][j] == raichu_sym:
                raichus_list.append((i, j))

    #print("Raichu list {}".format(raichus_list))
    moves = []
    moves1 = []
    moves2 = []
    moves3 = []
    moves4 = []
    moves5 = []
    moves6 = []
    moves7 = []
    for raichu in raichus_list:
        i, j = raichu[0], raichu[1]
        #print(i, j)
        r, c = i, j
        kill = 0

        ##down the row
        for row in range(i + 1, N):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][j] == same_pikachu or board_temp[row][j] == same_pichu or board_temp[row][j] == raichu_sym:
                break

            if board_temp[row][j] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][j] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, j
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][j] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves4))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves4.append(board_temp)
                    # print("moves 1 {}".format(moves4))

            elif board_temp[row][j] == opp_pichu or board_temp[row][j] == opp_pikachu or board_temp[row][j] == opp_raichu:
                if row == N - 1:
                    break
                if board_temp[row + 1][j] == opp_pichu or board_temp[row + 1][j] == opp_pikachu or board_temp[row + 1][j] == opp_raichu or board_temp[row + 1][j] == same_pichu or board_temp[row + 1][j] == same_pikachu or board_temp[row+1][j] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row + 1][j] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][j] = "."
                    kill += 1
                    r, c = row + 1, j
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves4))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves4.append(board_new)

                    # print("moves 2 {}".format(moves4))
        ####end of down the row######

        ####up the row
        kill = 0
        for row in range(i - 1, -1, -1):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][j] == same_pikachu or board_temp[row][j] == same_pichu or board_temp[row][j] == raichu_sym:
                break

            if board_temp[row][j] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][j] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, j
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][j] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves5))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves5.append(board_temp)
                    # print("moves 1 {}".format(moves5))

            elif board_temp[row][j] == opp_pichu or board_temp[row][j] == opp_pikachu or board_temp[row][j] == opp_raichu:
                if row == 0:
                    break
                if board_temp[row - 1][j] == opp_pichu or board_temp[row - 1][j] == opp_pikachu or board_temp[row-1][j] == opp_raichu or board_temp[row - 1][j] == same_pichu or board_temp[row - 1][j] == same_pikachu or board_temp[row - 1][j] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row - 1][j] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][j] = "."
                    kill += 1
                    r, c = row - 1, j
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves5))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves5.append(board_new)

                #  print("moves 2 {}".format(moves5))

            ####end of up the row######

        ### check right side columns
        kill = 0
        for col in range(j + 1, N):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[i][col] == same_pikachu or board_temp[i][col] == same_pichu or board_temp[i][col] == raichu_sym:
                break

            if board_temp[i][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[i][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = i, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[i][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves6))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves6.append(board_temp)
                #   print("moves 1 {}".format(moves6))

            elif board_temp[i][col] == opp_pichu or board_temp[i][col] == opp_pikachu or board_temp[i][col] == opp_raichu:
                if col == N - 1:
                    break
                if board_temp[i][col + 1] == opp_pichu or board_temp[i][col + 1] == opp_pikachu or board_temp[i][col+1] == opp_raichu or board_temp[i][col + 1] == same_pichu or board_temp[i][col + 1] == same_pikachu or board_temp[i][col+1] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[i][col + 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[i][col] = "."
                    kill += 1
                    r, c = i, col + 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves6))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves6.append(board_new)

                #   print("moves 2 {}".format(moves6))

        ### end of right side columns

        ###check left side columns
        kill = 0
        for col in range(j - 1, -1, -1):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[i][col] == same_pikachu or board_temp[i][col] == same_pichu or board_temp[i][col] == raichu_sym:
                break

            if board_temp[i][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[i][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = i, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[i][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves7))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves7.append(board_temp)
                #   print("moves 1 {}".format(moves7))

            elif board_temp[i][col] == opp_pichu or board_temp[i][col] == opp_pikachu or board_temp[i][col] == opp_raichu:
                if col == 0:
                    break
                if board_temp[i][col - 1] == opp_pichu or board_temp[i][col - 1] == opp_pikachu or board_temp[i][col-1] == opp_raichu or board_temp[i][col - 1] == same_pichu or board_temp[i][col - 1] == same_pikachu or board_temp[i][col - 1] == raichu_sym:
                    break
                if kill == 0:

                    board_temp[i][col - 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[i][col] = "."
                    kill += 1
                    r, c = i, col - 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves7))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves7.append(board_new)

                #   print("moves 2 {}".format(moves7))

        ### end of left sie column

        # This is upper right diagonal #done dont change now
        kill = 0
        for row, col in zip(range(i - 1, -1, -1), range(j + 1, N)):

            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][col] == same_pikachu or board_temp[row][col] == same_pichu or board_temp[row][col] == raichu_sym:
                break

            if board_temp[row][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves.append(board_temp)
                #   print("moves 1 {}".format(moves))

            elif board_temp[row][col] == opp_pichu or board_temp[row][col] == opp_pikachu or board_temp[row][col] == opp_raichu:
                if col == N - 1 or row == 0:
                    break
                if board_temp[row - 1][col + 1] == opp_pichu or board_temp[row - 1][col + 1] == opp_pikachu or board_temp[row-1][col+1] == opp_raichu or board_temp[row - 1][col + 1] == same_pichu or board_temp[row - 1][col + 1] == same_pikachu or board_temp[row - 1][col + 1] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row - 1][col + 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][col] = "."
                    kill += 1
                    r, c = row - 1, col + 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves.append(board_new)

                #   print("moves 2 {}".format(moves))

        ###end of upper right diagonal####

        # This is lower right diagonal #done dont change now
        kill = 0

        for row, col in zip(range(i + 1, N), range(j + 1, N)):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][col] == same_pikachu or board_temp[row][col] == same_pichu or board_temp[row][col] == raichu_sym:
                break

            if board_temp[row][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves1))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves1.append(board_temp)
                #   print("moves 1 {}".format(moves1))

            elif board_temp[row][col] == opp_pichu or board_temp[row][col] == opp_pikachu or board_temp[row][col] == opp_raichu:
                if col == N - 1 or row == N - 1:
                    break
                if board_temp[row + 1][col + 1] == opp_pichu or board_temp[row + 1][col + 1] == opp_pikachu or board_temp[row+1][col+1] == opp_raichu \
                        or board_temp[row + 1][col + 1] == same_pichu or board_temp[row + 1][col + 1] == same_pikachu or board_temp[row + 1][col + 1] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row + 1][col + 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][col] = "."
                    kill += 1
                    r, c = row + 1, col + 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves1))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves1.append(board_new)

                #   print("moves 2 {}".format(moves1))

        ###end of lower right diagonal####

        # This is lower left diagonal #done dont change now
        kill = 0
        for row, col in zip(range(i + 1, N), range(j - 1, -1, -1)):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][col] == same_pikachu or board_temp[row][col] == same_pichu or board_temp[row][col] == raichu_sym:
                break

            if board_temp[row][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves2))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves2.append(board_temp)
                #   print("moves 1 {}".format(moves2))

            elif board_temp[row][col] == opp_pichu or board_temp[row][col] == opp_pikachu or board_temp[row][col] == opp_raichu:
                if col == 0 or row == N - 1:
                    break
                if board_temp[row + 1][col - 1] == opp_pichu or board_temp[row + 1][col - 1] == opp_pikachu or board_temp[row+1][col-1] == opp_raichu or \
                        board_temp[row + 1][col - 1] == same_pichu or board_temp[row + 1][col - 1] == same_pikachu or board_temp[row + 1][col - 1] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row + 1][col - 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][col] = "."
                    kill += 1
                    r, c = row + 1, col - 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves2))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves2.append(board_new)

                #   print("moves 2 {}".format(moves2))

        ###end of lower left diagonal####

        # This is upper left diagonal #done dont change now
        kill = 0
        for row, col in zip(range(i - 1, -1, -1), range(j - 1, -1, -1)):
            if kill > 0:
                board_temp = copy.deepcopy(board_new)
            else:
                board_temp = copy.deepcopy(board)

            if board_temp[row][col] == same_pikachu or board_temp[row][col] == same_pichu or board_temp[row][col] == raichu_sym:
                break

            if board_temp[row][col] == ".":
                if kill > 0:
                    # board_temp=board_new
                    board_temp[row][col] = raichu_sym
                    board_temp[r][c] = "."
                    r, c = row, col
                else:
                    # board_temp=copy.deepcopy(board)
                    board_temp[row][col] = raichu_sym
                    board_temp[i][j] = "."

                # print("board_temp 1 {}".format(board_temp))
                # print("moves 4 {}".format(moves3))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves3.append(board_temp)
                #   print("moves 1 {}".format(moves3))

            elif board_temp[row][col] == opp_pichu or board_temp[row][col] == opp_pikachu or board_temp[row][col] == opp_raichu:
                if col == 0 or row == 0:
                    break
                if board_temp[row - 1][col - 1] == opp_pichu or board_temp[row - 1][col - 1] == opp_pikachu or board_temp[row-1][col-1] == opp_raichu or \
                        board_temp[row - 1][col - 1] == same_pichu or board_temp[row - 1][col - 1] == same_pikachu or board_temp[row - 1][col - 1] == raichu_sym:
                    break
                if kill == 0:
                    board_temp[row - 1][col - 1] = raichu_sym
                    board_temp[i][j] = "."
                    board_temp[row][col] = "."
                    kill += 1
                    r, c = row - 1, col - 1
                else:
                    break

                # print("board_temp 2 {}".format(board_temp))
                # print("moves 3 {}".format(moves3))
                if board_temp not in moves:
                    board_new = copy.deepcopy(board_temp)
                    moves3.append(board_new)

                #   print("moves 2 {}".format(moves3))
            ###end of upper left diagonal####

    #print("Raichu list {}".format(raichus_list))
    #print(moves7 + moves6 + moves5 + moves4 + moves3 + moves2 + moves1 + moves)
    return moves7 + moves6 + moves5 + moves4 + moves3 + moves2 + moves1 + moves



#call successors of Pichu,Pikachu and Raichu
def successor(board, N, player):
    #print("inside sucessor")
    result = []
    flag = 0
    move_pikachu = pikachu_succ(board, N, player)
    move_pichu = pichu_succ(board, N, player)
    for row in board:
        if (player == 'w' and '@' in row) or (player == 'b' and '$' in row):
            move_raichu = raichu_succ(board, N, player)

            flag = 1
            break

    if flag == 1:
        result = move_raichu + move_pikachu + move_pichu
    else:
        #print("succ else")
        # print(move_pikachu)
        # print(move_pichu)
        result = move_pikachu + move_pichu

    return result




#evaluation function to calculate scores at the horizon
def EvaluationFunction(state, currplayer):
    white_Pikachu = 0
    white_Pichu = 0
    white_Raichu = 0
    black_Pikachu = 0
    black_Pichu = 0
    black_Raichu = 0
    for row in state:
        white_Pikachu += row.count('W')
        white_Pichu += row.count('w')
        white_Raichu += row.count('@')
        black_Pikachu += row.count('B')
        black_Pichu += row.count('b')
        black_Raichu += row.count('$')

    #print(white_Pikachu, white_Pichu, white_Raichu, black_Pikachu, black_Pichu, black_Raichu)

    if currplayer == 'w':
        value = 500 * (white_Raichu - black_Raichu) + 35 * (white_Pikachu - black_Pikachu) + 5 * (
                    white_Pichu - black_Pichu)
        if state[0][0] != "." or state[0][N-1] != "." or state[N-1][0] != "." or state[N-1][N-1] != "." :
            value = value + 3
    else:
        value = 500 * (black_Raichu - white_Raichu) + 35 * (black_Pikachu - white_Pikachu) + 5 * (
                    black_Pichu - white_Pichu)
        if state[0][0] != "." or state[0][N - 1] != "." or state[N - 1][0] != "." or state[N - 1][N - 1] != ".":
            value = value + 3
    #print(value)
    return value



#Minimax algorithm with alpha-beta pruning. Psuedocode was taken from Prof. David Crandall's lecture slides.
def Minimax_Decision(S, maxplayer, N, depth):
    values = []
    # print("Inside minimax")
    alpha = -9999999
    beta = 9999999
    for S_ in successor(S, N, maxplayer):
        values.append([Min_Value(S_, depth, maxplayer, N, alpha, beta), S_])

    # print("Inside minimax",values)
    firstelemets = [element[0] for element in values]
    #print(firstelemets)
    if not firstelemets:
        return S
    maximum = max(firstelemets)
    indexes = []
    for i in range(len(firstelemets)):
        if maximum == firstelemets[i]:
            indexes.append(i)
    #print(indexes)
    #return values[firstelemets.index(max(firstelemets))][1]
    return values[random.choice(indexes)][1]






#minimizer function for min nodes
def Min_Value(S, depth, maxplayer, N,alpha,beta):
    #print("Inside min value")
    minvalues = []
    if maxplayer == 'w':
        minplayer = 'b'
    else:
        minplayer = 'w'
    depth = depth - 1
    if depth == 0:
        # print("Calculate Evaluation function : Inside min value; alpha :{} and beta:{} at depth {}".format(alpha, beta, depth))
        return EvaluationFunction(S, maxplayer)
    else:
        for S_ in successor(S, N, minplayer):
            #minvalues.append(Max_Value(S_, depth, minplayer, N,alpha,beta))
            beta = min(beta,Max_Value(S_, depth, minplayer, N,alpha,beta))
            if alpha >= beta:
                # print("Inside min value; alpha :{} and beta:{} at depth {}".format(alpha,beta,depth))
                return beta
        # print("Inside min value; outside for; alpha :{} and beta:{} at depth {}".format(alpha, beta, depth))
        #print("minvalue at depth {}: {}".format(depth,minvalues))
        return beta #min(minvalues)




#maximizer function for max nodes
def Max_Value(S, depth, minplayer, N,alpha,beta):
    #print("Inside max value")
    depth = depth - 1
    maxvalues = []
    if minplayer == 'w':
        maxplayer = 'b'
    else:
        maxplayer = 'w'
    if depth == 0:
        # print("Calculate Evaluation function : Inside max value; alpha :{} and beta:{} at depth {}".format(alpha, beta, depth))
        return EvaluationFunction(S, minplayer)
    else:
        for S_ in successor(S, N, maxplayer):
            #maxvalues.append(Min_Value(S_, depth, maxplayer, N,alpha,beta))
            alpha = max(alpha,Min_Value(S_, depth, maxplayer, N,alpha,beta))
            if alpha >= beta :
                # print("Inside max value; alpha :{} and beta:{} at depth {}".format(alpha, beta, depth))
                return alpha
        # print("Inside max value; outside for; alpha :{} and beta:{} at depth {}".format(alpha, beta, depth))
        # print("Maxvalue at depth {}: {}".format(depth,maxvalues))
        return alpha #max(maxvalues)





#get the desired output of strings
def FormatOutput(desc):
    string = ""
    for row in desc:
        for i in row:
            string = string + i
    return string





#get the best move and yeild outputs at multiple depths
def find_best_move(board, N, player, timelimit):
    # This sample code just returns the same board over and over again (which
    # isn't a valid move anyway.) Replace this with your code!
    #
    #print("inside find best move")
    board_list = parse_board(board, N)
    #print("Parsed initial board", board_list)
    #print(EvaluationFunction(board_list,player))
    # moves = successor(board_list, N, player)
    # return moves
    desc = Minimax_Decision(board_list, player, N,2)
    output = FormatOutput(desc)
    yield output
    depth = 3
    while True:
        desc = Minimax_Decision(board_list, player, N,depth)
        output = FormatOutput(desc)
        yield output
        depth+=2



if __name__ == "__main__":
    start = time.time()

    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")

    (_, N, player, board, timelimit) = sys.argv
    N = int(N)
    print("board input: {}".format(board))
    timelimit = int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N * N or 0 in [c in "wb.WB@$" for c in board]:
        raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")

    # moves = find_best_move(board, N, player, timelimit)
    # print(moves)
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)
    end = time.time()
    print("Time taken", end - start)
