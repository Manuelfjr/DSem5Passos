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