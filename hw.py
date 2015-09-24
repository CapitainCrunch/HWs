__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import re
import time

f = open('long_poem.txt', 'r', encoding='utf-8')
in_words = open('words.txt', 'r', encoding='utf-8')
f_out = open('snippets.txt', 'w', encoding='utf8')
f_out2 = open('rhymes.txt', 'w', encoding='utf8')

#clear_text = re.sub('[.!,-:/?")(]', '', f.read())

lines = []
num_lines = {}
LAST_LINE = 0
for num, line in enumerate(f):
    num_lines[num] = line
    lines.append(line)
    LAST_LINE += 1

f.close()

def find():
    f = open('long_poem.txt', 'r', encoding='utf-8')
    words_set = set()
    for l in f:
        l = l.split()
        for w in l:
            w = w.strip('.:-…/",)(!?')
            words_set.add(w)
    f.close()


    index = {}
    for word in words_set:
        arr = []
        for key, value in num_lines.items():
            m = re.search('(.*?)\s.*?' + word + '.*?', value)
            if m != None:
                arr.append(key)
        index[word.lower()] = arr
    return index

in_words_dict = {}
for string in in_words:
    string = string.strip('\n')
    in_words_dict[string.split(' ')[0]] =  string.split(' ')[1]


def start():
    f_out = open('snippets.txt', 'w', encoding='utf8')
    a = time.time()
    for in_word in in_words_dict.values():
        for k,v in find().items():
            if in_word == k:
                for i in v:
                    if i == LAST_LINE:
                        f_out.write(lines[i-1])
                        f_out.write(lines[i])
                    elif i == 0:
                        f_out.write(lines[i])
                        f_out.write(lines[i+1])
                    else:
                        f_out.write(lines[i-1])
                        f_out.write(lines[i])
                        f_out.write(lines[i+1])
    b = time.time()
    print(b-a)
    f_out.close()

"""Если хватит терпения, то запускай то, что сверху :D"""

def second():
    f_out = open('snippets.txt', 'w', encoding='utf8')
    words_in = open('words.txt', 'r', encoding='utf-8')
    for user_word in words_in:
        user_word = user_word.strip('\n')
        user_word = '\\b' + user_word + '\\b'
        f_in = open('long_poem.txt', 'r', encoding='utf-8')
        a = time.time()
        lines = re.findall('.*?\\n.*?' + user_word + '.*?\\n.*?\\n', f_in.read())
        b = time.time()
        f_in.close()
        for i in lines:
            f_out.write(i)
    f_out.close()


"""_______________________________________2________________________"""

numerate_lines = ''
for num, line in num_lines.items():
    numerate_lines += str(num) + ' ' + line

found_words = set()
for n, word in in_words_dict.items():
    word = word.strip('\n')
    endings = re.search('.*([а-я].*?[а-я].*)', word)
    end = endings.group(1)
    x = time.time()
    num_word = re.findall('(\\d+)\\s.*?(\\w+' + end + ')$', numerate_lines , re.MULTILINE)
    for number, found_word in num_word:
        #print(number, found_word)
        if int(number) - 2 == int(n) or int(number) - 1 == int(n) or int(number) == int(n) or int(number) + 1 == int(n) or int(number) + 2 == int(n):
            found_words.add(found_word)
    y = time.time()

for i in found_words:
    f_out2.write(i + '\n')