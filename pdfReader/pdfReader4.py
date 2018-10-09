#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/6 21:02
# @Author  : chen
# @Site    : 
# @File    : simplePDF.py
# @Software: PyCharm
import os
from cStringIO import StringIO
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
def convert_pdf_2_text(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    with open(path, 'rb') as fp:
        for page in PDFPage.get_pages(fp, set()):
            interpreter.process_page(page)
        text = retstr.getvalue()
    device.close()
    retstr.close()
    return text
    
if __name__ == '__main__':
    result = convert_pdf_2_text('./pdf/01.pdf')
    with open('./pdf/01.txt', 'a') as f:
        # f.write(x.get_text().encode('utf-8')+'\n')
        f.write(result)
