# part 1
with open("../input.txt") as input_file:
    input_str = input_file.read()
    lines = input_str.split('\n')

def get_board_obj(board):
    return {
        "rows": [r.split() for r in board],
        "cols": [[r.split()[i] for r in board] for i in range(0,5)],
    }

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

balls = lines[0]
boards = [line for line in lines[2:]]
board_list = list(chunks([b for b in boards if b != ''], 5))
processed_boards = [get_board_obj(board) for board in board_list]

def proc(balls, boards):
    for ball in balls.split(','):
        for board in boards:
            for row in board["rows"]:
                try:
                    row.remove(ball)
                except ValueError:
                    pass
                if len(row) == 0:
                    return f"part 1 answer = {sum([int(r) for row in board['rows'] for r in row]) * int(ball)}"
            for col in board["cols"]:
                try:
                    col.remove(ball)
                except ValueError:
                    pass
                if len(col) == 0:
                    return f"part 1 answer = {sum([int(c) for col in board['cols'] for c in col]) * int(ball)}"

print(proc(balls, processed_boards))

# part 2
def proc_loser(balls, boards):
    last_winner = 0
    for ball in balls.split(','):
        for board in boards:
            for row in board["rows"]:
                if len(boards) == 1:
                    print(boards)
                    print(sum([int(c) for col in board['cols'] for c in col]))
                    print(int(ball))
                print(len(boards))
                try:
                    row.remove(ball)
                except ValueError:
                    pass
                if len(row) == 0:
                    try:
                        boards.remove(board)
                    except ValueError:
                        pass
                    last_winner = sum([int(r) for row in board['rows'] for r in row]) * int(ball)
                    continue
            for col in board["cols"]:
                try:
                    col.remove(ball)
                except ValueError:
                    pass
                if len(col) == 0:
                    try:
                        boards.remove(board)
                    except ValueError:
                        pass
                    last_winner = sum([int(c) for col in board['cols'] for c in col]) * int(ball)
                    continue
    return last_winner

print(proc_loser(balls, processed_boards))
