__author__ = 'Bogdan'
__email__ = 'evstrat.bg@gmail.com'
__mobile_phone__ = 89252608400

import requests
import re
import bz2

lang = str(input('Какой язык? '))

def url_dumps():
    url = 'http://dumps.wikimedia.org/' + define_lang(lang.capitalize()) + 'wiki/' + get_date_dump() + '/' + define_lang(lang.capitalize()) + 'wiki-' + get_date_dump() + '-pages-articles-multistream.xml.bz2'
    return url

def define_lang(in_lang):
    url = 'https://ru.wikipedia.org/wiki/Коды_языков'
    page = requests.get(url)
    to_lang = re.findall('title=".*?">' + in_lang + '</a></td>\\n<td>(.*?)</td>\\n<td>(.*?)</td>',page.content.decode('utf8'), flags=re.DOTALL)
    if to_lang[0][0] == '-':
        return to_lang[0][1]

    elif to_lang[0][0] != '-':
        return to_lang[0][0]

    else:
        raise TypeError('NoLangDetected')

def get_date_dump():
    url = 'http://dumps.wikimedia.org/' + define_lang(lang.capitalize()) + 'wiki'
    page = requests.get(url)
    date = re.search('<a href=".*">(.*?)/</a.*?<a href="latest/">latest/</a>', page.content.decode('utf8)'), flags=re.DOTALL)
    merged_date = date.group(1)
    return merged_date


def download_file(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()
    return local_filename

#download_file(url_dumps())


#____________2_____________



def dump_parse():
    f_out = open('article_names.txt', 'w', encoding='utf8')
    fname = '-'.join(url_dumps().split('/')[-1:])[:-4]
    regex = re.compile('<title>(.*?)</title>', flags=re.DOTALL)
    all_titles = []
    with open('/Users/Bogdan/Desktop/HWs/' + fname, 'r') as f:
        for line in f:
            re_titles = regex.findall(line)
            if len(re_titles) > 0:
                all_titles += re_titles

    for title in sorted(all_titles, key=lambda x: x[0]):
        f_out.write(title + '\r\n')

    f.close()
    f_out.close()


#dump_parse()
