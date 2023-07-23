# tool009_elipythontools

## 001a-批量转换png为jpg格式

这是一个基于 Python 的批量转换图片格式程序，它可以将指定文件夹中的所有png图片转换为jpg，并保存到指定的输出目录。

### 功能特性

* 支持将指定文件夹中的所有图片进行批量格式转换。
* 可以设置转换后的图片格式。
* 输出目录可以自定义，如果未指定，则默认为输入文件夹的父目录。

### 安装依赖

在运行该程序之前，请先确保你已经安装了 Python 3 和以下依赖：

`pillow`

* 你可以使用以下命令安装依赖：
`pip install pillow`

* 如果使用的 Linux 发行版是 Arch Linux，可以使用以下命令安装：
`pacman -S python-pillow`

### 使用方法

使用以下命令从命令行运行程序：

* 处理单张图片：`python 001-image_png2jpg.py /path/from/file /path/to/file`
* 处理文件夹下的所有图片：`python 001a-image_png2jpg_batch.py /path/from/folder /path/to/folder`

⚠️ 注意：`001a-image_png2jpg_batch.py` 依赖于名为 `001-image_png2jpg.py` 的 Python 脚本来实际执行图片格式转换操作，请确保它们处于同一文件夹下。

## 002a-批量压缩图片程序

这是一个基于 Python 的批量压缩图片程序，它可以自动将指定文件夹中的所有图片文件进行压缩，并保存到指定的输出目录。

### 功能特性

- 支持将指定文件夹中的所有图片进行批量压缩。
- 可以设置压缩后的最大尺寸和图片质量参数。
- 输出目录可以自定义，如果未指定，则默认为输入文件夹的父目录。

### 安装依赖

在运行该程序之前，请先确保你已经安装了 Python 3 和以下依赖：

`pillow`

* 你可以使用以下命令安装依赖：
`pip install pillow`

* 如果使用的linux发行版是ArchLinux，使用以下命令安装：
`pacman -S python-pillow`

### 使用方法

使用以下命令从命令行运行程序：

* 处理单张图片：`python 002-image_compress.py -i /path/from/file -o /path/to/file -s 1024 -q 80`
* 处理文件夹下的所有图片：`python 002a-image_compress_batch.py /path/from/folder /path/to/folder -s 1024 -q 80`

其中：

- `-s` 或 `--size` 参数用于设置压缩后的最大尺寸（默认为 1024）。
- `-q` 或 `--quality` 参数用于设置图片质量（默认为 30）。

如果未指定 `-s` 和 `-q` 参数，程序将使用默认值进行压缩。

⚠️ 注意：`002a-image_compress_batch.py`依赖于名为 `002-image_compress.py` 的 Python 脚本来实际执行图片压缩操作，请确保它们处于同一文件夹下。

⚠️ 注意：png格式的图片不支持压缩图片质量，只支持缩小图片尺寸，如果想获得更小的图片存储大小，可以先将png图片转换为jpg格式，再进行压缩处理。

⚠️ 补充说明：以上提供的代码和 README 文件是由 GPT-3.5 模型生成的。请注意，生成的代码和文本是模型基于先前训练的数据和模式生成的，并不保证完全正确或符合实际需求。因此，在使用生成的代码和文本时，请仔细检查和验证，并根据需要进行适当的修改和调整，以确保其适应你的具体情况。
