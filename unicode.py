from unidecode import unidecode

def replace_unicode_characters(text, spchars):
    """
    Replace unicode characters.
    """
    # print type(text)
    if isinstance(text, (unicode, str)):
        try:
            text = text.encode('utf-8')
        except:
            pass
        text = text.decode("utf-8", "replace")
        text = unidecode(text)
        for spchar in spchars:
            text = text.replace(spchar[0], spchar[1])
        while text.find("  ") >= 0:
            text = text.replace("  ", " ")
    print text

spchars = [('\r', ' '), ('\n', ' '), ('\t', ' ')]
text = u'2019'
replace_unicode_characters(text, spchars)
