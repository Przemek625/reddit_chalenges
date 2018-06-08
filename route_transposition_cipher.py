# https://www.reddit.com/r/dailyprogrammer/comments/8n8tog/20180530_challenge_362_intermediate_route/
# [2018-05-30] Challenge #362 [Intermediate] "Route" Transposition Cipher

DATA_1 = 'This is an example'

DATA_2 = 'why is this professor so boring omg'


# TODO write a unite test for this function
def string_to_alpha_table(text: str, xdim: int, ydim: int):

    table_to_partition = [e.upper() for e in text if e.isalpha()]

    table_to_partition_length = len(table_to_partition)
    dimension = xdim * ydim

    assert table_to_partition_length < dimension

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


# TODO in the future change the signature of method to take string instead of table.
def encrypt_note(table, algorithm):

    assert algorithm in ['clockwise', 'counterclockwise']


if __name__ == '__main__':
    print(string_to_alpha_table(DATA_1, 6, 3))

    print(string_to_alpha_table(DATA_2, 6, 5))

