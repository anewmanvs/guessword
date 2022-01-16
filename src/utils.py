"""Métodos úteis"""

import numpy as np
import pandas as pd

def read_txt(filename):
    """
    Faz a leitura de um arquivo de texto contendo as palavras
    """

    with open(filename, 'r') as _f:
        return _f.read().split('\n')

def filter_context_words(lwords, size):
    """
    Filtra apenas as palavras que serão consideradas no jogo
    """

    df_words = pd.DataFrame(lwords, columns=['word'])
    df_words = df_words[df_words['word'].str.len() == size]
    # só aceita palavras sem caracteres especiais
    rgx = r'[^\wáéíóúãõàèìòùç]'
    df_words = df_words[~df_words['word'].str.contains(rgx, regex=True)]
    df_words = df_words.copy()
    # todas as palavras em lower case
    df_words['word'] = df_words['word'].str.lower()

    return df_words

def word_in_dict(word, df_words):
    """Retorna se a palavra pertence ao dicionário"""

    return df_words['word'].isin([word]).any()

def random_select_word(df_words):
    """Retorna uma palavra aleatória para ser a referência"""

    return df_words.sample(1).iloc[0, 0]

def compare_words(word, refword):
    """
    Faz a comparação entre a palavra input e referência

    Retorna uma lista de inteiros onde cada char é:
        -1 se o caractere não pertence à palavra
        0 se o caractere pertence mas está na posição errada
        1 se o caractere pertence e está na posição correta
    """

    word = list(word)
    refword = list(refword)

    res = np.in1d(word, refword).astype(int)
    res += np.array([x == y for x, y in zip(word, refword)]).astype(int)
    return res - np.ones(len(word))
