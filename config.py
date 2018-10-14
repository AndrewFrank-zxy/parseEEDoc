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
        self.takp = setting['txt_article_keywords_path']
        self.tasp = setting['txt_article_summary_path']
    
    def get_pap(self):
        return self.pap

    def get_tap(self):
        return self.tap

    def get_takp(self):
        return self.takp

    def get_tasp(self):
        return self.tasp
