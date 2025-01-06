import random
import string
import iuliia


# транскрипция имени фамили с русского на английский 
def transliterate(name):
   return iuliia.translate(name, schema=iuliia.WIKIPEDIA)

# генерирует пароль по типу cybquw-7gakri-Qygpop
def pass_generation():
    characters = string.ascii_letters + string.digits
    pas = ""
    for i in range(19):
       if i == 6 or i == 13:
          pas += "-"
       else:
          pas += characters[random.randrange(len(characters))]
    return pas


