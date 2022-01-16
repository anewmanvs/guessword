"""Game"""

import src.utils as ut

class Game:
    """
    Implementa um jogo

    filename - str indicando arquivo contendo as palavras a serem
        utilizadas no jogo.
    size - int indicando o tamanho das palavras a serem utilizadas
    """

    def __init__(self, filename, size, maxtries):
        """Construtor"""

        self.df_words = ut.filter_context_words(
            ut.read_txt(filename), size)
        self.__word = ut.random_select_word(self.df_words)

        self.tries = 0  # número de tentativas utilizadas
        self.maxtries = maxtries  # número máximo de tentivas

    def produce_score(self):
        """Calcula o score"""

        return self.maxtries - self.tries + 1

    def compare(self, word):
        """
        Compara input word com a palavra sorteada
        """

        if self.tries > self.maxtries:  # acabaram as tentativas
            print('Game over: {}'.format(self.__word))
            return 0

        if not ut.word_in_dict(word, self.df_words):
            return print('Palavra inválida')

        # palavra entrada está no dicionário
        word = word.lower()  # palavra sempre em lower case
        self.tries += 1  # soma uma tentativa
        if word == self.__word:
            print('Acertou!')
            return self.produce_score()
        # não acertou
        return print(ut.compare_words(word, self.__word))
