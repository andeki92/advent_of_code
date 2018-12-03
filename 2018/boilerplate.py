from pathlib import Path
import pandas as pd


def part1(df):
    return "<NotImplemented>"


def part2(df):
    return "<NotImplemented>"


if __name__ == "__main__":
    file = Path(__file__).parent.joinpath("input.txt")

    with file.open("r") as f:
        data = f.readlines()

    input_data = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

    df = pd.read_csv(file, names=["input"], header=None, delim_whitespace=True)

    print("Solutions to day {}".format(file.parent.name[-2:].replace("0", "")))
    print("> Part One Solution: {}".format(part1(df)))
    print("> Part Two Solution: {}".format(part2(df)))
