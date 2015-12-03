__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import numpy as np
import re
from matplotlib import pyplot as plt
from matplotlib import mlab


with open('anna.txt', encoding='utf-8') as f:
    anna = f.read()
with open('sonets.txt', encoding='utf-8') as f:
    sonets = f.read()

anna_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', anna)
sonet_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', sonets)

#  just for test
def count_vowels(sentences):
    d = {}
    c = 1
    for sent in sentences:
        d[c] = ''
        for word in words(sent):
            for letter in word:
                if letter.lower() not in d[c] and letter.lower() in 'еёыаоэяию':
                    d[c] += letter.lower()
                else:
                    continue
        c += 1
    return d


def count_vowels_word(sentences):
    d = {}
    c = 1
    for sent in sentences:
        d[c] = []
        for word in words(sent):
            v_words = []
            for letter in word:
                if letter.lower() not in d[c] and letter.lower() in 'еёыаоэяию':
                    v_words.append(letter.lower())
                else:
                    continue
            d[c].append(v_words)
        c += 1
    return d



#_______________________


def word(sentence):
    return sentence.lower().split()


def vowels_in_sent(sentence):
    return [vowels_count(word) for word in sentence]


def len_words(sentence):
    return [len(i) for i in sentence]


def diff_letters(sentence):
    ALPHABET = 'йцукенёгшщзхъфывапролджэячсмитьбю'
    letters = set()
    for word in sentence:
        for letter in word:
            if letter.lower() in ALPHABET:
                letters.add(letter)
    return len(letters)


def vowels_count(word):
    VOWELS = 'уеёэоаыяию'
    num = 0
    for letter in word:
        if letter in VOWELS:
            num += 1
    return num


anna_sent = [word(sentence) for sentence in anna_sentences if len(word(sentence)) > 0]
sonet_sent = [word(sentence) for sentence in sonet_sentences if len(word(sentence)) > 0]

anna_data = [(sum(len_words(sentence)),  diff_letters(sentence),  sum(vowels_in_sent(sentence)),
              np.median(len_words(sentence)),  np.median(vowels_in_sent(sentence))) for sentence in anna_sent]

sonet_data = [(sum(len_words(sentence)), diff_letters(sentence), sum(vowels_in_sent(sentence)),
              np.median(len_words(sentence)), np.median(vowels_in_sent(sentence))) for sentence in sonet_sent]


anna_data = np.array(anna_data)
sonet_data = np.array(sonet_data)


data = np.vstack((anna_data, sonet_data))
p = mlab.PCA(data, True)
N = len(anna_data)

plt.plot(p.Y[:N,0], p.Y[:N,1], 'og', p.Y[N:,0], p.Y[N:,1], 'sb')
plt.show()
print(p.Wt)