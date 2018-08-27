
def generuj_kody(kod1: str, kod2: str):

    kod1 = int(kod1.replace('-', ''))
    kod2 = int(kod2.replace('-', ''))

    min_kod = min(kod1, kod2)
    max_kod = max(kod1, kod2)

    zakres_kodow = []

    for e in range(min_kod, max_kod + 1):
        kod = str(e)
        zeros_to_append = 5 - len(kod)
        kod = '0' * zeros_to_append + kod
        kod = kod[0:2] + '-' + kod[2:5]
        zakres_kodow.append(kod)

    return zakres_kodow

if __name__ == '__main__':
    generuj_kody('79-900', '80-155')