# -*- coding: utf-8 -*-
import os
import re
import logging
logging.getLogger().setLevel(logging.INFO)
# full_filename代表完整文件名
# filename完整文件名或仅包含文件名
class ModefyPath(object):
    def __init__(self, **patterns):
        self.__pattern = {}
        self.__pattern['depart'] = re.compile(r'[\\/]+') #分割
        self.__pattern['begin'] = re.compile(r'^[.\\/][\\/]*') # ./
        self.__pattern['begin_ddot'] = re.compile(r'^[A-Z]:') # [A-z]:

        for k in patterns:
            self.__pattern[k] = re.compile(patterns[k])
        
        self.local_path = self.get_local_path()
    
    def get_local_path(self):
        '''
        获取当前文件夹完整路径
        '''
        return os.getcwd()

    def join_path(self, *paths):
        '''
        拼接路径
        '''
        f_p = ''
        for p in paths:
            p = re.split(self.__pattern['depart'], p)
            if re.match(self.__pattern['begin_ddot'], p[0]):
                p[0] = p[0] + '\\' # windows匹配
            for each in p:
                f_p = os.path.join(f_p, each)
        return f_p

    def is_relative_path(self, path):
        return re.match(self.__pattern['begin'], path)

    def modefy_join_path(self, base, path):
        '''
        去除开头的.并拼接，主要为后面两个函数调用
        '''
        f_p = base
        for p in path:
            try:
                pb = re.match(self.__pattern['begin'], p).group()
                p = p.replace(pb, '', 1)
            except AttributeError:
                pass
                # print('The input path \"' + p + '\" dont include root path')
            p = re.split(self.__pattern['depart'], p)
            for each in p:
                f_p = os.path.join(f_p, each)
        return f_p

    def get_full_path(self, *path):
        '''
        拼接完成完整路径
        '''
        return self.modefy_join_path(self.local_path, path)

    def get_relative_path(self, *path):
        '''
        拼接完成相对路径
        '''
        return self.modefy_join_path('.', path)

    def load_file(self, folder, type='pdf'):
        '''
        监测文件夹，并获取所有子文件夹和文件
        '''
        fl = []
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            logging.error("No such folder")
            return None

        for f in files:
            f_full = self.get_full_path(folder, f)

            if(os.path.isfile(f_full)):
                # 添加文件
                portion = os.path.splitext(f)
                if portion[1] == '.' + type:
                    fl.append(f)
                else:
                    logging.info('The file \"' + f +
                                  '\" is not a ' + type + ' document')
        return fl

    def retrieve_file(self, folder, filename, type='txt'):
        '''
        监测输出文件夹是否准备妥当
        '''
        portion = os.path.splitext(filename)
        full_filename = portion[0] + '.' + type

        if not os.path.exists(folder):
            os.mkdir(folder)
            return full_filename

        o_f_p = self.get_full_path(folder, full_filename)
        if os.path.exists(o_f_p):
            while True:
                logging.info('The file \"' + full_filename + '\" in folder \"' +
                             folder + '\" already exists. Continue conversion/parsing will overwrite the original file. Continue?[Y/N]')
                toGo = input()
                if toGo.lower() == 'y':
                    os.remove(o_f_p)
                    return full_filename
                elif toGo.lower() == 'n':
                    return False
                else:
                    logging.error('[InputError]: Invalid input, try Y or N')
        else:
            return full_filename

def save_txt(full_filename, content):
    '''保存正文内容到文件
    '''
    with open(full_filename, 'a', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    # pass
    mp = ModefyPath()
    print("1:", mp.get_relative_path('.\\bbbb//cc//cc', 'ccccc.txt'))
    print("2:", mp.load_file('.\\articles\\pdf'))
    print("2.1:", mp.load_file(r'F:\PerStudy\NLTK\parseEEDoc\utils\articles\pdf'))
    print("3:", mp.retrieve_file('articles', '2', 'docx'))
    print("4:", mp.join_path('./articles', '2'))
    # test = re.compile('[ ]+$')
    # replace_es = re.search(test, 'sdf12  ').group()
    # print(re.sub(replace_es, '1', 'sdf12  '))
