
DATA_1 = 'This is an example'

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

    print(table)

    current_dim = 0

    print(table_to_partition)

    for index, e in enumerate(table_to_partition, start=1):
        print(current_dim, index, e)

        if index % xdim == 0 and index != dimension:
            current_dim += 1
        table[current_dim].append(e)

    return table


if __name__ == '__main__':
    print(string_to_alpha_table(DATA_1, 6, 3))

