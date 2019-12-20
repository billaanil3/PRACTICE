from unidecode import unidecode

def replace_unicode_characters(text, spchars):
    """
    Replace unicode characters.
    """
    if isinstance(text, (unicode, str)):
        try:
            text = text.encode('utf-8')
        except:
            pass
        text = text.decode("utf-8", "replace")
        print "^^^^^^^^^^^^^^^^^^",text
        text = unidecode(text)
        print ",,,,,,,,,,,,,",text
        for spchar in spchars:
            print spchar
            # print "...................",len(spchars)
            text = text.replace(spchar[0], spchar[1])
            print text
        while text.find("  ") >= 0:
            text = text.replace("  ", " ")
    return text

lst = ["(", ")", "[", "]", "{", "}", "<", ">", "!", "#","$", "%", "^", "&", "*", "+", "/", ",", "?"]
replace_unicode_characters("Hai Anil Billa /u { } < $ * # ( ) How are you",lst)
                        # ["(", ")", "[", "]", "{", "}", "<", ">", "!", "#","$", "%", "^", "&", "*", "+", "/", ",", "?"])
