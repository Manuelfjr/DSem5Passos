from gtts import gTTS 
import os 
import warnings
from emoji import emojize

condition = True
while condition:
    def speak(text):   
        name = ".speak.mp3"
        gtts = gTTS(text=text, lang='pt', slow=False) 
        gtts.save(name)
        try:
            try:
                try:
                    try:
                        os.system('cvlc {} --play-and-exit'.format(name))
                    except:
                        os.system('sudo apt install cvlc')
                except:
                    try:
                        os.system('cvlc {} --play-and-exit'.format(name))
                    except:
                        os.system('sudo pacman -S cvlc')
            except:
                os.system('cvlc {} --play-and-exit'.format(name))     
        except:
            os.system('sudo apt install cvlc')
            url = 'https://get.videolan.org/vlc/3.0.12/win32/vlc-3.0.12-win32.exe'
            print('\t Você não possui o VLC, instale com o seguinte link:\n')
            print(f'\t \t {url}')
            os.system(f'start chrome {url}')
            print('\t Reinicie os comandos ...')
                

    if __name__ == '__main__':
        text = input("\n {} Oque eu digo ? ".format(emojize(":rosto_pensativo:",language = 'pt')))
        speak(text)
        answer = str(input("\n {} Denovo ? ".format(emojize(":rosto_pensativo:",language = 'pt'))))
        while (answer.lower() != 'nao') and (answer.lower() != 'sim'):
            emoji = emojize(":aviso:",language = 'pt')
            warnings.warn(f'{emoji} resposta nao identificada, tente denovo.  {emoji}')
            answer = str(input("\n {} Denovo ? ".format(emojize(":rosto_pensativo:",language = 'pt'))))
        if (answer.lower() != 'sim') and (answer.lower() == 'nao'):
            condition = False