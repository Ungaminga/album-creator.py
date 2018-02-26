# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:17:50 2018

@author: loljkpro
"""

from moviepy.editor import *
import sys, os
import natsort
from mp3_tagger import MP3File

def edit_timing_output(number, name):
    if current_time//3600 > 1:
        print(str(number)+". "+name+" - "+current_time//3600)
    else:
        print(str(number)+". "+name+" - "+"%02d"%(current_time//60)+":%02d"%(current_time%60))

def get_name_for_track(file):
    return MP3File(dir+os.sep+file).get_tags()['ID3TagV1']['song'] or file

dir = os.getcwd()
if len(sys.argv) > 1:
    dir = sys.argv[1]

ld = natsort.natsorted(os.listdir(dir))

album = ''
tracks = []

output = ''
current_time = 0
number = 1

for file in ld:
    if file[0:5] == 'album':
        album = dir+os.sep+file
    else:
        l = len(file)
        if file[l-3:l] == 'mp3':
            f = dir+os.sep+file
            a = AudioFileClip(f)
            tracks.append(a)
            edit_timing_output(number, get_name_for_track(file))
            number = number+1
            current_time+=a.duration//1

output = 'output.mp4'
if len(sys.argv) > 2:
    output = sys.argv[2]

aa = concatenate_audioclips(tracks)
im = ImageClip(album, duration=aa.duration)
im.audio = aa
im.write_videofile(output, fps=24)

del tracks[:]
del aa