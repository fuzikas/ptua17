# You have a list of ten random words which starts with letters A, C, or P.
# Write a function that takes a list of the word_list and prints new list 
# with all words that starts with letter P.

from typing import List

word_list = ["apple", "car", "park", "cat", "plane", "cup", "carpet", "pet", "map", "panda"]
p = "p"
def filtering(word_list:List[str]) ->List[str]:
    new_list =[]
    for word in word_list:
        if word.startswith(p):
            new_list.append(word)
    print(new_list)
    return new_list

filtering(["apple", "car", "park", "cat", "plane", "cup", "carpet", "pet", "map", "panda"])


def antras(word_list:List[str])->List:
    sec_list = []
    for word in word_list:
        for letter in word:
            if letter == "p":
                sec_list.append(word)
            break
    print(sec_list)
    return sec_list

antras(["apple", "car", "park", "cat", "plane", "cup", "carpet", "pet", "map", "panda"])

def extract_specific_words(word_list: List[str]) -> List[str]:
    return [name for name in word_list if name.upper().startswith('P')]

extract_specific_words(word_list)