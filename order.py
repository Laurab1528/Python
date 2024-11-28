
from typing import List

class WordForm:
    def __init__(self, words: List[str]):
     

        self.words = words

    def form_word(self) -> str:

        formed_word = ""
        for i, word in enumerate(self.words):
            if i < len(word):  
                formed_word += word[i]  
        return formed_word

