"""
Time Complexity: O(n)
Auxillary Space Complexity: O(1)
"""


def calculate_final_position_product(inputs):
    final_horizontal_position = 0
    final_depth = 0
    for command in inputs:  # O(n)
        direction, movement = command
        if direction == "forward":
            final_horizontal_position += movement
        elif direction == "up":
            final_depth -= movement
        elif direction == "down":
            final_depth += movement
    return final_horizontal_position * final_depth


def calculate_aim_based_final_position_product(inputs):
    horizontal_position = 0
    depth = 0
    aim = 0
    for command in inputs:  # O(n)
        direction, movement = command
        if direction == "forward":
            horizontal_position += movement
            depth += aim * movement
        elif direction == "up":
            aim -= movement
        elif direction == "down":
            aim += movement
    return horizontal_position * depth


def read_inputs(input_file):
    with open(input_file) as f:
        inputs = [tuple(line.strip().split()) for line in f]
    return [(command[0], int(command[1])) for command in inputs]


if __name__ == "__main__":
    test_inputs = read_inputs(
        input_file="inputs/test_day_2_input.txt",
    )

    inputs = read_inputs(
        input_file="inputs/day_2_input.txt",
    )
    assert calculate_final_position_product(test_inputs) == 150
    print(calculate_final_position_product(inputs))
    assert calculate_aim_based_final_position_product(test_inputs) == 900
    print(calculate_aim_based_final_position_product(inputs))
