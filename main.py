#creates board
board = [
["-","-","-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-","-","-",],
["-","-","-","-","-","-","-","-","-","-",]]



cursor_pos = [4,9]



#reads cursor position change and applies it to board
def cursor_reader():
    board[cursor_pos[0]][cursor_pos[1]] = "0"

def display():
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
      for row in board]))


#runs cursor_reader
cursor_reader()

#shows cursor position
print(cursor_pos)

#displays the board
display()

#activates:
running = True

while running:
    cursor_reader()
    print(cursor_pos)
    display()

    move = input("ennter movement:")

    # takes w input and moves cursor up 1
    if cursor_pos[0] <= 3 and cursor_pos[0] >= 0 and move == "s":
        cursor_pos[0] = (cursor_pos[0] + 1)

    # takes s input and moves cursor down 1
    if cursor_pos[0] >= 1 and move == "w":
        cursor_pos[0] = (cursor_pos[0] - 1)

    # takes a input and moves cursor left 1
    if cursor_pos[1] >= 1 and move == "a":
        cursor_pos[1] = (cursor_pos[1] - 1)

    # takes d input and moves cursor right 1
    if cursor_pos[1] <= 8 and move == "d":
        cursor_pos[1] = (cursor_pos[1] + 1)




#saving the old board
'''row1 = ["-","-","-","-","-","-","-","-","-","-",]
row2 = ["-","-","-","-","-","-","-","-","-","-",]
row3 = ["-","-","-","-","-","-","-","-","-","-",]
row4 = ["-","-","-","-","-","-","-","-","-","-",]
row5 = ["-","-","-","-","-","-","-","-","-","-",]'''


#saving old display method
'''print(''.join(board_1))
    print(''.join(board_2))
    print(''.join(board_3))
    print(''.join(board_4))
    print(''.join(board_5))'''
