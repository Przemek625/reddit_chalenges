
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


def zwroc_brakujace_elementy(itterable: list, n: int)->list:

    A = set(range(1, n + 1))
    B = set(itterable)

    return list(A - B)


def generuj_liste_liczb_ze_skokiem(start, end, step):
    return [start + x * step for x in range(0, int((end - start) / step) + 1)]


if __name__ == '__main__':
    v1 = [2, 3, 7, 4, 9]
    n1 = 10

    print(zwroc_brakujace_elementy(v1, n1))

    print(generuj_kody('79-900', '80-155'))

    print(generuj_liste_liczb_ze_skokiem(2.0, 5.5, 0.5))