def solution(keyinput, board):
    position = [0, 0]

    moves = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    
    x_limit, y_limit = board[0] // 2, board[1] // 2

    for key in keyinput:
        position[0] = max(-x_limit, min(x_limit, position[0] + moves[key][0]))
        position[1] = max(-y_limit, min(y_limit, position[1] + moves[key][1]))

    return position
