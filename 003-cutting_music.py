#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 批量修改当前文件夹下的mp3文件，只截取前224秒

import os
from pydub import AudioSegment

# 获取当前文件夹下的所有mp3文件
folder_path = './'
mp3_files = [file for file in os.listdir(folder_path) if file.endswith('.mp3')]

# 遍历每个mp3文件
for mp3_file in mp3_files:
    # 加载音频文件
    audio = AudioSegment.from_file(os.path.join(folder_path, mp3_file), format='mp3')

    # 截取前2分24秒
    time = 144 * 1000  # 毫秒数
    trimmed_audio = audio[:time]

    # 导出文件
    output_file = mp3_file.replace('.mp3', '_224.mp3')
    trimmed_audio.export(os.path.join(folder_path, output_file), format='mp3')

