from .config.Config import PathConfig
from .convert import folder_converter

def get_document():
    pc = PathConfig()
    pap = pc.get_pap()
    wap = pc.get_wap()
    tap = pc.get_tap()
    folder_converter(pap, 'pdf_to_word', wap)
    return folder_converter(wap, 'word_to_txt', tap)

if __name__ == '__main__':
    print(get_document())
