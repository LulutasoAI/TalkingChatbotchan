import random
import texts
import pickle
import os
import pyttsx3


listy = []
#path = r"G:\Discordproj"
text_path = "text.sav"
try:
    file = open(text_path,"rb")
    texten = pickle.load(file)
    file.close
except:
    texten = []
    for a in listy:
        texten.append(a)
print(len(texten))
print(texten)


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
while True:
    try:
        randomizer = random.randint(0,len(texten))
        txt = texten[randomizer]
    except:
        txt = "Hello!"
    engine.say(txt)
    engine.runAndWait()
    X = str(input("{}".format(txt)))

    if "save" in X or "Save" in X:
        file =open(text_path, "wb")
        pickle.dump(texten,file)
        file.close()
        print("textfile Saved!")
    elif "quit" in X:
        break
    else:
        texten.append(X)
