from docx import Document
import content
import re


def check_font_size(run):
    '''检查字体大小
    '''
    try:
        return run.font.size.pt
    except AttributeError:
        return 'None'


def get_text(paragraphs):
    '''检查处理正文信息
    '''
    to_write = ""
    for paragraph in paragraphs:
        par_str = paragraph.text
        par_runs = paragraph.runs
        if len(par_runs):
            if len(par_str) and check_font_size(par_runs[0]) == 'None':
                # print("=====================================")
                par_str = content.tidy_para_text(par_str)
                if par_str[0].islower():
                    to_write = to_write[:-1] + ' ' + par_str + '\n'
                else:
                    to_write = to_write + par_str + '\n'
    return to_write


def save_txt(filename, all_txt):
    '''保存正文内容到文件
    '''
    with open(filename, 'a') as f:
        f.write(all_txt)


if __name__ == "__main__":
    doc = Document(
        "F:\\PerStudy\\Desktop\\ParticipleDocs\\parseEEDoc\\articles-word\\Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties01.docx")
    
    save_txt("F:\\PerStudy\\Desktop\\ParticipleDocs\\parseEEDoc\\articles-txt\\Debtholders' Demand for Conservatism Evidence from Changes in Directors' Fiduciary Duties.txt", get_text(doc.paragraphs))
