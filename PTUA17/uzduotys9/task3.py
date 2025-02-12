def count_words_with_e(text):
    return len([word for word in text.split() if "e" in word])


user_text = input("Įveskite tekstą: ")
words_with_e = count_words_with_e(user_text)
print("Žodžių su 'e' skaičius:", words_with_e)