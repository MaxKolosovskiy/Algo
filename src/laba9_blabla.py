import itertools
import math

def calculate_length(heights, w):
    max_length = 0
    n = len(heights)

    # All combinations for height
    # Product decart product equivalent to the nested cycle FOR
    for combo in itertools.product(*[range(1, h + 1) for h in heights]):
        # We calculate the length of the wire for the current combination of the heights of the supports
        length = 0
        for i in range(1, n):
            length += math.sqrt((w ** 2) + ((combo[i] - combo[i - 1]) ** 2))

        # We compare the found length with the maximum length and, if it is greater, we update the maximum length
        max_length = max(max_length, length)

    return round(max_length, 2)

def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        w = int(lines[0].strip())
        heights = list(map(int, lines[1].strip().split()))
    return heights, w

def write_output(file_path, result):
    with open(file_path, 'w') as file:
        file.write(str(result) + '\n')

if __name__ == "__main__":
    heights, w = read_input('input.txt')
    result = calculate_length(heights, w)
    write_output('output.txt', result)