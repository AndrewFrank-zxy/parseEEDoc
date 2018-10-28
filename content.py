import re


def check_begin(text):
    '''检查keywords
    '''
    result = re.search(r'Keywords:', text, re.IGNORECASE)
    return bool(result)


def tidy_para_text(paragraph):
    '''整理一段内容，清理不合理回车和‘- ’
    '''
    replace_n = re.compile(r'\n+')
    replace_c = re.compile(r'- +')
    text = re.sub(replace_n, ' ', paragraph)
    return re.sub(replace_c, '', text)
