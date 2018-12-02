from pathlib import Path
from difflib import ndiff
from collections import Counter
import pandas as pd


def part1(df):
    df["twos"] = df["input"].apply(lambda x: 2 in Counter(x).values())
    n_twos = len(df[df["twos"]])

    df["threes"] = df["input"].apply(lambda x: 3 in Counter(x).values())
    n_threes = len(df[df["threes"]])

    return n_twos * n_threes


def part2(df):
    for n, row in df.iterrows():
        code = row["input"]

        for m in range(n + 1, len(df)):
            t_code = df["input"].iloc[m]
            char = []
            pos = []

            for i, s in enumerate(ndiff(code, t_code)):
                if s[0] == ' ':
                    continue
                if s[0] == "+" or s[0] == "-":
                    char.append(s[-1])
                    pos.append(i)

            # If the difference is two characters (one in each string) then return this string
            if len(char) == 2:
                return code[:pos[0]] + code[pos[0] + 1:]


if __name__ == "__main__":
    file = Path(__file__).parent.joinpath("input.txt")
    df = pd.read_csv(file, names=["input"], header=None, delim_whitespace=True)

    print("Part One Solution: {}".format(part1(df)))
    print("Part Two Solution: {}".format(part2(df)))
