running = True
pos = [0, 0]
while running:
    move = input()

    if move == "w":
        pos[0] = (pos[0] + 1)
        print(pos)
    elif move == "d":
        pos[1] = (pos[1] + 1)
        print(pos)
    elif move == "x":
        break
