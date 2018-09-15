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
import os
fp = open('1-s2.0-S0304414908001877-main.pdf', 'rb')

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
    # 创建一个PDF资源管理器对象来存储共赏资源
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

    # 处理每一页
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout=device.get_result()
        for x in layout:
            if(isinstance(x,LTTextBoxHorizontal)):
                with open('output.txt','a') as f:
                    f.write(x.get_text().encode('utf-8')+'\n')