import re

class Content(object):
    def __init__(self, begin_word='keywords', **patterns):
        self.__pattern = {}
        self.__pattern['multi_enter'] = re.compile(r'\n+')  # 匹配多个回车
        self.__pattern['start_space_types'] = re.compile(r'^[\s]+')  # 匹配空白字符开头
        # self.__pattern['not_content'] = re.compile(r'^[\s]+|- +')  # 匹配无意义组合
        self.__pattern['end_quto'] = re.compile(r'.*\w\.[0-9]$')  # 匹配结尾出现的引用
        self.__pattern['end_space'] = re.compile('[ ]+$') # 匹配结尾出现多组空格

        for k in patterns:
            self.__pattern[k] = re.compile(patterns[k])

        self.__begin_word = begin_word

    def is_article_begin(self, paragraph_str):
        '''检查keywords
        '''
        result = re.search(self.__begin_word, paragraph_str, re.IGNORECASE)
        return bool(result)

    def is_paragraph_meaningful(self, paragraph_str):
        '''检查段落是否为无意义段落
        '''
        if len(paragraph_str) == 0 or paragraph_str.isdigit() or not re.search(r'[a-zA-Z]', paragraph_str):
            return False
        return paragraph_str

    def tidy_paragraph_common(self, paragraph_str):
        '''整理一段内容
        '''
        if re.match(self.__pattern['end_quto'], paragraph_str):
            paragraph_str = paragraph_str[:-1]
        paragraph_str = re.sub(
            self.__pattern['multi_enter'], ' ', paragraph_str)
        paragraph_str = re.sub(
            self.__pattern['start_space_types'], '', paragraph_str)
        try:
            replace = re.search(
                self.__pattern['end_space'], paragraph_str).group()
            paragraph_str = re.sub(replace, '', paragraph_str)
        except AttributeError:
            pass

        return paragraph_str
    
    def tidy_paragraph_ICCAE(self, paragraph_str):
        '''
        2010 The 2nd International Conference on Computer and Automation Engineering 
        '''
        begin_figure = re.compile(r"Figure [\d]+\.")
        paragraph_str = self.tidy_paragraph_common(paragraph_str)
        return ((False if re.search(begin_figure, paragraph_str) else True) and self.is_paragraph_meaningful(paragraph_str))

    def tidy_paragraph_JAR(self, paragraph_str):
        pass

    def tidy_paragraph_LS(self, paragraph_str):
        '''
        International Conference on Logistics Systems & Intelligent Management
2010
        '''
        pass

def strQ2B(ustring):
    """全角转半角"""
    rstring = ""
    for uchar in ustring:
        inside_code=ord(uchar)
        if inside_code == 12288: #全角空格直接转换
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
            inside_code -= 65248
        rstring += chr(inside_code)
    return rstring
