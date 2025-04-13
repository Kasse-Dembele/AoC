def parse_input_file():
    left = []
    right= []
    with open("input_puzzle.txt", "r") as file:
        for line in file:
            line.strip()
            input_split = line.split()
            left.append(int(input_split[0]))
            right.append(int(input_split[1]))

    return (left, right)
def calculate_distance(left, right):
    distance = 0
    for i in range(0, len(left)):
        distance = distance + abs(left[i] - right[i])
    return distance

if __name__ == "__main__":
    left_list, right_list = parse_input_file()
    left_list.sort()
    right_list.sort()
    distance = calculate_distance(left_list, right_list)
    print("distance: ", distance)
