# https://www.reddit.com/r/dailyprogrammer/comments/6v29zk/170821_challenge_328_easy_latin_squares/
# [17-08-21] Challenge #328 [Easy] Latin Squares

INPUT_DATA1 = {
    'dimension': 5,
    'numbers': '1 2 3 4 5 5 1 2 3 4 4 5 1 2 3 3 4 5 1 2 2 3 4 5 1'
}

INPUT_DATA2 = {
    'dimension': 2,
    'numbers': '1 3 3 4'
}

INPUT_DATA3 = {
    'dimension': 4,
    'numbers': '1 2 3 4 1 3 2 4 2 3 4 1 4 3 2 1'
}


def make_rows(numbers, dimension):

    if len(numbers) != pow(dimension, 2):
        raise ValueError("Undefined for sequences of improper dimension")

    rows = [
        [] for _ in range(dimension)
    ]

    row_index = 0
    for i, e in enumerate(numbers, 1):
        rows[row_index].append(e)
        if i % dimension == 0:
            row_index += 1
    return rows


def make_cols(numbers, dimension):
    cols = [
        [] for _ in range(dimension)
    ]

    for i in range(dimension):
        for i2 in range(i, i + dimension * (dimension - 1) + 1, dimension):
            cols[i].append(numbers[i2])
    return cols


def is_latin(rows, cols, dimension):

    set_ = set([str(i) for i in range(1, dimension + 1)])

    it = list()
    it.extend(rows)
    it.extend(cols)

    for e in it:
        if set(e) != set_:
            return False
    return True


if __name__ == '__main__':

    for e in (INPUT_DATA1, INPUT_DATA2, INPUT_DATA3):
        e['numbers'] = e['numbers'].split(sep=' ')
        rows = make_rows(e['numbers'], e['dimension'])
        cols = make_cols(e['numbers'], e['dimension'])
        print(is_latin(rows, cols, dimension=e['dimension']))

