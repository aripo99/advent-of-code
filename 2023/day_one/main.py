import re


def convert_spelled_numbers_to_digits(string: str) -> str:
    number_mapping = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    pattern = "|".join(number_mapping.keys())

    def replace_spelled_numbers(match):
        return number_mapping[match.group(0)]

    return re.sub(pattern, replace_spelled_numbers, string, flags=re.IGNORECASE)


def compute_calibration_values_sum(data):
    sum = 0
    for line in data:
        parsed_line = convert_spelled_numbers_to_digits(line)
        numbers = [int(c) for c in parsed_line if c.isdigit()]
        if len(numbers) == 1:
            sum += numbers[0] * 10 + numbers[0]
        else:
            sum += numbers[0] * 10 + numbers[-1]

    return sum


def main():
    with open("input.txt", "r") as f:
        data = f.readlines()
    print(compute_calibration_values_sum(data))


if __name__ == "__main__":
    main()
