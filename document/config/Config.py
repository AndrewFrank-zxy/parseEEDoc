# -*- coding: utf-8 -*-
import os
import json
import logging
current_path = os.path.dirname(__file__)

class Config(object):
    def __init__(self, config_file="./config.json"):
        self.config_file = config_file


class PathConfig(Config):
    """定义"""

    def __init__(self, config_file=current_path + "/config.json"):
        Config.__init__(self, config_file)
        self.load_path()

    def load_path(self):
        f = open(self.config_file, 'r')
        setting = json.load(f)
        self.__pap = setting['pdf_articles_path']
        self.__tap = setting['txt_articles_path']
        self.__wap = setting['word_articles_path']
        self.__trap = setting['txt_results_all_path']
        self.__trkp = setting['txt_results_keywords_path']
        self.__trsp = setting['txt_results_summaries_path']
        self.__prgp = setting['png_results_graphs_path']
    
    def get_pap(self):
        return self.__pap

    def get_tap(self):
        return self.__tap

    def get_wap(self):
        return self.__wap

    def get_trap(self):
        return self.__trap

    def get_trkp(self):
        return self.__trkp

    def get_trsp(self):
        return self.__trsp

    def get_prgp(self):
        return self.__prgp


class WordFormat(Config):
    """定义"""

    def __init__(self, config_file=current_path + "/config.json"):
        Config.__init__(self, config_file)
        self.load_format()

    def load_format(self):
        f = open(self.config_file, 'r')
        setting = json.load(f)
        self.__format = setting['format']

    def get_format(self, format="Document"):
        try:
            return self.__format['wdFormat' + str(format)]
        except KeyError:
            logging.error("No such format type. Set with default value `0`")
            return 0

    # def get_wdFormatDocument(self):
    #     return self.__format['wdFormatDocument']

    # def get_wdFormatDocument97(self):
    #     return self.__format['wdFormatDocument97']

    # def get_wdFormatDocumentDefault(self):
    #     return self.__format['wdFormatDocumentDefault']

    # def get_wdFormatDOSText(self):
    #     return self.__format['wdFormatDOSText']

    # def get_wdFormatDOSTextLineBreaks(self):
    #     return self.__format['wdFormatDOSTextLineBreaks']

    # def get_wdFormatEncodedText(self):
    #     return self.__format['wdFormatEncodedText']

    # def get_wdFormatFilteredHTML(self):
    #     return self.__format['wdFormatFilteredHTML']

    # def get_wdFormatFlatXML(self):
    #     return self.__format['wdFormatFlatXML']

    # def get_wdFormatFlatXMLMacroEnabled(self):
    #     return self.__format['wdFormatFlatXMLMacroEnabled']

    # def get_wdFormatFlatXMLTemplate(self):
    #     return self.__format['wdFormatFlatXMLTemplate']

    # def get_wdFormatFlatXMLTemplateMacroEnabled(self):
    #     return self.__format['wdFormatFlatXMLTemplateMacroEnabled']

    # def get_wdFormatHTML(self):
    #     return self.__format['wdFormatHTML']

    # def get_wdFormatRTF(self):
    #     return self.__format['wdFormatRTF']

    # def get_wdFormatTemplate(self):
    #     return self.__format['wdFormatTemplate']

    # def get_wdFormatTemplate97(self):
    #     return self.__format['wdFormatTemplate97']

    # def get_wdFormatText(self):
    #     return self.__format['wdFormatText']

    # def get_wdFormatTextLineBreaks(self):
    #     return self.__format['wdFormatTextLineBreaks']

    # def get_wdFormatUnicodeText(self):
    #     return self.__format['wdFormatUnicodeText']

    # def get_wdFormatWebArchive(self):
    #     return self.__format['wdFormatWebArchive']

    # def get_wdFormatXML(self):
    #     return self.__format['wdFormatXML']

    # def get_wdFormatXMLDocument(self):
    #     return self.__format['wdFormatXMLDocument']

    # def get_wdFormatXMLDocumentMacroEnabled(self):
    #     return self.__format['wdFormatXMLDocumentMacroEnabled']

    # def get_wdFormatXMLTemplate(self):
    #     return self.__format['wdFormatXMLTemplate']

    # def get_wdFormatXMLTemplateMacroEnabled(self):
    #     return self.__format['wdFormatXMLTemplateMacroEnabled']

    # def get_wdFormatXPS(self):
    #     return self.__format['wdFormatXPS']

    # def get_wdFormatPDF(self):
    #     return self.__format['wdFormatPDF']

if __name__ == "__main__":
    pc = WordFormat()
    print(pc.get_format('wdFormatPDF'))
