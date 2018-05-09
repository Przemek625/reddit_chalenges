# 2018-03-05] Challenge #353 [Easy] Closest String
# https://www.reddit.com/r/dailyprogrammer/comments/826coe/20180305_challenge_353_easy_closest_string/
from collections import namedtuple

INPUT_DATA1 = [
    'CTCCATCACAC',
    'AATATCTACAT',
    'ACATTCTCCAT',
    'CCTCCCCACTC',
]

INPUT_DATA2 = [
    'AACACCCTATA',
    'CTTCATCCACA',
    'TTTCAATTTTC',
    'ACAATCAAACC',
    'ATTCTACAACT',
    'ATTCCTTATTC',
    'ACTTCTCTATT',
    'TAAAACTCACC',
    'CTTTTCCCACC',
    'ACCTTTTCTCA',
    'TACCACTACTT',

]

INPUT_DATA3 = [
    'ACAAAATCCTATCAAAAACTACCATACCAAT',
    'ACTATACTTCTAATATCATTCATTACACTTT',
    'TTAACTCCCATTATATATTATTAATTTACCC',
    'CCAACATACTAAACTTATTTTTTAACTACCA',
    'TTCTAAACATTACTCCTACACCTACATACCT',
    'ATCATCAATTACCTAATAATTCCCAATTTAT',
    'TCCCTAATCATACCATTTTACACTCAAAAAC',
    'AATTCAAACTTTACACACCCCTCTCATCATC',
    'CTCCATCTTATCATATAATAAACCAAATTTA',
    'AAAAATCCATCATTTTTTAATTCCATTCCTT',
    'CCACTCCAAACACAAAATTATTACAATAACA',
    'ATATTTACTCACACAAACAATTACCATCACA',
    'TTCAAATACAAATCTCAAAATCACCTTATTT',
    'TCCTTTAACAACTTCCCTTATCTATCTATTC',
    'CATCCATCCCAAAACTCTCACACATAACAAC',
    'ATTACTTATACAAAATAACTACTCCCCAATA',
    'TATATTTTAACCACTTACCAAAATCTCTACT',
    'TCTTTTATATCCATAAATCCAACAACTCCTA',
    'CTCTCAAACATATATTTCTATAACTCTTATC',
    'ACAAATAATAAAACATCCATTTCATTCATAA',
    'CACCACCAAACCTTATAATCCCCAACCACAC',
]


def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


if __name__ == '__main__':
    HammingString = namedtuple('HammingString', ['string_', 'hamming_distance'])

    for input_data in (INPUT_DATA1, INPUT_DATA2, INPUT_DATA3):
        hamming_string_table = []
        for s1 in input_data:
            total_hamming_distance = 0
            for s2 in input_data:
                total_hamming_distance += hamming_distance(s1, s2)
            hamming_string_table.append(HammingString(s1, total_hamming_distance))
        sorted_hamming_string_table = sorted(hamming_string_table, key=lambda e: e.hamming_distance)
        print(sorted_hamming_string_table[0].string_)
