# 图片名称格式化工具
## 根据 EXIF 信息来格式化图片名字，方便管理

## 环境与安装

本工具使用 `uv` 管理依赖和运行环境。

### 安装依赖并同步环境：
```bash
uv sync
```

---

## 用法

### 1. format-img

格式化当前目录下的图片文件名。

#### 基本用法
```bash
uv run format-img [-f format] [-s suffixs] [-h]
```

- `-f` 文件名的格式，默认值为 `%Y%m%d%H%M%S`。支持的占位符列表见下表。
- `-s` 要格式化文件名的后缀名列表（以逗号分隔，不区分大小写），默认值为 `jpg,png,jpeg,heic`。例如 `-s "jpg,png"`。
- `-h` 获取帮助信息。

#### 支持的格式占位符：

| 格式 | 含义 |
|---|---|
| %a | 本地（locale）简化星期名称 |
| %A | 本地完整星期名称 |
| %b | 本地简化月份名称 |
| %B | 本地完整月份名称 |
| %c | 本地相应的日期和时间表示 |
| %d | 一个月中的第几天（01 - 31） |
| %H | 一天中的第几个小时（24小时制，00 - 23） |
| %I | 第几个小时（12小时制，01 - 12） |
| %j | 一年中的第几天（001 - 366） |
| %m | 月份（01 - 12） |
| %M | 分钟数（00 - 59） |
| %p | 本地am或者pm的相应符 |
| %S | 秒（01 - 61） |
| %U | 一年中的星期数（00 - 53，星期天为一个星期的开始） |
| %w | 一个星期中的第几天（0 - 6，0是星期天） |
| %W | 和 %U 基本相同，不同的是以星期一为一个星期的开始 |
| %x | 本地相应日期 |
| %X | 本地相应时间 |
| %y | 去掉世纪的年份（00 - 99） |
| %Y | 完整的年份 |
| %Z | 时区的名字 |
| %% | '%' 字符 |

#### 示例
把当前目录下的 `jpg` 和 `png` 文件的名称格式化成 `2017-10-01 10:17:01` 的形式：
```bash
uv run format-img -s "jpg,png" -f "%Y-%m-%d %H:%M:%S"
```

---

### 2. modify-exif

用于读取/修改图片的 EXIF 信息。

#### 基本用法
```bash
# 读取属性详情
uv run modify-exif -f file -r property [-s]

# 读取拍摄时间与数字化时间（only output value if -s is set）
uv run modify-exif -f file -rt [-s]

# 写入指定属性
uv run modify-exif -f file -w property -v value

# 写入拍摄时间与数字化时间
uv run modify-exif -f file -wt -v value

# 查看帮助
uv run modify-exif -h
```

具体示例可以参考 `scripts/update-datetime.ps1`，用于批量修改目标文件夹里面 `yyyyMMddHHmmss` 这样命名规则图片的 EXIF 时间信息。

## 注意事项

**跨路径调用**：如果要在其他路径（即不是项目根目录）下调用本工具，建议使用 `--project` 参数指定项目路径，例如：

```powershell
uv --project D:\Development\format-img run format-img
```

使用 `--project` 可以确保 `uv` 能够找到该项目的环境与依赖，同时**不会**改变当前的工作路径（cwd），从而正确地对你当前所在的命令行路径下的图片进行格式化操作。

