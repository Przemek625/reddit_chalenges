# https://www.reddit.com/r/dailyprogrammer/comments/8n8tog/20180530_challenge_362_intermediate_route/
# [2018-05-30] Challenge #362 [Intermediate] "Route" Transposition Cipher

DATA_1 = 'This is an example'

DATA_2 = 'why is this professor so boring omg'

DATA_3 = 'For lunch let\'s have peanut-butter and bologna sandwiches'


# TODO write a unite test for this function
def string_to_alpha_table(text: str, xdim: int, ydim: int):
    table_to_partition = [e.upper() for e in text if e.isalpha()]

    table_to_partition_length = len(table_to_partition)
    dimension = xdim * ydim

    assert table_to_partition_length <= dimension

    if table_to_partition_length < dimension:
        supplementary_table = ['X'] * (dimension - table_to_partition_length)

        table_to_partition.extend(supplementary_table)

    table = list([] for _ in range(ydim))
    current_dim = 0

    for index, e in enumerate(table_to_partition, start=1):
        table[current_dim].append(e)

        if index % xdim == 0:
            current_dim += 1

    return table


# TODO add 'counterclockwise' algorithm
def encrypt(text: str, algorithm, xdim: int, ydim: int):

    assert algorithm in ['clockwise', 'counterclockwise']

    data = string_to_alpha_table(text, xdim, ydim)

    encrypted = []

    first_row, first_col, last_row, last_col = 0, 0, ydim - 1, xdim - 1

    while last_row >= first_row and last_col >= first_col:

        if algorithm == 'clockwise':
            encrypted.extend(data[k][last_col] for k in range(first_row, last_row + 1))
            encrypted.extend(data[last_row][k] for k in range(last_col - 1, first_col - 1, -1))
            encrypted.extend(data[k][first_col] for k in range(last_row - 1, first_row - 1, -1))
            encrypted.extend(data[first_row][k] for k in range(first_col + 1, last_col))
        else:
            raise NotImplementedError

        last_row -= 1
        last_col -= 1
        first_row += 1
        first_col += 1

    return ''.join(encrypted)


# TODO add more cases
if __name__ == '__main__':
    print(encrypt(DATA_3, 'clockwise', 4, 12))
