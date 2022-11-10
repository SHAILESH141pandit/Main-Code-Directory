
import random

emptyList = []

def displayWord(CWord):
    '''Display the random arrangement ward, the displayward function is used.'''
    for i in CWord:
        emptyList.append(i)
    random.shuffle(emptyList)
    Shuffle_RandomWord = ''.join(emptyList)
    emptyList.clear()
    return Shuffle_RandomWord
