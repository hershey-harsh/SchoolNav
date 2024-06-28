from googletrans import Translator

def english_to_spanish(description):
    translator = Translator()
    translation = translator.translate(description, src='en', dest='es')
    return translation.text