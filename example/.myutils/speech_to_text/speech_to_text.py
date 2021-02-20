import speech_recognition as sr
from emoji import emojize
import os as os
import time
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
    ################
    elif (frase != None) and (frase.lower().split(' ')[0] == 'desligar') and (frase.lower().split(' ')[1] == 'agora'):
        print(os.system('shutdown'))
        condition = False
    elif (frase != None) and (frase.lower().split(' ')[0] == 'desligar') and (frase.lower().split(' ')[1] == 'depois'):
        hnow = time.strftime('%H:%M', time.localtime())
        minutes = hnow.split(':')[1]
        hnow_new = int(hnow.split(':')[0]) + int(frase.split(' ')[-2])
        print(os.system(f'shutdown {hnow_new}:{minutes}'))

    ################