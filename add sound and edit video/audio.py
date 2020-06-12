from moviepy.editor import *
from moviepy.audio.fx.volumex import volumex

videoclip = VideoFileClip('output.avi')
audioclip = AudioFileClip('Our-Mountain_v003_Looping.mp3')
videoclip.audio = audioclip.subclip(0,20.8).fx(volumex, 0.05)

videoclip.write_videofile("Finished.mp4")
