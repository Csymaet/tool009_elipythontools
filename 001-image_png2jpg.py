#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from PIL import Image

def convert_png_to_jpg(png_path, jpg_path):
    try:
        image = Image.open(png_path)
        rgb_image = image.convert('RGB')
        rgb_image.save(jpg_path)
        print("转换完成！")
    except Exception as e:
        print("转换失败:", str(e))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='PNG to JPG Converter')
    parser.add_argument('input', help='输入PNG文件路径')
    parser.add_argument('output', help='输出JPG文件路径')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output

    convert_png_to_jpg(input_file, output_file)
