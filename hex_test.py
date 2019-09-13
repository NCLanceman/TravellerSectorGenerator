import map_hex

def grid_generate(radius):
    origin = [radius+1, radius+1]
    edge = origin[0] + radius

    board = []
    count = 0
    print("Origin is at :", origin)
    for i in range(1,edge+1):
        for j in range(1, edge+1):
            name = ("{}-{}").format(i,j)
            print(("Adding #{}: {}").format(count,name))
            coord = [i,j]
            board.append(map_hex.Map_Hex(coord,name, origin))
            count = count + 1
    
    return board

rad = int(input("Insert Radius: "))
grid = grid_generate(rad)
