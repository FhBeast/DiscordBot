def simplify_word(word):
    last_letter = ''
    result = ''
    
    # пробегаемся по каждой букве слова
    for letter in word:
        if letter != last_letter:
            last_letter = letter
            result += letter
    
    return result