from __future__ import annotations
from beginnercodes.challenges import test

def no_yelling(sentence):

    if sentence[-1] != "!" and sentence[-1] != "?":           #if last character is not ! or ?, it's ok
        return sentence

    else:
        if sentence[-2] != sentence[-1]:          #if last character is ! or ?, and there's only one, it's ok
            return sentence
        else:
            new_sentence = sentence.rstrip(sentence[-1])      #if there is more than one repeating ! or ?, strip all from the end then add just one
            return new_sentence+sentence[-1]

print(no_yelling("HELLO MY NAME IS AL!!!!!"))

test(588, no_yelling)


