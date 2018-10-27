# -*- coding: utf-8 -*-
import comtypes.client
from win32com import client as wc
import os

def open_app(app_dir):
    os.startfile(app_dir)

def get_pdf(in_file,out_file):
    # wdFormatDocument = 0
    # wdFormatDocument97 = 0
    wdFormatDocumentDefault = 16
    # wdFormatDOSText = 4
    # wdFormatDOSTextLineBreaks = 5
    # wdFormatEncodedText = 7
    # wdFormatFilteredHTML = 10
    # wdFormatFlatXML = 19
    # wdFormatFlatXMLMacroEnabled = 20
    # wdFormatFlatXMLTemplate = 21
    # wdFormatFlatXMLTemplateMacroEnabled = 22
    # wdFormatHTML = 8
    # wdFormatRTF = 6
    # wdFormatTemplate = 1
    # wdFormatTemplate97 = 1
    # wdFormatText = 2
    # wdFormatTextLineBreaks = 3
    # wdFormatUnicodeText = 7
    # wdFormatWebArchive = 9
    # wdFormatXML = 11
    # wdFormatXMLDocument = 12
    # wdFormatXMLDocumentMacroEnabled = 13
    # wdFormatXMLTemplate = 14
    # wdFormatXMLTemplateMacroEnabled = 15
    # wdFormatXPS = 18
    wdFormatPDF = 17

    # word = comtypes.client.CreateObject('Word.Application')
    wc.gencache.EnsureDispatch('Word.Application')
    word = wc.Dispatch('Word.Application')
    doc = word.Documents.Open(in_file)
    # print(word.Selection)
    doc.SaveAs(out_file, wdFormatDocumentDefault)
    doc.Close()
    word.Quit()


if __name__== '__main__':
    in_file="D:\insWork\programming\python\parseEEDoc\pdfReader\pdf\Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.pdf"
    out_file="D:\insWork\programming\python\parseEEDoc\pdfReader\pdf\a.docx"
    
    get_pdf(in_file, out_file)
    # app_dir = r'C:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe'
    # open_app(app_dir)