def process_file(filename):
    """Opens and processes a file by finding the first and last
    numbers on each line, taking the difference, and then summing
    that difference over all lines.
    """
    diff_sum = 0
    with open(filename) as fh:
        for line in fh:
            first = find_first(line)
            last = find_last(line)
            diff = first - last
            diff_sum += diff
    return diff_sum


def find_first(line):
    """Finds the first number to occur on a line."""
    number = ""
    i = 0
    while not line[i].isdigit():  # find where num starts
        i += 1
    while line[i].isdigit():  # read num
        number += line[i]
        i += 1
    return int(number)


def find_last(line):
    """Finds the last number to occur on a line."""
    number = ""
    i = len(line) - 1
    while not line[i].isdigit():  # find where num starts
        i -= 1
    while line[i].isdigit():  # read num
        number = line[i] + number
        i -= 1
    return int(number)


if __name__ == "__main__":
    print(process_file("data.txt"))
