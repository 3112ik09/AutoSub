from moviepy.editor import *

mp4_file = r'/home/ishu/Desktop/AutoSub/vid.mp4'
mp3_file = r'/home/ishu/Desktop/AutoSub/vid.mp3'


videoclip = VideoFileClip(mp4_file)

audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)

audioclip.close()
videoclip.close()
