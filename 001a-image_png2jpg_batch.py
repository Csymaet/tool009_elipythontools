#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import argparse
import subprocess

def create_directory(directory):
    # 检查目录是否存在
    if not os.path.exists(directory):
        # 创建目录
        os.makedirs(directory)

def convert_images(input_folder, output_folder):
    # 获取文件夹下所有文件
    files = os.listdir(input_folder)

    # 遍历文件夹中的文件
    for file in files:
        # 获取文件的完整路径
        input_file_path = os.path.join(input_folder, file)
        
        # 检查文件是否为 PNG 格式
        if file.endswith(".png"):
            # 构建输出文件的路径
            output_file_path = os.path.join(output_folder, file[:-4] + ".jpg")
            
            # 构建命令行命令
            command = f"python 001-image_png2jpg.py {input_file_path} {output_file_path}"
            
            # 执行命令行命令
            subprocess.call(command, shell=True)
            print(f"转换完成：{file}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='批量转换文件夹下的 PNG 图像为 JPG 格式')
    parser.add_argument('input_folder', help='输入文件夹路径')
    parser.add_argument('output_folder', help='输出文件夹路径')

    args = parser.parse_args()

    input_folder = args.input_folder
    output_folder = args.output_folder

    # 创建输出目录（如果不存在）
    create_directory(output_folder)

    # 调用函数进行批量转换
    convert_images(input_folder, output_folder)
