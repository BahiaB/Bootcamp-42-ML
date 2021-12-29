import sys
import string

def text_analyzer(text=None):
    
    if text is None:
        text = input("What is the text to analyze? ")
    if len(text) == 0:
        print("No text to analyze.")
    else:
        marks = 0
        space = 0
        up = 0
        low = 0
        dig = 0
        i = 0
        for c in text:
            if c.isupper():
                up += 1
            elif c.islower():
                low += 1
            elif c.isdigit():
                dig += 1
            elif c in (string.punctuation):
                marks += 1
            else:
                space += 1
            i += 1
        print(f'the text contain, {i} charactere\n {up} upper latter\n {low} Lower letter')
        print(f' {dig} digit character\n {marks},punctuation marks\n and {space} space')
    




    
       
    