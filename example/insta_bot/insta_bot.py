# from instabot import Bot
# bot = Bot()
# bot.login(username = "testando@gmail.com",
#           password = "12345678")

# bot.upload_photo("asdasd.jpg",
#                 caption = ".")
from emoji import emojize
from instabot import Bot
def bot(user, password, caption, name):
    bot = Bot()
    bot.login(username = user,
              password = password)

    #bot.upload_photo(name, caption = open(caption, 'r').read())
    bot.upload_photo(name, caption = caption)

if __name__ == '__main__':
    emj1,emj2 = emojize(':cadeado:', language='pt'), emojize(':post_office:', language='en')
    emj3 = emojize(':framed_picture:', language='en')
    USER, PASSWORD = input(f'\n{emj1} Username: '), input(f'{emj1} Password: ')
    CAPTION, NAME = input(f'\n{emj2} Caption: '), input(f'\n{emj2} ImgName: ')
    bot(user=USER,password=PASSWORD,caption=CAPTION,name=NAME)