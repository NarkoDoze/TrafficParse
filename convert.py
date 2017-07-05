#-*- coding: utf-8 -*-
import codecs
import os

directory = os.listdir()
for fname in directory:
    if (fname.endswith('.csv')):
        with codecs.open(fname, 'r', encoding='euc-kr') as file:
            lines = file.read()
        with codecs.open('u' + fname, 'w', encoding='utf-8') as file:
            file.write(lines)
