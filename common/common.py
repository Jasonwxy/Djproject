#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os


def read_file_list(dir_path):
    file_list = []
    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        for file in files:
            if file != '__init__.py' and not file.endswith('log') and not file.endswith('pyc'):
                file_list.append(file)
    return file_list


def read_file_lists(dir_path):
    file_walk = os.walk(dir_path)
    for a, b, c in file_walk:
        print(a, b, c)


read_file_lists('E:\\working\\wutaishan45\\cases')
