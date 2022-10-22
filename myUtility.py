#!/usr/bin/env python3
# -*-coding:utf-8-*-
# 自定义工具集
from datetime import date, datetime
import os
import re
import configparser
from exif import Image, DATETIME_STR_FORMAT

CWD = os.path.abspath(os.path.dirname(__file__))


def getImgs(suffixs=['jpg']):
    '获取指定后缀到图片文件名'
    # 构造匹配表达式
    img_pattern = '$|.*\.'.join(suffixs)
    if img_pattern != "":
        img_pattern += '$'
        img_pattern = '.*\.'+img_pattern
    dirs = os.listdir('.')
    imgs = []
    for img in dirs:
        if re.match(img_pattern, img, re.I):
            imgs.append(img)
    return imgs


def getSuffixs():
    '获取默认到文件后缀'
    config = configparser.RawConfigParser()
    config.read(CWD+'/config.ini')
    return config.get('default', 'suffixs').split(',')

def getFormat():
    '获取默认到命名格式'
    config = configparser.RawConfigParser()
    config.read(CWD+'/config.ini')
    return config.get('default', 'format')


def getFileSuffix(filename=''):
    '获取文件后缀'
    if filename != '':
        tmp = filename.split('.')
        if len(tmp) > 0:
            return tmp.pop()


def getFileExif(filename='', property=''):
    '获取指定文件的EXIF信息，默认获取所有信息'
    image = Image(filename)
    if not image.has_exif:
        return ""
    if property == "":
        return image.list_all()
    else:
        return image.get(property, "")


def setFileExif(filename='', property='datetime_original', value=''):
    '设定指定文件的EXIF信息，默认设置datetime_original为当前时间'
    image = Image(filename)
    if value == '':
        value = datetime.now().strftime(DATETIME_STR_FORMAT)
    image.set(property, value)
    with open(filename,'wb') as f:
        f.write(image.get_file())


if __name__ == '__main__':
    '模块测试'
    # print(getFileSuffix('file.suffix'))
    # print(getImgs())