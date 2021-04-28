import os
from os import path
import time
file1 = input('file1 path?')
file2 = input('file2 path?')
os.system(f'ffmpeg -i {file1} -pix_fmt yuv420p 1.mp4')
time.sleep(5)
os.system(f'ffmpeg -i {file2} -pix_fmt yuv444p 2.mp4')
time.sleep(5)
if path.exists('a.txt') == False:
    with open('a.txt', 'w') as f:
        f.write("file \'1.mp4\'\n")
        f.write("file \'2.mp4\'\n")
os.system('ffmpeg -f concat -safe 0 -auto_convert 1 -i a.txt -c copy out.mp4')
time.sleep(5)
os.remove('1.mp4')
os.remove('2.mp4')