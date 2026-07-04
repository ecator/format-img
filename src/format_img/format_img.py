"""
格式化图片名称
"""
import sys
import getopt
import exifread
import time
import os
from .my_utility import get_imgs, get_suffixes, get_format, get_file_suffix

HELP = """
format-img
            [-f format]   default is '%Y%m%d%H%M%S'
            [-s suffixs]  default is 'jpg,png,jpeg,heic'
            -h            help
"""


def main():
    """主入口函数"""
    fmt = ''
    suffixes = []
    try:
        options, args = getopt.getopt(sys.argv[1:], 'hs:f:')
        for option, value in options:
            if option == '-f':
                fmt = value
            elif option == '-s':
                suffixes = value.split(',')
            elif option == '-h':
                print(HELP)
                sys.exit(0)
    except Exception as e:
        sys.stderr.write(f"Error parsing options: {e}\n")
        sys.exit(1)

    if not fmt:
        fmt = get_format()
    if not suffixes:
        suffixes = get_suffixes()

    ok_cnt = 0
    ng_cnt = 0
    
    for img in get_imgs(suffixes):
        # 遍历出图片的EXIF时间或者文件创建时间并且按照格式重新命名文件
        try:
            with open(img, 'rb') as f_img:
                tags = exifread.process_file(f_img, stop_tag='EXIF DateTimeOriginal')
        except Exception as e:
            sys.stderr.write(f"Failed to read EXIF from {img}: {e}\n")
            ng_cnt += 1
            continue

        if 'EXIF DateTimeOriginal' in tags:
            try:
                img_time = time.strptime(str(tags['EXIF DateTimeOriginal']), "%Y:%m:%d %H:%M:%S")
            except ValueError:
                img_time = time.localtime(os.path.getmtime(img))
        else:
            img_time = time.localtime(os.path.getmtime(img))

        # 重命名文件
        i = 0
        img_suffix = get_file_suffix(img)
        img_new_name = time.strftime(fmt, img_time) + "." + img_suffix
        while os.path.exists(img_new_name):
            i += 1
            img_new_name = time.strftime(fmt, img_time) + "_" + str(i) + "." + img_suffix
        try:
            os.rename(img, img_new_name)
            print("%-25s\t→\t%-25s\tsuccess" % (img, img_new_name))
            ok_cnt += 1
        except Exception as e:
            print("%-25s\t→\t%-25s\tfailed" % (img, img_new_name))
            sys.stderr.write(f"Error: {e}\n")
            ng_cnt += 1

    # 输出统计信息
    print("\nProcess completed\nSuccess: %d\nFailed: %d" % (ok_cnt, ng_cnt))


if __name__ == '__main__':
    main()
