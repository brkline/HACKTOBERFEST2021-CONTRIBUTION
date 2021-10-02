# Searches text files in the path specified for a specific word

from pathlib import Path

# Where are we searching and for what are we searching
PATH_TO_SEARCH = '.'
SEARCH_WORD = 'ipsum'

""" 
Read through all files with txt extension in the current
path.  If we find a file that contains our search word,
then print out the path.  You could also change the
code below so it returns a list.

"""


def search_for_text():
    for p in Path(PATH_TO_SEARCH).glob('*.txt'):
        with p.open() as f:
            if SEARCH_WORD in f.read():
                print(f"{p.name}")


def main():
    search_for_text()


if __name__ == '__main__':
    main()
