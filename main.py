# TIK-TAC-TOE


def print_field(matrix):
    for line in matrix:
        print(*line)


def do_step(sign):
    while True:
        x, y = map(int, input(f"step {sign}: ").split())
        if matrix[x - 1][y - 1] == "-":
            matrix[x - 1][y - 1] = sign
            break
        print("item is not empty")


def win(matrix, sign):
    for line in matrix:
        if line.count(sign) == 3:
            print(f"{sign} win")
            return True

    for j in range(len(matrix)):
        list_ = []
        for i in range(len(matrix)):
            list_.append(matrix[i][j])
        if list_.count(sign) == 3:
            print(f"{sign} win")
            return True

    if matrix[0][0] + matrix[1][1] + matrix[2][2] == sign * 3:
        print(f"{sign} win")
        return True

    if matrix[0][2] + matrix[1][1] + matrix[2][0] == sign * 3:
        print(f"{sign} win")
        return True

    return False


matrix = [["-" for j in range(3)] for i in range(3)]
game = True
player_step = 0

while game:
    print_field(matrix)
    if player_step % 2 == 0:
        do_step("X")
    else:
        do_step("O")

    player_step += 1
    if win(matrix, "X") or win(matrix, "O"):
        print()
        print_field(matrix)
        game = False
    elif player_step == 9:
        print("Draw")
        print_field(matrix)
        game = False
