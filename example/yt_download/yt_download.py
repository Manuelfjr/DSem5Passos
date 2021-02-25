from __future__ import unicode_literals
import youtube_dl
import os
from emoji import emojize

class Download: 
    def __init__(self, url):
        self.url = url
        self.save_path = os.path.join (os.path.expanduser('~'), 'Downloads')
        self.song() 
    def song(self):
        opts = {
            'verbose': True,
            'fixup': 'detect_or_warn',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '1411',
            }],
            'extractaudio' : True, 
            'outtmpl': self.save_path + '/%(title)s.X(ext)s', 
            'noplaylist' : True 
        }
        with youtube_dl.YoutubeDL(opts) as ydl:
            ydl.download([self.url])

if __name__ == '__main__':
    emj1 = emojize(':musical_note:', language='en')
    URL = input(f"\n{emj1} Enter url to song here\n >> ")
    Download(url = URL)