
#https://github.com/IvanWend/python_practice - ссылка на репозиторий, который я создал использую Git комманды

import string

def text_cleaner(text):

    clean_text = ""

    for i in text:
        if i not in string.punctuation:
            clean_text += i

    words = clean_text.lower().split()

    return words

print(text_cleaner("What did you just say?"))

    