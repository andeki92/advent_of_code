
from pathlib import Path
import string


def is_upper_and_lower(char1, char2):
    ''' Check if the polarity fo the two chars are different '''
    if char1.islower() and char2.isupper():
        return True
    if char1.isupper() and char2.islower():
        return True
    return False


def part1(data):
    index = 0
    data = list(data)

    while index + 1 < len(data):
        if data[index].lower() == data[index + 1].lower():
            if is_upper_and_lower(data[index], data[index + 1]):
                char1 = data[index]
                char2 = data[index + 1]

                # Actually remove the polymer at the same index as we delete the first one
                del data[index]
                del data[index]

                index -= 1
                # Skip the index + 1 term
                continue
        index += 1
    return len(data)


def part2(data):
    sizes = map(lambda d: part1(d), map(lambda s: data.replace(s, "").replace(
        s.upper(), ""), string.ascii_lowercase))
    return min(sizes)


if __name__ == "__main__":
    file = Path(__file__).parent.joinpath("input.txt")

    with file.open("r") as f:
        data = f.readlines()[0]

    #data = 'dabAcCaCBAcCcaDA'

    print("Solutions to day {}".format(file.parent.name[-2:].replace("0", "")))
    print("> Part One Solution: {}".format(part1(data)))
    print("> Part Two Solution: {}".format(part2(data)))
