# https://www.reddit.com/r/dailyprogrammer/comments/8n8tog/20180530_challenge_362_intermediate_route/
# [2018-05-30] Challenge #362 [Intermediate] "Route" Transposition Cipher

DATA_1 = 'This is an example'

DATA_2 = 'why is this professor so boring omg'

DATA_3 = 'For lunch let\'s have peanut-butter and bologna sandwiches'


def string_to_alpha_table1(text: str, xdim: int, ydim: int):
    table_to_partition = [e.upper() for e in text if e.isalpha()]

    table_to_partition_length = len(table_to_partition)
    dimension = xdim * ydim

    if table_to_partition_length < dimension:
        supplementary_table = ['X'] * (dimension - table_to_partition_length)

        table_to_partition.extend(supplementary_table)

    return table_to_partition


# TODO write a unite test for this function
def string_to_alpha_table2(text: str, xdim: int, ydim: int):
    table_to_partition = [e.upper() for e in text if e.isalpha()]

    table_to_partition_length = len(table_to_partition)
    dimension = xdim * ydim

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


def encrypt(data, xdim, ydim):

    encrypted = []
    X = 0
    Z = 0
    c = 1
    start, end = xdim - 1, xdim * (ydim - X) - 1

    while(True):

        encrypted.extend(data[start: end: 4])

        start, end = end, end - xdim + 1
        encrypted.extend(data[start: end: -1])

        start, end = end, end - xdim * (ydim - 1 - X)
        encrypted.extend(data[start: end: -4])

        start, end = end, end + xdim - 1 - 1
        encrypted.extend(data[start: end: 1])
        start, end = end, xdim * (ydim - X) - 1
        print(start, end)

        X += 1
        c += 1
        print(encrypted)

        if (c == 3):
            break

    return encrypted


# TODO in the future change the signature of method to take string instead of table.
def encrypt_note(table, algorithm):
    assert algorithm in ['clockwise', 'counterclockwise']


if __name__ == '__main__':
    print(encrypt(string_to_alpha_table1(DATA_3, 4, 12), 4, 12))
