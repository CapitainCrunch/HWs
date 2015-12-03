__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import numpy as np
from lxml import etree
from matplotlib import mlab
from matplotlib import pyplot as plt



def parse_corpus(cname):
    parser = etree.HTMLParser()
    tree = etree.parse(cname, parser).getroot()[0]
    sents = [[word[0].attrib['gr'].split('=')[0].split(',')[0] for word in sent if len(word) != 0] for sent in tree]
    full_arr = []
    for sent in sents:
        arr = []
        a, s, v, adv, spro = 0, 0, 0, 0, 0
        for abbr in sent:
            if abbr == 'S':
                s += 1
            if abbr == 'A':
                a += 1
            if abbr == 'ADV':
                adv += 1
            if abbr == 'SPRO':
                spro += 1
        arr += a, s, v, adv, spro
        full_arr.append(arr)

    return full_arr

#print(parse_corpus('corpus1.txt'))

sonets = parse_corpus('corpus1.txt')
anna = parse_corpus('corpus2.txt')

# ПОДСКАЖИТЕ ПОЧЕМУ НЕ РАБОТЕТ Я УЖЕ ЗАПУТАЛСЯ ХЕЛП ЗАРАНЕЕ СПАСИБО :)

data = np.vstack((np.array(sonets), np.array(anna)))
print(data)
p = mlab.PCA(data, True)
N = len(np.array(sonets))
print(p.Wt)

plt.plot(p.Y[N:,0], p.Y[N:,1], 'or', p.Y[:N,0], p.Y[:N,1], 'sb')
plt.show()


