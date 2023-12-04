import re


def parse_file(file_path):
    games = []

    with open(file_path, "r") as file:
        for line in file:
            # Split the line into rounds
            rounds = line.strip().split("; ")
            current_game = []

            for i, round_info in enumerate(rounds, 1):
                # Extract color counts for each round
                round_data = re.findall(r"(\d+) (\w+)", round_info)
                round_list = [{color: int(count) for count, color in round_data}]
                current_game.append(round_list)

            games.append(current_game)

    return games


def main():
    games = parse_file("2023/day_two/input.txt")
    sum_indexes = 0
    num_cubes = {"red": 12, "green": 13, "blue": 14}

    for index, game in enumerate(games):
        is_game_valid = True
        for round in game:
            for color, count in round[0].items():
                if count > num_cubes[color]:
                    is_game_valid = False
                    break

        if is_game_valid:
            sum_indexes += index + 1

    print(sum_indexes)


if __name__ == "__main__":
    main()
