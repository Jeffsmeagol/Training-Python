import wikipedia
from gtts import gTTS

import os

mytext = wikipedia.summary('canton concourse', sentences=5)

language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)

myobj.save('voice1.mp3')

os.system('mediaplayer voice.mp3')