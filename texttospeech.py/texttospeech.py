from gtts import gTTS

text ="Hello, how are you?"
language = 'en'
obj = gTTS(text= text, lang = language, slow = False)
obj.save("sample.mp3")