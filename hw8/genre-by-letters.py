__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import numpy as np
from matplotlib import pyplot as plt
import re

with open('corpus1.txt', encoding='utf8') as f:
    media = f.read()

with open('corpus2.txt', encoding='utf8') as f2:
    anna = f2.read()

media_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', media)
anna_sentences = re.split(r'(?:[.]\s*){3}|[.?!]', anna)

def words(sentence):
    return [len(word) for word in sentence.split()]

anna_sentlens = [words(sentence) for sentence in anna_sentences if len(words(sentence)) > 0]
media_sentlens = [words(sentence) for sentence in media_sentences if len(words(sentence)) > 0]
anna_data = [(len(sentence), np.mean(sentence), np.median(sentence), np.std(sentence))
             for sentence in anna_sentlens]
media_data = [(len(sentence), np.mean(sentence), np.median(sentence), np.std(sentence)) for
              sentence in media_sentlens]

anna_data = np.array(anna_data)
print(anna_data)
print('___________')
media_data = np.array(media_data)
print(media_data)

plt.figure()
c1, c2 = 0, 1
plt.plot(anna_data[:,c1], anna_data[:,c2], 'og',
         media_data[:,c1], media_data[:,c2], 'sr')
plt.show()