# -*- coding: utf-8 -*-
import os
import re

replace_pdb = re.compile(r'^[.\\/][\\/]*')
replace_fd = re.compile(r'^.')
replace_pd = re.compile(r'[\\/]+')

def local_path():
    '''
    获取当前文件夹完整路径
    '''
    return os.getcwd()


def full_path(*path):
    '''
    拼接完成完整路径
    '''
    f_p = local_path()
    for p in path:
        try:
            pdb = re.match(replace_pdb, p).group()
            p = p.replace(pdb, '', 1)
        except AttributeError:
            pass
            # print('The input path \"' + p + '\" dont include root path')
        p = re.split(replace_pd, p)
        for each in p:
            f_p = os.path.join(f_p, each)
    return f_p


def full_local_path(*path):
    '''
    拼接完成相对路径
    '''
    f_p = '.'
    for p in path:
        try:
            pdb = re.match(replace_pdb, p).group()
            p = p.replace(pdb, '', 1)
        except AttributeError:
            pass
            # print('The input path \"' + p + '\" dont include root path')
        p = re.split(replace_pd, p)
        for each in p:
            f_p = os.path.join(f_p, each)
    return f_p


def retrieve_input_path(in_path, file_type = 'pdf'):
    '''
    监测输入文件夹，并获取所有子文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dl = []
    # 所有文件
    fl = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    files = os.listdir(in_path)
    for f in files:
        f_full = full_local_path(in_path, f)
        if(os.path.isdir(f_full)):
            # 排除隐藏文件夹。因为隐藏文件夹可能过多
            if not re.match(replace_fd, f):
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


def retrieve_output_path(out_path, filename, file_type='txt'):
    '''
    监测输出文件夹是否准备妥当
    '''
    portion = os.path.splitext(filename)
    output_file = portion[0] + '.' + file_type

    if not os.path.exists(out_path):
        os.mkdir(out_path)
        return output_file

    o_f_p = full_local_path(out_path, output_file)
    if os.path.exists(o_f_p):
        while True:
            print('The file \"' + output_file + '\" in path \"' +
                  out_path + '\" already exists.')
            toGo = input(
                'Continue conversion/parsing will overwrite the original file. Continue?[Y/N]')
            if toGo.lower() == 'y':
                os.remove(o_f_p)
                return output_file
            elif toGo.lower() == 'n':
                return False
            else:
                print('[InputError]: Invalid input, try Y or N')
    else:
        return output_file


def save_txt(filename, all_txt):
    '''保存正文内容到文件
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(all_txt)
        

if __name__ == '__main__':
    print("1:", full_local_path('.\\bbbb//cc//cc', 'ccccc.txt'))
    print("2:", retrieve_input_path('.\\articles-pdf'))
    print("3:", retrieve_output_path('articles-txt', '2.txt', 'doc'))
    test = re.compile('[ ]+$')
    replace_es = re.search(test, 'sdf12  ').group()
    print(re.sub(replace_es, '1', 'sdf12  '))
