# -*- coding: utf-8 -*-
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import os, re

def readPath(path):
    '''
    获取一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(path)
    for f in files:
        f_full = path + '/' + f
        if(os.path.isdir(f_full)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(f[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(f)
        if(os.path.isfile(f_full)):
            # 添加文件
            portion = os.path.splitext(f)
            if portion[1] == '.pdf':
                fileList.append(f)
            else:
                print('The file \"' + f + '\" is not a pdf document')
                
    return fileList, dirList


def pathReady(filename, inputPath, outputPath):
    ''''
    监测输出文件夹是否准备妥当
    '''
    portion = os.path.splitext(filename)
    outputFile = portion[0] + '.txt'

    if not os.path.exists(outputPath):
        os.mkdir(outputPath)
        return outputFile
    
    if(os.path.exists(outputPath + '/' + outputFile)):
        while True:
            toGo = raw_input(
                'The file \"' + outputFile + '\" already exists. Continue conversion will overwrite the original file. Continue?[Y/N]')
            if (toGo.lower() == 'y'):
                os.remove(outputPath + '/' + outputFile)
                return outputFile
            elif (toGo.lower() == 'n'):
                return False
            else:
                print('[InputError: Invalid input, try Y or N]')
    else:
        return outputFile

def pdfToTxt(filename, inputPath, outputPath):  
    # 检查输出路径是否合适  
    o_f = pathReady(filename, inputPath, outputPath)
    if not o_f:
        print('Conversion cancelled')
        return False
        
    fp = open(inputPath + '/' + filename, 'rb')
    #来创建一个pdf文档分析器
    # PDFParser：从一个文件中获取数据
    parser = PDFParser(fp)

    #创建一个PDF文档对象存储文档结构
    # PDFDocument：保存获取的数据，和PDFParser是相互关联的
    document = PDFDocument(parser)

    # 检查文件是否允许文本提取
    if not document.is_extractable:
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
        for page in PDFPage.create_pages(document):
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


def check_begin(text):
    '''检查文章是否正式开始
    '''
    result = re.search(r'abstract', text, re.IGNORECASE)

    return bool(result)


def check_body(text):
    '''检查文章是否正式开始
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

if __name__ == '__main__':
    pdfPath = './pdf'
    txtPath = './txt'
    fileInPath, dirInPath = readPath('./pdf')
    for filePath in fileInPath:
        pdfToTxt(filePath, pdfPath, txtPath)
