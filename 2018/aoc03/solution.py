from pathlib import Path
import pandas as pd
import numpy as np
import collections
import re


class Fabric():
    def __init__(self, x, y):
        # Create a 1000x1000 matrix containing the fabric
        self.fabric = [[[] for i in range(x)] for j in range(y)]
        self.unique_claims = []

    def __add__(self, other):
        self.unique_claims.append(other.id)

        for x in range(other.x, other.xm):
            for y in range(other.y, other.ym):
                self.fabric[x][y].append(other.id)

                # Remove any claim that lands on top of another
                if len(self.fabric[x][y]) >= 2:

                    # Make sure we remove the old one as well
                    for claim in self.fabric[x][y]:
                        if claim in self.unique_claims:
                            self.unique_claims.remove(claim)

    def __repr__(self):
        return '\n'.join(["".join(['{0:2}{1:4}{0:2}'.format("", ", ".join([str(i) for i in item])) for item in row]) for row in self.fabric])

    def overlaps(self):
        count = 0

        for x in range(len(self.fabric[0])):
            for y in range(len(self.fabric[0])):
                if len(self.fabric[x][y]) >= 2:
                    count += 1

        return count


class Claim():
    def __init__(self, id, x, y, w, h):
        self.id = id
        self.x = x
        self.xm = x + w
        self.y = y
        self.ym = y + h

        # Create a piece of fabric WxH in size
        self.claim = np.ones((w, h))

    def __repr__(self):
        return "({}, {}, {}, {})".format(self.x, self.y, self.xm, self.ym)


def part1(df, f):
    # Create a fabric of size 1000x1000
    for claim in df["claim"]:
        f + claim

    return f.overlaps()


def part2(df, f):
    return f.claims


def test():
    f = Fabric(8, 8)

    c1 = Claim(1, 1, 3, 4, 4)
    c2 = Claim(2, 3, 1, 4, 4)
    c3 = Claim(3, 5, 5, 2, 2)

    # Add all the claims to the fabric
    f + c1
    f + c2
    f + c3

    assert(f.overlaps() == 4)
    print("All tests passed")


if __name__ == "__main__":
    file = Path(__file__).parent.joinpath("input.txt")

    with file.open("r") as f:
        data = f.readlines()

    # Map the input data to a list of lists
    input_data = list(
        map(lambda s: list(map(int, re.findall(r'-?\d+', s))), data))

    # Convert the list of lists to a dataframe
    df = pd.DataFrame(input_data)

    # Set the index to the 0th column and rename it
    df.set_index(0, inplace=True)
    df.index.name = "id"

    # Convert each row to a claim
    for n, row in df.iterrows():
        df.at[n, "claim"] = Claim(n, row[1], row[2], row[3], row[4])

    # Drop the previously converted coords
    df.drop(columns=[1, 2, 3, 4], inplace=True)

    test()

    f = Fabric(1000, 1000)

    print("Solutions to day {}".format(file.parent.name[-2:].replace("0", "")))
    print("> Part One Solution: {}".format(part1(df, f)))
    print("> Part Two Solution: {}".format(part2(df, f)))
