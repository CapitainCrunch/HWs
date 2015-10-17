__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import sqlite3
import collections
import re

class SQL():
    def __init__(self, test_db):
        self.connection = sqlite3.connect(test_db, check_same_thread=False)
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.table = 'CREATE TABLE freqDict (WORD TEXT, COUNT INTEGER)'
        self.cursor.execute(self.table)

    def insert(self, word, count):
        query = 'INSERT into freqDict VALUES ("{}", {})'.format(word, count)
        self.cursor.execute(query)
        self.connection.commit()

    def add_count(self, count, word):
        query = 'UPDATE freqDict SET COUNT = {} where WORD = "{}"'.format(count, word)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def check_word(self, word):
        query = 'SELECT COUNT FROM freqDict where WORD = "{}"'.format(word)
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_all(self):
        query = 'SELECT * FROM freqDict'
        self.cursor.execute(query)
        return self.cursor.fetchall()


f_in = open('./dump.xml', 'r', encoding='utf8')
f_out = open('csv_table.csv', 'w', encoding='utf8')
sql = SQL('freqDict.db')
try:
    sql.create_table()
except:
    pass
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
        text = regex_text.findall(page)
        if text == []:
            pass
        else:
            for word in (text[0].split(' ')):
                if sql.check_word(word.strip('[]!\"#\'')) == []:
                    sql.insert(word, 0)
                else:
                    sql.add_count(int(sql.check_word(word.strip('[]!\"#\''))[0][0]) + 1, word.strip('[]!\"#\''))
        page = ''
    continue

f_in.close()
f_out.close()