import collections
import re

f_in = open('./dump.xml', 'r', encoding='utf8')
f_out = open('csv_table.csv', 'w', encoding='utf8')
c = collections.Counter()
regex_title = re.compile('<title>(.*?)</title>', re.DOTALL)
regex_refs = re.compile('\\[\\[', re.DOTALL)
regex_text = re.compile('<text.*?>(.*?)</text>')

page = ''
for line in f_in:
    if '<page>' in line:
        page += line
    page += line
    if '</page>' in line:
        page += line
        title = regex_title.findall(page)
        refs = regex_refs.findall(page)
        text = regex_text.findall(page)
        if not text:
            f_out.write(title[0] + ';' + str(len(refs)) + ';' + 'None' + '\r\n')
        else:
            count_words = str(len(text[0].split(' ')))
            f_out.write(title[0] + ';' + str(len(refs)) + ';' + count_words + '\r\n')
            i = 1
            for word in text[0].split(' '):
                c[word] += 1
        page = ''
    continue

f_in.close()
f_out.close()
