# main

from src.game import Game

SIZE = 5
MAXTRIES = 5
FILENAME = 'palavras.txt'

if __name__ == '__main__':
    game = Game(FILENAME, SIZE, MAXTRIES)
    while game.compare(input()) is None:
        pass
