"""
Time Complexity: O(n)
Auxillary Space Complexity: O(1)
"""


def count_increasing_measurements(inputs):
    num_increase = 0
    for i in range(1, len(inputs)):  # O(n)
        if inputs[i] > inputs[i - 1]:
            num_increase += 1
    return num_increase


def count_increasing_window(inputs, window_size=3):
    num_increase = 0
    for i in range(0, len(inputs) - window_size):  # O(n)
        if inputs[i + 3] > inputs[i]:
            num_increase += 1
    return num_increase


def read_inputs(
    input_file, test_input_file, test_part_1_result, test_part_2_result
):
    with open(input_file) as f, open(test_input_file) as test_f:
        inputs = [int(line.strip()) for line in f]
        test_inputs = [int(line.strip()) for line in test_f]
    assert count_increasing_measurements(test_inputs) == test_part_1_result
    print(count_increasing_measurements(inputs))

    assert count_increasing_window(test_inputs) == test_part_2_result
    print(count_increasing_window(inputs))


read_inputs(
    input_file="inputs/day_1_input.txt",
    test_input_file="inputs/test_day_1_input.txt",
    test_part_1_result=7,
    test_part_2_result=5,
)
