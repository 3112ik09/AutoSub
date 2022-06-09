from googletrans import Translator
translator = Translator()
result = translator.translate('रुक जाओ', src='hi', dest='en')
# print(result.src)
# print(result.dest)
print(result.text)
