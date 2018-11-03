from parse import load_kanji
from csv import reader
from random import randint
from kanji_bg import draw

def get_kanji(csv_reader):
    n_kanji = randint(0, n - 1)
    kanji = []
    for i in range(n_kanji):
        kanji = next(csv_reader)

if __name__ == '__main__':
    load_kanji()
    csv_reader = reader(open('kanji.csv'))

    # First line in file kanji.csv is a number of elements which have been written in it
    n = int(next(csv_reader)[0])

    # If kanji have no its drawing choose another
    kanji = ['']
    while kanji[0] == '':
        kanji = get_kanji(csv_reader)

    draw(kanji)


