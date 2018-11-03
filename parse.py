from bs4 import BeautifulSoup
from requests import get
from time import sleep
import os


def load_kanji(csv_file):
    # Means that file already exists and it has data in it
    if os.path.exists(csv_file) and os.path.getsize(csv_file) > 0:
        return

    html = get('https://nihongoichiban.com/2011/04/30/complete-list-of-vocabulary-for-the-jlpt-n5/').text

    # If file doesn't exist create it
    csv = open(csv_file, 'w+')
    soup = BeautifulSoup(html)

    '''
    ' All Kanjis and their descriptions are placed in <table> tags
    ' specially in <tr> stores all information about one perticular
    ' kanji. (Kanji, Furigana, Romaji, Meaning)
    '
    ' In <td> stores each of those four.
    '''
    data = []
    for i in soup.find_all('tr'):
        temp_data = []
        for j in i.find_all('td'):
            temp_data.append(j.text)
        data.append(','.join(temp_data))
    csv.write(str(len(data)) + '\n' + '\n'.join(data))
    csv.close()

if __name__ == '__main__':
    load_kanji()
