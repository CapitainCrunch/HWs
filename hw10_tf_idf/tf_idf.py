from lxml import etree
from collections import Counter
import os
from math import log


def collect_texts():
    texts = []
    for root, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('xml'):
                parser = etree.HTMLParser()
                tree = etree.parse(root + '/' + f, parser).getroot()[0]
                words = [word[0].attrib['lex'] for sentence in tree for word in sentence if len(word) > 0 ]
                texts.append((f, words))
    return texts


def unique_lemms(texts):
    uniq_lemms = set()
    for text in texts:
        uniq_lemms.update(text[1])
    return uniq_lemms


def idf_dict(lemms, texts):
    l = len(texts)
    d = {}
    for lemm in lemms:
        d.update({lemm: log(l/sum([lemm in text[1] for text in texts]))})
    return d



def tfidf_dict(texts, idf, lems):
    t = {}
    for text in texts:
        t.update({text[0]: Counter(text[1])})
    d = {}
    for x in lems:
        for y in t:
            d[(x,y)] = (t[y][x]/len(t[y]))*idf[x]
    return d


texts = collect_texts()
uniq = unique_lemms(texts)
idf = idf_dict(uniq, texts)
tf_idf = tfidf_dict(texts, idf, uniq)
for k, v in sorted(tf_idf.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(str(v) + ' <--- "' + k[0] + '" из файла "' + k[1] + '"')
