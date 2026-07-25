class Solution:
    def detectCapitalUse(self, word: str) -> bool:
    
        n =len(word)

        count = 0   

        if word.isupper():
            return True
        elif word.islower():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True
        else:
            return False
        