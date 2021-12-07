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

def proc(balls, _boards):
    for ball in balls.split(','):
        for board in _boards:
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
balls = lines[0]
boards = [line for line in lines[2:]]
board_list = list(chunks([b for b in boards if b != ''], 5))
processed_boards = [get_board_obj(board) for board in board_list]


for idx, ball in enumerate(balls.strip().split(',')):
    for board in processed_boards:
        for row in board["rows"]:
            if ball in row and not board.get("win_round"):
                row.remove(ball)
            if len(row) == 0 and not board.get("win_round"):
                board["win_round"] = idx
                board["win_score"] = sum([int(r) for row in board['rows'] for r in row]) * int(ball)
        for col in board["cols"]:
            if ball in col and not board.get("win_round"):
                col.remove(ball)
            if len(col) == 0 and not board.get("win_round"):
                board["win_round"] = idx
                board["win_score"] = sum([int(r) for row in board['cols'] for r in row]) * int(ball)

loser_score = sorted(processed_boards, key=lambda d: d['win_round'])[-1]["win_score"]
print(f"part 2 answer = {loser_score}")
