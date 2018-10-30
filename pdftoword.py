import os
import comtypes.client
from win32com.client import Dispatch
import winerror
import util
from config import path_config, word_format
from win32com.client.dynamic import Dispatch, ERRORS_BAD_CONTEXT


ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)

local_dir = util.local_path()
new_local_dir = local_dir
wf = word_format()
wdFormatPDF = wf.get_wdFormatPDF()

def get_pdf(in_file, out_file):
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()


def get_doc(input_file, output):
    avDoc = Dispatch("AcroExch.AVDoc")
    ret = avDoc.Open(input_file, input_file)
    assert(ret)
    pdDoc = avDoc.GetPDDoc()
    jsObject = pdDoc.GetJSObject()
    jsObject.SaveAs(output, "com.adobe.acrobat.docx")
    pdDoc.Close()
    avDoc.Close(True)


# def get_new_pdf(origin_pdf):
#     the_pdf_path = local_dir + origin_pdf
#     new_pdf_path = new_local_dir + origin_pdf
#     if not os.path.exists(new_pdf_path):
#         dir = os.path.dirname(new_pdf_path)
#         if not os.path.exists(dir):
#             os.makedirs(dir)
#         try:
#             get_doc(the_pdf_path, temp_file)
#             get_pdf(temp_file, new_pdf_path)
#             os.remove(temp_file)
#         except _ctypes.COMError:
#             return origin_pdf

def pdf_to_word():
    pc = path_config()
    pap = pc.get_pap()
    wap = pc.get_wap()
    fp, dp = util.retrieve_input_path(pap)
    for file_name in fp:
        o_f = util.retrieve_output_path(wap, file_name, 'docx')
        if not o_f:
            print('Conversion cancelled')
            continue
        get_doc(util.full_path(pap, file_name), util.full_path(wap, o_f))

if __name__ == '__main__':
    pdf_to_word()
