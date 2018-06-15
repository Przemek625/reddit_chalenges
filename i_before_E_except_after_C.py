# https://www.reddit.com/r/dailyprogrammer/comments/8q96da/20180611_challenge_363_easy_i_before_e_except/
# Challenge #363 [Easy] I before E except after C

TEST_DATA = [
    'a',
    'zombie',
    'transceiver',
    'veil',
    'icier'
]


def follow_spelling_rule(text: str) -> bool:
    return 'cie' not in text and text.count('ei') == text.count('cei')


if __name__ == '__main__':
    for e in TEST_DATA:
        print(follow_spelling_rule(e))
