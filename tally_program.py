# https://www.reddit.com/r/dailyprogrammer/comments/8jcffg/20180514_challenge_361_easy_tally_program/
# [2018-05-14] Challenge #361 [Easy] Tally Program

import collections
from operator import itemgetter

INPUT_DATA = [
    'abcde',
    'dbbaCEDbdAacCEAadcB',
    'EbAAdbBEaBaaBBdAccbeebaec'
]


if __name__ == '__main__':

    for seq in INPUT_DATA:

        points = {}

        for e in seq:
            if e == e.lower():
                points[e] = points.get(e, 0) + 1
            else:
                points[e.lower()] = points.get(e.lower(), 0) - 1

        sorted_points = collections.OrderedDict(sorted(points.items(), key=itemgetter(1), reverse=True))
        print(sorted_points)



