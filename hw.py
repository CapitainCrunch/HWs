__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import re
import time

f = open('long_poem.txt', 'r', encoding='utf-8')
in_words = open('words.txt', 'r', encoding='utf-8')
f_out = open('snippets.txt', 'w', encoding='utf8')

clear_text = re.sub('[.!,-:?")(]', '', f.read())

num_lines = {}
for num, line in enumerate(clear_text):
    num_lines[num] = line


f = open('long_poem.txt', 'r', encoding='utf-8')
words_set = set()
for l in f:
    l = l.split()
    for w in l:
        w = w.strip('.:-/",)(!?')
        words_set.add(w)

index = {}
for word in words_set:
    arr = []
    print(word)
    for key, value in num_lines.items():
        m = re.search('\\b' + word + '\\b', value)
        if m != None:
            arr.append(key)
    index[word] = arr
for k,v in index.items():
    print(k,v)





