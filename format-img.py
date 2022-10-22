#!/usr/bin/env python3
# -*-coding:utf-8-*-

# 格式化图片名称

from myUtility import *
import sys
import getopt
import exifread
import time


HELP = """
format-img.py
            [-f format]   default read from config.ini
            [-s suffixs]  default read from config.ini
            -h
"""


def main():
    '主函数'
    ok_cnt = 0
    ng_cnt = 0
    for img in getImgs(Suffixs):
        '遍历出图片的EXIF时间或者文件创建时间并且按照格式重新命名文件'
        f_img = open(img, 'rb')
        tags = exifread.process_file(f_img, stop_tag='EXIF DateTimeOriginal')
        f_img.close()
        # print tags
        if 'EXIF DateTimeOriginal' in tags.keys():
            img_time = time.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
        else:
            img_time = time.localtime(os.path.getmtime(img))
        # print("%s：%s"%(img,time.strftime("%Y-%m-%d %H:%M:%S",img_time)))
        # 重命名文件
        i = 0
        img_new_name = time.strftime(Format, img_time)+"."+getFileSuffix(img)
        while os.path.exists(img_new_name):
            i += 1
            img_new_name = time.strftime(Format, img_time)+"_"+str(i)+"."+getFileSuffix(img)
        try:
            os.rename(img, img_new_name)
            print("%-25s\t→\t%-25s\tsuccess" % (img, img_new_name))
            ok_cnt += 1
        except Exception as e:
            print("%-25s\t→\t%-25s\tfailed" % (img, img_new_name))
            raise e
            ng_cnt += 1
    # 输出统计信息
    print("\nProcess completed\nSuccess：%d\nFailed：%d" % (ok_cnt, ng_cnt))

if __name__ == '__main__':
    # 解析参数
    Format = ''
    Suffixs = []
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hs:f:')
        for option, value in options:
            if option == '-f':
                Format = value
            elif option == '-s':
                Suffixs = value.split(',')
            elif option == '-h':
                print(HELP)
                exit()
    except Exception as e:
        raise e
    finally:
        if Format == '':
            Format = getFormat()
        if Suffixs == []:
            Suffixs = getSuffixs()
    main()
