def mark_boards(boards, curr_number):
    """Mark the drawn numbers in board.

    Parameters
    ----------
    boards : List
        list of boards
    curr_number : int
        Drawn number in the current iteration

    Returns
    -------
    boards
        list of boards where the current drawn number is marked.
    """
    for board in boards:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j][0] == curr_number:
                    board[i][j][1] = True
    return boards


def get_complete_boards(boards):
    """Check for completeness of board and return the first complete board."""
    board_idx_set = set()
    winning_boards = []
    for board_idx, board in enumerate(boards):
        horizontal_check = vertical_check = False
        for i in range(len(board)):
            horizontal_check = all(
                [board[i][j][1] for j in range(len(board[0]))]
            )
            vertical_check = all([board[j][i][1] for j in range(len(board[0]))])
            if horizontal_check or vertical_check:
                board_idx_set.add(board_idx)
                winning_boards.append(board)
    return list(board_idx_set), winning_boards


def compute_result(winning_board, curr_number):
    """Compute final result."""
    unmarked_sum = 0
    for i in range(len(winning_board)):
        for j in range(len(winning_board[0])):
            number, mark = winning_board[i][j]
            if not mark:
                unmarked_sum += number
    return unmarked_sum * curr_number


def get_winner_result(draw_numbers, matrix_boards, mode):
    """Simulate bingo gameplay."""
    game_play = True
    draw_idx = 0
    while True and draw_idx < len(draw_numbers):
        curr_number = draw_numbers[draw_idx]
        matrix_boards = mark_boards(matrix_boards, curr_number)
        board_idx_list, winning_boards = get_complete_boards(matrix_boards)
        if len(winning_boards) > 0:
            if mode == "first":
                return compute_result(winning_boards[0], curr_number)
            elif mode == "last":
                if len(matrix_boards) == 1:
                    return compute_result(winning_boards[0], curr_number)
                for board_idx in sorted(board_idx_list, reverse=True):
                    matrix_boards.pop(board_idx)
        draw_idx += 1
    return -1


def convert_to_matrix(boards, n=5):
    """Convert 1d list to 2d matrix."""
    return [
        [board[i : i + n] for i in range(0, len(board), n)] for board in boards
    ]


def read_inputs(input_file):
    """Read inputs from file."""
    boards = []
    board_idx = -1
    with open(input_file) as fp:
        for i, line in enumerate(fp.readlines()):
            if i == 0:
                draw_numbers = list(map(int, line.strip().split(",")))
                continue
            if not line.strip().split():
                board_idx += 1
                boards.append([])
            else:
                boards[board_idx].extend(list(map(int, line.strip().split())))
    return draw_numbers, boards


def add_mark(boards):
    """Replace each number in bingo board with Tuple(number, mark)
    where mark is bool

    Parameters
    ----------
    boards : List[List[int]]
        The bingo boards containing numbers
    """
    return [[[number, False] for number in board] for board in boards]


def run_bingo(input_file, mode="first"):
    """Run bingo game play for an input file."""
    draw_numbers, boards = read_inputs(input_file)
    boards = add_mark(boards)
    matrix_boards = convert_to_matrix(boards)
    final_score = get_winner_result(draw_numbers, matrix_boards, mode=mode)
    return final_score


if __name__ == "__main__":
    assert (
        run_bingo(input_file="inputs/test_day_4_input.txt", mode="first")
        == 4512
    )
    print(run_bingo(input_file="inputs/day_4_input.txt", mode="first"))
    assert (
        run_bingo(input_file="inputs/test_day_4_input.txt", mode="last") == 1924
    )
    print(run_bingo(input_file="inputs/day_4_input.txt", mode="last"))
