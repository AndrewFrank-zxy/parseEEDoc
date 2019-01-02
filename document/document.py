from .config.Config import PathConfig
from .convert import folder_converter

def read_txt(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def get_document(type='byPDF', filename=''):
    if type == 'byPDF':
        pc = PathConfig()
        pap = pc.get_pap()
        wap = pc.get_wap()
        folder_converter(pap, 'pdf_to_word', wap)
        return folder_converter(wap, 'get_word')
    elif type == 'byTXT':
        return read_txt(filename)

if __name__ == '__main__':
    print(get_document())
