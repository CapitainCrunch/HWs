from lxml import etree
from collections import Counter
import numpy as np
from sklearn import svm, grid_search

TAGS = ['ADVPRO', 'ADV', 'A', 'ANUM', 'CONJ', 'APRO', 'COM', 'INTJ', 'S', 'SPRO', 'V', 'PR', 'NUM', 'PART']


def collect_texts(fname):
    parser = etree.HTMLParser()
    tree = etree.parse(fname, parser).getroot()[0]
    sentences = [' '.join([elem.text + elem.tail.strip() for elem in sentence]) for sentence in tree] 
    pos_counts = [Counter([elem[0].attrib['gr'].split('=')[0].split(',')[0] for elem in sentence if len(elem) != 0]) for sentence in tree]
    return sentences, pos_counts



k_sentences, k_tags = collect_texts('kapital.xml')
voina_sents, voina_pos = collect_texts('voina.xml')

k_table = np.array([[d[i] for i in TAGS] for d in k_tags])
v_table = np.array([[d[i] for i in TAGS] for d in voina_pos])

data = np.vstack((k_table, v_table))
target = np.array([0 for _ in k_tags] + [1 for _ in voina_pos])

parameters = {'C': (.1, .5, 1.0)}
gs = grid_search.GridSearchCV(svm.LinearSVC(), parameters)
gs.fit(data, target)
print(k_table)

print(gs.best_score_)

best = gs.best_estimator_

true_examples = []
false_examples = []
for i in range(len(k_table)):
    guess = best.predict(k_table[i].reshape(1, -1))
    if guess != 0:
        if len(false_examples) < 3:
            false_examples.append((k_sentences[i], k_table[i]))
    else:
        if len(true_examples) < 3:
            true_examples.append((k_sentences[i], k_table[i]))
    if len(false_examples) >= 3 and len(true_examples) >= 3:
        break

print('Ошибки ')
for i in false_examples:
    print('   ', i[0], i[1])
print('Верные угадки: ')
for i in true_examples:
    print('   ', i[0], i[1])

