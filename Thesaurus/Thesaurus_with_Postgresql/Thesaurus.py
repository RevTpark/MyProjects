import psycopg2
import difflib
from secrets import *


def keys():
    words = []
    conn = psycopg2.connect(f"dbname='Dictionary' user={user} password={password} host='localhost'"
                            f"port={port} ")
    cur = conn.cursor()
    cur.execute("SELECT word FROM dictionary")
    for i in cur.fetchall():
        words.append(i[0])
    conn.close()
    return words


def search(w):
    # PostGreSQL connect database
    conn = psycopg2.connect(f"dbname='Dictionary' user={user} password={password} host='localhost'"
                            f"port={port} ")
    cur = conn.cursor()
    # Search and collecting the word
    cur.execute("SELECT * FROM dictionary WHERE word='%s'" % w)
    rows = cur.fetchall()

    conn.close()
    return rows


def validator(word):
    meanings = search(word)
    if not meanings:
        meanings = search(word.title())
    if not meanings:
        meanings = search(word.upper())
    if not meanings:
        if len(difflib.get_close_matches(word, keys(), cutoff=0.8)) > 0:
            y_n = input(f'Did you mean {difflib.get_close_matches(word, keys(), cutoff=0.8)[0]}'
                        f' instead? Enter Y if Yes or N if No.')

            if y_n.upper() == "Y":
                meanings = search(difflib.get_close_matches(word, keys(), cutoff=0.8)[0])

            elif y_n.upper() == "N":
                return "Word does not exist in database.", False

            else:
                return "Entry made was not valid!", False

        else:
            return "Word entered was not found in the database. Please enter a valid word.", False

    return meanings, True


if __name__ == 'main':
    input_word = input("Enter a word: ")
    result, value = validator(input_word)
    if value:
        for i in result:
            print(i[1])
    else:
        print(result)
