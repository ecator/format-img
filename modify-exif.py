#!/usr/bin/env python3
# -*-coding:utf-8-*-

# 编辑图片的EXIF信息

from myUtility import *
import sys
import getopt


HELP = """
modify-exif.py 
              -f file -r property [-s]         read property, only output value if s is set
              -f file -rt [-s]                 read datetime_original and datetime_digitized, only output value if s is set
              -f file -w property -v value     write property
              -f file -wt -v value             write datetime_original and datetime_digitized
              -h                               help
"""


processFile = ""
processMode = ""
processProperty = ""
processValue = ""
simpleOut = False


def readProperty():
    '读取属性并打印详情'
    value=getFileExif(processFile,processProperty)
    if simpleOut:
        if value != "":
            print(value)
    else:
        print(f"read {processProperty} from {processFile}")
        print(f"value is {value}")


def writeProperty():
    '写入属性并打印详情'
    print(f"write '{processProperty}={processValue}' to {processFile}")
    setFileExif(processFile, processProperty, processValue)


def main():
    '主函数'
    global processProperty
    try:
        if processMode == 'r':
            if processProperty == "t":
                processProperty = "datetime_original"
                readProperty()
                processProperty = "datetime_digitized"
                readProperty()

            else:
                readProperty()
        else:
            if processProperty == "t":
                processProperty = "datetime_original"
                writeProperty()
                processProperty = "datetime_digitized"
                writeProperty()
            else:
                writeProperty()
    except Exception as e:
        sys.stderr.write("".join(e.args))
        exit(1)


if __name__ == '__main__':
    # 解析参数

    try:
        options, args = getopt.getopt(sys.argv[1:], 'hf:r:w::v:s')
        for option, value in options:
            if option == '-f':
                processFile = value
            elif option == '-r':
                processMode = "r"
                processProperty = value
            elif option == '-w':
                processMode = "w"
                processProperty = value
            elif option == '-v':
                processValue = value
            elif option =='-s':
                simpleOut = True
            elif option == '-h':
                print(HELP)
                exit()
        if processFile == "":
            raise Exception("file is empty")
        if processMode == "":
            raise Exception("r or w flag is necessary")
        if processProperty == "":
            raise Exception("property is necessary")
        if processMode == "w" and processValue == "":
            raise Exception("value is necessary")
    except Exception as e:
        sys.stderr.write("".join(e.args))
        exit(1)
    main()