#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


def read_file_list(dir_path):
    file_list = []
    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        for file in files:
            if file != '__init__.py' and not file.endswith('log') and not file.endswith('pyc'):
                file_dict = {"name": file}
                file_path = os.path.join(dir_path, file)
                if os.path.isdir(file_path):
                    file_dict["sub_node"] = read_file_list(file_path)
                # else:
                #     file_dict["sub_node"] = []
                file_list.append(file_dict)
    return file_list


# print(read_file_list('E:\\working\\wutaishan45\\cases'))
config = os.path.join(os.path.abspath('.').split('\\Djproject')[0], 'abc\\ba\\d')
print(config)
