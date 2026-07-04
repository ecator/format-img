"""
自定义工具集
"""
from datetime import datetime
import os
import re
from exif import Image, DATETIME_STR_FORMAT


def get_imgs(suffixs=None):
    """获取指定后缀的图片文件名"""
    if suffixs is None:
        suffixs = get_suffixes()
    
    # 构造匹配表达式
    img_pattern = '$|.*\\.'.join(suffixs)
    if img_pattern != "":
        img_pattern += '$'
        img_pattern = '.*\\.' + img_pattern
    
    try:
        dirs = os.listdir('.')
    except Exception:
        dirs = []
        
    imgs = []
    for img in dirs:
        if re.match(img_pattern, img, re.I):
            imgs.append(img)
    return imgs


def get_suffixes():
    """获取默认的文件后缀"""
    return ['jpg', 'png', 'jpeg', 'heic']


def get_format():
    """获取默认的命名格式"""
    return '%Y%m%d%H%M%S'


def get_file_suffix(filename=''):
    """获取文件后缀"""
    if filename != '':
        tmp = filename.split('.')
        if len(tmp) > 0:
            return tmp.pop()
    return ''


def get_file_exif(filename='', property=''):
    """获取指定文件的EXIF信息，默认获取所有信息"""
    image = Image(filename)
    if not image.has_exif:
        return ""
    if property == "":
        return image.list_all()
    else:
        return image.get(property, "")


def set_file_exif(filename='', property='datetime_original', value=''):
    """设定指定文件的EXIF信息，默认设置datetime_original为当前时间"""
    image = Image(filename)
    if value == '':
        value = datetime.now().strftime(DATETIME_STR_FORMAT)
    image.set(property, value)
    with open(filename, 'wb') as f:
        f.write(image.get_file())


if __name__ == '__main__':
    # 模块测试
    pass
