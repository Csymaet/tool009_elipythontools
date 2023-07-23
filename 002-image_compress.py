#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from PIL import Image

def compress_image(input_path, output_path, max_size, quality):
    image = Image.open(input_path)  # 打开图片
    width, height = image.size

    # 检查图像尺寸是否小于 max_size
    if width <= max_size and height <= max_size:
        image.thumbnail((width, height))  # 缩放图片到指定尺寸
    else:
        image.thumbnail((max_size, max_size))  # 缩放图片到指定尺寸
    image.save(output_path, optimize=True, quality=quality)  # 保存压缩后的图片

# 解析命令行参数
parser = argparse.ArgumentParser(description='图片压缩程序')
parser.add_argument('-i', '--input', type=str, help='输入图片路径')
parser.add_argument('-o', '--output', type=str, help='输出图片路径')
parser.add_argument('-s', '--size', type=int, default=1024, help='压缩后的最大尺寸')
parser.add_argument('-q', '--quality', type=int, default=30, help='图片质量')
args = parser.parse_args()

compress_image(args.input, args.output, args.size, args.quality)
