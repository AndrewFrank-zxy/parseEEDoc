# -*- coding: utf-8 -*-
import os


def retrieve_input_path(path, file_type = 'pdf'):
    '''
    获取一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dl = []
    # 所有文件
    fl = []
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
                dl.append(f)
        if(os.path.isfile(f_full)):
            # 添加文件
            portion = os.path.splitext(f)
            if portion[1] == '.' + file_type:
                fl.append(f)
            else:
                print('The file \"' + f + '\" is not a '+ file_type + ' document')

    return fl, dl


def retrieve_output_path(filename, Path):
    '''
    监测输出文件夹是否准备妥当
    '''
    portion = os.path.splitext(filename)
    output_file = portion[0] + '.txt'

    if not os.path.exists(Path):
        os.mkdir(Path)
        return output_file

    if(os.path.exists(Path + '/' + output_file)):
        while True:
            print('The file \"' + output_file + '\" in path \"' + Path + '\" already exists.')
            toGo = raw_input(
                'Continue conversion/parsing will overwrite the original file. Continue?[Y/N]')
            if (toGo.lower() == 'y'):
                os.remove(Path + '/' + output_file)
                return output_file
            elif (toGo.lower() == 'n'):
                return False
            else:
                print('[InputError: Invalid input, try Y or N]')
    else:
        return output_file
