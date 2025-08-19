import sys
script, input_encoding, error = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)

languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)

# 3 different way to display copyright in pyhton
print("\u00a9")
# Codepunkt gehöriges Zeichen ermitteln
print(chr(0xA9))
print(chr(169))

# ASCII: standard maps a number to a letter
# jede Sprache hat ihre eigene Codierung 
# Unicode ist ein internationaler Standard zur Codierung, Darstellung und Verarbeitung von
# Textzeichen aus nahezu allen Schriftsystemen der Welt.
# UTF-8 ist eine Unicode Variante
# https://www.ionos.de/digitalguide/websites/webseiten-erstellen/unicode/


raw_bytes = b'\xe6\x96\x87\xe8\xa8\x80'
utf_string = "文言"
print(raw_bytes.decode())
print(utf_string.encode())
print(raw_bytes == utf_string.encode())
print(utf_string == raw_bytes.decode())

## Merke DBES -> Decode Bytes Encode Strings