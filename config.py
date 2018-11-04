# -*- coding: utf-8 -*-
import json


class path_config(object):
    """定义"""

    def __init__(self, config_file="./config.json"):
        self.config_file = config_file
        self.load_path()

    def load_path(self):
        f = open(self.config_file, 'r')
        setting = json.load(f)
        self.pap = setting['pdf_articles_path']
        self.tap = setting['txt_articles_path']
        self.wap = setting['word_articles_path']
        self.trkp = setting['txt_results_keywords_path']
        self.trsp = setting['txt_results_summaries_path']
        self.rgp = setting['results_graphs_path']
    
    def get_pap(self):
        return self.pap

    def get_tap(self):
        return self.tap

    def get_wap(self):
        return self.wap

    def get_trkp(self):
        return self.trkp

    def get_trsp(self):
        return self.trsp

    def get_rgp(self):
        return self.rgp


class word_format(object):
    """定义"""

    def __init__(self, config_file="./config.json"):
        self.config_file = config_file
        self.load_format()

    def load_format(self):
        f = open(self.config_file, 'r')
        setting = json.load(f)
        self.format = setting['format']

    def get_wdFormatDocument(self):
        return self.format['wdFormatDocument']

    def get_wdFormatDocument97(self):
        return self.format['wdFormatDocument97']

    def get_wdFormatDocumentDefault(self):
        return self.format['wdFormatDocumentDefault']

    def get_wdFormatDOSText(self):
        return self.format['wdFormatDOSText']

    def get_wdFormatDOSTextLineBreaks(self):
        return self.format['wdFormatDOSTextLineBreaks']

    def get_wdFormatEncodedText(self):
        return self.format['wdFormatEncodedText']

    def get_wdFormatFilteredHTML(self):
        return self.format['wdFormatFilteredHTML']

    def get_wdFormatFlatXML(self):
        return self.format['wdFormatFlatXML']

    def get_wdFormatFlatXMLMacroEnabled(self):
        return self.format['wdFormatFlatXMLMacroEnabled']

    def get_wdFormatFlatXMLTemplate(self):
        return self.format['wdFormatFlatXMLTemplate']

    def get_wdFormatFlatXMLTemplateMacroEnabled(self):
        return self.format['wdFormatFlatXMLTemplateMacroEnabled']

    def get_wdFormatHTML(self):
        return self.format['wdFormatHTML']

    def get_wdFormatRTF(self):
        return self.format['wdFormatRTF']

    def get_wdFormatTemplate(self):
        return self.format['wdFormatTemplate']

    def get_wdFormatTemplate97(self):
        return self.format['wdFormatTemplate97']

    def get_wdFormatText(self):
        return self.format['wdFormatText']

    def get_wdFormatTextLineBreaks(self):
        return self.format['wdFormatTextLineBreaks']

    def get_wdFormatUnicodeText(self):
        return self.format['wdFormatUnicodeText']

    def get_wdFormatWebArchive(self):
        return self.format['wdFormatWebArchive']

    def get_wdFormatXML(self):
        return self.format['wdFormatXML']

    def get_wdFormatXMLDocument(self):
        return self.format['wdFormatXMLDocument']

    def get_wdFormatXMLDocumentMacroEnabled(self):
        return self.format['wdFormatXMLDocumentMacroEnabled']

    def get_wdFormatXMLTemplate(self):
        return self.format['wdFormatXMLTemplate']

    def get_wdFormatXMLTemplateMacroEnabled(self):
        return self.format['wdFormatXMLTemplateMacroEnabled']

    def get_wdFormatXPS(self):
        return self.format['wdFormatXPS']

    def get_wdFormatPDF(self):
        return self.format['wdFormatPDF']
