#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import subprocess

def compress_folder_images(folder_path, output_folder, max_size, quality):
    # 获取文件夹中所有图片文件的路径
    image_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(('.jpg', '.jpeg', '.png'))]

    # 获取脚本所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建完整路径
    script_path = os.path.join(script_dir, "002-image_compress.py")

    # 遍历每个图片文件并调用 002-image_compress.py 进行压缩
    for image_file in image_files:
        output_file = os.path.join(output_folder, os.path.basename(image_file))
        # 调用 002-image_compress.py 并传递命令行参数
        command = f"python {script_path} -i {image_file} -o {output_file} -s {max_size} -q {quality}"
        subprocess.call(command, shell=True)

# 解析命令行参数
parser = argparse.ArgumentParser(description='批量压缩图片程序')
parser.add_argument('input', type=str, help='要处理的文件夹路径')
parser.add_argument('output', type=str, help='要保存压缩图片的目录')
parser.add_argument('-s', '--size', type=int, default=1024, help='压缩后的最大尺寸')
parser.add_argument('-q', '--quality', type=int, default=30, help='图片质量 (0-100)')
args = parser.parse_args()

# 检查输出目录是否存在，如果不存在则创建
if not os.path.exists(args.output):
    os.makedirs(args.output)

compress_folder_images(args.input, args.output, args.size, args.quality)
