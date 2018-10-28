# -*- coding: utf-8 -*-
from config import path_config
import util
import re

from pdfminer.layout import LAParams, LTTextBox, LTTextBoxHorizontal# , LTTextLine, LTFigure, LTImage, LTChar
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter, PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfdevice import PDFDevice


def check_begin(text):
    '''检查文章是否正式开始
    '''
    result = re.search(r'abstract', text, re.IGNORECASE)
    return bool(result)


def check_body(text):
    '''检查段落是否为无意义段落
    '''
    if text[-1] == ' ':
        text = text[0:-2]

    result = True

    if len(text) == 0:
        result = False

    elif text.isdigit():
        result = False

    elif not re.search(r'\w', text):
        result = False

    return result


def pdfToTxt(filename, inputPath, outputPath):  
    # 检查输出路径是否合适  
    o_f = util.retrieve_output_path(filename, outputPath)
    if not o_f:
        print('Conversion cancelled')
        return False
        
    fp = open(inputPath + '/' + filename, 'rb')
    #来创建一个pdf文档分析器
    # PDFParser：从一个文件中获取数据
    parser = PDFParser(fp)

    #创建一个PDF文档对象存储文档结构
    # PDFDocument：保存获取的数据，和PDFParser是相互关联的
    doc = PDFDocument(parser)

    # 连接分析器 与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码
    # 如果没有密码 就创建一个空的字符串
    doc.initialize()

    # 检查文件是否允许文本提取
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建一个PDF资源管理器对象来存储共享资源
        # PDFResourceManager用于存储共享资源，如字体或图像。
        rsrcmgr=PDFResourceManager()

        # 设定参数进行分析
        laparams=LAParams()

        # 创建一个PDF设备对象
        # PDFDevice将其翻译成你需要的格式
        # device=PDFDevice(rsrcmgr)

        # 创建一个PDF页面聚合对象
        device=PDFPageAggregator(rsrcmgr,laparams=laparams)

        # 创建一个PDF解释器对象
        # PDFPageInterpreter处理页面内容
        interpreter=PDFPageInterpreter(rsrcmgr,device)

        replace_n = re.compile(r'\n+')
        replace_c = re.compile(r'- +')
        begin = False

        # 处理每一页
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            layout=device.get_result()
            for x in layout:
                #如果x是水平文本对象的话
                if isinstance(x,LTTextBoxHorizontal) and hasattr(x, "get_text"):
                    text = re.sub(replace_n, ' ', x.get_text().encode('utf-8'))
                    text = re.sub(replace_c, '', text)

                    # 如果没有检查到文章起点就反复检查
                    if not begin:
                        begin = check_begin(text)
                    # begin = True
                    # 如果检查到起点且检查本段文字满足输出条件
                    if begin and check_body(text):
                        with open(outputPath + '/' + o_f, 'a') as f:
                            # f.write(x.get_text().encode('utf-8')+'\n')
                            f.write(text+'\n')
    return True


if __name__ == '__main__':
    pc = path_config()
    pap = pc.get_pap()
    tap = pc.get_tap()
    fp, dp = util.retrieve_input_path(pap)
    for file_path in fp:
        pdfToTxt(file_path, pap, tap)
