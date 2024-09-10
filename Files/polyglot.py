from Files.polyglot import Translator

translator = Translator(to_lang='es')

try:
    with open('translate.txt', mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('translate-version.txt', mode='w') as translated_file:
            translated_file.write(translation)

except FileNotFoundError as err:
    print('File not found. Check the file path.')
