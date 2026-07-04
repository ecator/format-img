"""
编辑图片的EXIF信息
"""
import sys
import getopt
from .my_utility import get_file_exif, set_file_exif

HELP = """
modify-exif 
              -f file -r property [-s]         read property, only output value if s is set
              -f file -rt [-s]                 read datetime_original and datetime_digitized, only output value if s is set
              -f file -w property -v value     write property
              -f file -wt -v value             write datetime_original and datetime_digitized
              -h                               help
"""


def read_property(filename, property_name, simple_out=False):
    """读取属性并打印详情"""
    value = get_file_exif(filename, property_name)
    if simple_out:
        if value != "":
            print(value)
    else:
        print(f"read {property_name} from {filename}")
        print(f"value is {value}")


def write_property(filename, property_name, value):
    """写入属性并打印详情"""
    print(f"write '{property_name}={value}' to {filename}")
    set_file_exif(filename, property_name, value)


def main():
    """主入口函数"""
    process_file = ""
    process_mode = ""
    process_property = ""
    process_value = ""
    simple_out = False

    try:
        options, args = getopt.getopt(sys.argv[1:], 'hf:r:w::v:s')
        for option, value in options:
            if option == '-f':
                process_file = value
            elif option == '-r':
                process_mode = "r"
                process_property = value
            elif option == '-w':
                process_mode = "w"
                process_property = value
            elif option == '-v':
                process_value = value
            elif option == '-s':
                simple_out = True
            elif option == '-h':
                print(HELP)
                sys.exit(0)

        if process_file == "":
            raise Exception("file is empty")
        if process_mode == "":
            raise Exception("r or w flag is necessary")
        if process_property == "":
            raise Exception("property is necessary")
        if process_mode == "w" and process_value == "":
            raise Exception("value is necessary")
    except Exception as e:
        sys.stderr.write("".join(e.args) + "\n")
        sys.exit(1)

    try:
        if process_mode == 'r':
            if process_property == "t":
                read_property(process_file, "datetime_original", simple_out)
                read_property(process_file, "datetime_digitized", simple_out)
            else:
                read_property(process_file, process_property, simple_out)
        else:
            if process_property == "t":
                write_property(process_file, "datetime_original", process_value)
                write_property(process_file, "datetime_digitized", process_value)
            else:
                write_property(process_file, process_property, process_value)
    except Exception as e:
        sys.stderr.write("".join(e.args) + "\n")
        sys.exit(1)


if __name__ == '__main__':
    main()
