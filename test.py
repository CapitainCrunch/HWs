__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import re
s = 'Склонясь над книгою! (следить) сквозь дым словесный'

s1 = re.sub('[!()]', '', s)
print(s1)