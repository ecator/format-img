# 图片名称格式化工具
## 根据EXIF信息来格式化图片到名字，方便管理

# 环境
python3

运行下面命令安装依赖包：
```
pip install -r requirement.txt
```

# 用法

## format-img.py

### 基本用法

```
format-img.py
            [-f format]   default read from config.ini
            [-s suffixs]  default read from config.ini
            -h            help
```

* `-s` 要格式化文件名的的后缀名，需要用引号括起来，比如`-s 'jpg,png'`，不区分大小写
* `-f` 文件名的格式，支持的占位符如下：

格式	| 含义
--- | ---
%a |	本地（locale）简化星期名称 	 
%A |	本地完整星期名称	 
%b |	本地简化月份名称  
%B |	本地完整月份名称 	 
%c |	本地相应的日期和时间表示 	 
%d |	一个月中的第几天（01 - 31） 	 
%H |	一天中的第几个小时（24小时制，00 - 23） 	 
%I |	第几个小时（12小时制，01 - 12） 	 
%j |	一年中的第几天（001 - 366） 	 
%m |	月份（01 - 12） 	 
%M |	分钟数（00 - 59） 	 
%p |	本地am或者pm的相应符 
%S |	秒（01 - 61） 
%U |	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 
%w |	一个星期中的第几天（0 - 6，0是星期天）
%W |	和%U基本相同，不同的是%W以星期一为一个星期的开始。 	 
%x |	本地相应日期 	 
%X |	本地相应时间 	 
%y |	去掉世纪的年份（00 - 99） 	 
%Y |	完整的年份 
%Z |	时区的名字（如果不存在为空字符）
%% |	‘%’字符

* `-h` 获取帮助

### 例

把当前目录下的`jpg`和`png`文件的名称格式化成`2017-10-01 10:17:01`的形式
```
./format-img.py -s "jpg,png" -f "%Y-%m-%d %H:%M:%S"
```

### 其他

如果不带参数运行脚本则读取`./config.ini`中`default`节中的配置。

建议以alias方式运行本脚本，比如在`~/.bash_profile`文件中加入`alias format-img='format-img.py全路径'`，这样就可以在任意一个文件夹运行脚本了。

文件查找只查找当前目录，无法查找子目录。


## modify-exif.py

用于修正EXIF信息。

### 基本用法

```
modify-exif.py
              -f file -r property [-s]         read property, only output value if s is set
              -f file -rt [-s]                 read datetime_original and datetime_digitized, only output value if s is set
              -f file -w property -v value     write property
              -f file -wt -v value             write datetime_original and datetime_digitized
              -h                               help
```

具体示例可以参考`update-datetime.ps1`，可以修改目标文件夹里面的`yyyyMMddHHmmss`这样命名规则的图片EXIF时间信息。

