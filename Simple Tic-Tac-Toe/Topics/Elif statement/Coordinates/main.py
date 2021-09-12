name = input()
dict_ = {'é': 'e',
         'ë': 'e',
         'á': 'a',
         'å': 'a',
         'œ': 'oe',
         'æ': 'ae'}

def normalize(str_1):
    for letter in str_1:
        for id_, item in dict_.items():
            if letter == id_:
                str_1 = str_1.replace(letter, item)
    return str_1

print(normalize(name))
