import speech_recognition as sr
from emoji import emojize

def speech_to_text():
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print("\n {} Diga alguma coisa: ".format(emojize(":boca:",language = 'pt')))
        audio = microfone.listen(source)
        try:
            frase = microfone.recognize_google(audio,language='pt-BR')
            print("{} Você disse: {}".format(emojize(":polegar_para_cima:",language = 'pt'),frase))
            return frase
        except:
            return print("{} Não entendi, pode repetir ?! ...".format(emojize(":rosto_pensativo:",language = 'pt')))
        
condition = True
while condition == True:
    frase = speech_to_text()
    if (frase != None) and (frase.lower() == 'pare agora'):
        print('\n {} \t Parando ...'.format(emojize(":polegar_para_baixo:",language = 'pt')))
        condition = False

## isntabot

# from instabot import Bot

# bot = Bot()
# bot.login(username = "studentoutlier",
#           password = "timeoutlier20")

# bot.upload_photo("st.jpg",
#                 caption = "testando postagem")

## youtube_dl

# from __future__ import unicode_literals
# import youtube_dl
# import os


# class Download: 
#     def __init__(self, url):
#         self.url = url 
#         self.save_path = os.path.join (os.path.expanduser('~'), 'Downloads')
#         self.song() 
#     def song(self):
#         opts = {
#             'verbose': True,
#             'fixup': 'detect_or_warn',
#             'format': 'bestaudio/best',
#             'postprocessors': [{
#                 'key': 'FFmpegExtractAudio',
#                 'preferredcodec': 'mp3',
#                 'preferredquality': '1411',
#             }],
#             'extractaudio' : True, 
#             'outtmpl': self.save_path + '/%(title)s.X(ext)s', 
#             'noplaylist' : True 
#         }
#         with youtube_dl.YoutubeDL(opts) as ydl:
#             ydl.download([self.url])

# if __name__ == '__main__':
#     URL = input("Enter url to song here\n >> ")
#     Download(url = URL)
    
####################
# import speech_recognition as sr

# r = sr.Recognizer()

# with sr.Microphone() as source:
#     print("SPEAK ...")
#     audio = r.listen(source)

# print(r.recognize_google(audio, language= 'pt-BR'))


############################


# from gtts import gTTS 
# import os 
# import warnings
# from emoji import emojize

# condition = True
# while condition:
#     def speak(text):   
#         name = ".speak.mp3"
#         gtts = gTTS(text=text, lang='pt', slow=False) 
#         gtts.save(name)
#         os.system('cvlc {} --play-and-exit'.format(name))

#     if __name__ == '__main__':
#         text = input("\n {} Oque eu digo ? ".format(emojize(":rosto_pensativo:",language = 'pt')))
#         speak(text)
#         answer = str(input("\n {} Denovo ? ".format(emojize(":rosto_pensativo:",language = 'pt'))))
#         while (answer.lower() != 'nao') and (answer.lower() != 'sim'):
#             emoji = emojize(":aviso:",language = 'pt')
#             warnings.warn(f'{emoji} resposta nao identificada, tente denovo.  {emoji}')
#             answer = str(input("\n {} Denovo ? ".format(emojize(":rosto_pensativo:",language = 'pt'))))
#         if (answer.lower() != 'sim') and (answer.lower() == 'nao'):
#             condition = False

############################
