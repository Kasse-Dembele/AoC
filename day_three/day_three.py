import re

def eval_operation(operation) -> int:
    pattern = r"mul\(([^,]+),([^)]+)\)"
    operands = re.findall(pattern, operation)
    result = 0
    for item in operands:
        first, second = item
        result = int(first) * int(second) + result
    return result

def evaluate_operations(operations, total_accumulator):
    if len(operations) == 0:
        return total_accumulator
    else:
        operation = operations.pop()
        total_accumulator = total_accumulator + eval_operation(operation)
        return evaluate_operations(operations, total_accumulator)

if __name__ == "__main__":
    matcher_pattern = r"mul\(\d{1,3},\d{1,3}\)"
    final_sum = 0
    with open("input_puzzle.txt",'r') as file:
        for line in file:
            valid_operations = re.findall(matcher_pattern, line)
            final_sum = evaluate_operations(valid_operations, final_sum)

    print(final_sum)
