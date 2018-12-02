from pathlib import Path


def get_file(filename):
    p = Path(__file__).parent

    return p.joinpath(filename)


def part1():
    solution = 0

    with get_file("input.txt").open("r") as file:
        for line in file:
            cleanline = line.strip()
            solution += eval(cleanline)

    return solution


def part2():
    seen = []
    solution = 0

    while solution not in seen:
        with get_file("input.txt").open("r") as file:
            for line in file:
                seen.append(solution)
                cleanline = line.strip()

                solution += eval(cleanline)

                if solution in seen:
                    return solution


if __name__ == "__main__":
    print("Part One Solution:", part1())
    print("Part Two Solution:", part2())
