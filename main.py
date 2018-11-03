from parse import load_kanji
from csv import reader
from random import randint
from kanji_bg import draw
from configuration import *
from time import sleep

def get_kanji(n, csv_reader):
    n_kanji = randint(0, n-1)
    kanji = []
    for i in range(n_kanji):
        kanji = next(csv_reader)
    return kanji

if __name__ == '__main__':
    load_kanji(csv_file)
    csv_reader = reader(open(csv_file))

    # First line in file kanji.csv is a number of elements which have been written in it
    n = int(next(csv_reader)[0])

    while True:
        # If kanji have no its drawing choose another
        kanji = ['']
        while kanji[0] == '':
            kanji = get_kanji(n, csv_reader)

        draw(kanji, path_bg=path_bg, path_font=path_font)

        # Sleep 1 hour after changing kanji
        sleep(3600)


