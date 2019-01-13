from .config.Config import PathConfig
from .convert import folder_converter
from .utils.util import ModefyPath, save_txt
import logging
mp = ModefyPath()


def save_result(file_name, file_result):
    pc = PathConfig()
    trap = pc.get_trap()
    o_f = mp.retrieve_file(trap, file_name, 'txt')
    if not o_f:
        logging.info('Conversion cancelled')
        return False
    output_file = mp.get_full_path(trap, o_f)
    save_txt(output_file, file_result)
    return True
