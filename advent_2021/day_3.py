"""
    Time Complexity: O(nm)
        where m is the number of bits in the report
    Auxillary Space Complexity: O(1)
"""


def collect_bit_frequency(inputs, position):
    zero_index = []  # list of indices with 0 in the specific position
    one_index = []
    for idx, report in enumerate(inputs):
        if report[position] == "1":
            one_index.append(idx)
        else:
            zero_index.append(idx)
    return zero_index, one_index


def calculate_rating(inputs, mode="oxygen"):
    report_length = len(inputs[0])
    current_inputs = inputs
    for position in range(0, report_length):  # O(m)
        zero_index, one_index = collect_bit_frequency(
            current_inputs, position
        )  # O(n)
        if mode == "oxygen":
            filter_index = (
                zero_index if len(zero_index) > len(one_index) else one_index
            )
        else:
            filter_index = (
                one_index if len(one_index) < len(zero_index) else zero_index
            )
        new_inputs = [current_inputs[i] for i in filter_index]
        current_inputs = new_inputs
        if len(filter_index) == 1:
            break
    return int(current_inputs[0], 2)


def calculate_life_support_rating(inputs):
    """
    Compute product of oxygen rating and CO2 scrubber rating.
    """
    return calculate_rating(inputs, mode="oxygen") * calculate_rating(
        inputs, mode="co2"
    )


def calculate_power_consumption(inputs):
    """
    Compute product of gamma rate and epsilon rate.

    gamma rate: most common value of each position
    epsilon rate: least common value of each position or (2^5 - 1 - gamma_rate)
    """
    report_length = len(inputs[0])
    gamma_rate = [0 for _ in range(report_length)]
    for report in inputs:  # O(n)
        for i, bit in enumerate(report):  # O(m)
            if bit == "1":
                gamma_rate[i] += 1
            else:
                gamma_rate[i] -= 1

    gamma_rate = int(
        "".join(map(str, [1 if val > 0 else 0 for val in gamma_rate])), 2
    )
    return gamma_rate * ((2 ** report_length) - 1 - gamma_rate)


def read_inputs(input_file):
    with open(input_file) as f:
        inputs = [line.strip() for line in f]
    return inputs


if __name__ == "__main__":
    test_inputs = read_inputs(
        input_file="inputs/test_day_3_input.txt",
    )

    inputs = read_inputs(
        input_file="inputs/day_3_input.txt",
    )
    assert calculate_power_consumption(test_inputs) == 198
    print(calculate_power_consumption(inputs))
    assert calculate_life_support_rating(test_inputs) == 230
    print(calculate_life_support_rating(inputs))
