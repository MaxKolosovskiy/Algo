import math

def calculate_wire_length(distance, previous_height, current_height):
    return math.sqrt(distance ** 2 + (previous_height - current_height) ** 2)

def compute_maximum_wire_length(distance, heights, output_filename):
    num_pillars = len(heights)
    wire_lengths = [[0, 0] for _ in range(num_pillars)]

    for i in range(1, num_pillars):
        bottom_to_bottom = wire_lengths[i - 1][0] + calculate_wire_length(distance, 1, 1)
        top_to_bottom = wire_lengths[i - 1][1] + calculate_wire_length(distance, 1, heights[i - 1])
        wire_lengths[i][0] = max(bottom_to_bottom, top_to_bottom)

        bottom_to_top = wire_lengths[i - 1][0] + calculate_wire_length(distance, heights[i], 1)
        top_to_top = wire_lengths[i - 1][1] + calculate_wire_length(distance, heights[i], heights[i - 1])
        wire_lengths[i][1] = max(bottom_to_top, top_to_top)

    max_wire_length = round(max(wire_lengths[num_pillars - 1][0], wire_lengths[num_pillars - 1][1]), 2)

    with open(output_filename, 'w') as file:
        file.write(f"{max_wire_length}")

    return max_wire_length

def load_input(filename):
    with open(filename, 'r') as file:
        distance = int(file.readline().strip())
        heights = list(map(int, file.readline().strip().split()))

    return distance, heights
