def compute_calibration_values_sum(data):
    sum = 0
    for line in data:
        numbers = [int(c) for c in line if c.isdigit()]
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
