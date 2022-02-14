# %%

import os
import time

from datetime import datetime
from subprocess import Popen


# %%01'
video_file_path = r'D:\video_test\video1.mp4'
pipe = r'\\.\pipe\\videopipe0'
print(pipe)
print(video_file_path)

# %%
ffmpeg_processes = []
ffmpeg_processes.append(Popen(r'ffmpeg -y -f rawvideo -vcodec rawvideo -s 500x500 -pix_fmt gray -r 60 -i {} -c:v h264_nvenc -profile:v high -preset slow -an {}'.format(pipe, video_file_path),shell=True))

# %%
time.sleep(10)

# # %%
# pipe2 = r'\\.\pipe\videopipe1'
# video_file_path2 = r'D:\video_test\video2.mp4'
# print(pipe2)
# print(video_file_path2)

# # %%

# ffmpeg_processes.append(Popen(r'ffmpeg -y -f rawvideo -vcodec rawvideo -s 1024x1024 pix_fmt bgr8 -r 60 -i {} -c:v h264_nvenc -profile:v high -preset slow -an {}'.format(pipe2, video_file_path2)))

# # %%

# #print(r'ffmpeg -y -f rawvideo -vcodec rawvideo -s 1024x1024 -pix_fmt bgr8 -r 60 -i {} -c:v h264_nvenc -profile:v high -preset slow -an {}'.format(pipe, video_file_path))

# # %%




# %%
