import re


def check_begin(paragraph):
    '''检查keywords
    '''
    result = re.search(r'Keywords:', paragraph, re.IGNORECASE)
    return bool(result)


def tidy_para_text(paragraph):
    '''整理一段内容，清理不合理回车和‘- ’
    '''
    replace_n = re.compile(r'\n+')
    replace_c = re.compile(r'- +')
    text = re.sub(replace_n, ' ', paragraph)
    return re.sub(replace_c, '', text)


def check_paragraph(paragraph):
    '''检查段落是否为无意义段落
    '''
    match_es = re.compile('[ ]+$')
    try:
        replace_es = re.search(match_es, paragraph).group()
        paragraph = re.sub(replace_es, '', paragraph)
    except AttributeError:
        pass
    result = True
    if len(paragraph) == 0 or paragraph.isdigit() or not re.search(r'\w', paragraph):
        result = False
    return result
