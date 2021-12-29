import sys
import string

morse_dict = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ' ': '/'}

i = 1
str =''
while i < len(sys.argv):
    if  i == 1:
        str = str + sys.argv[i]
    else:    
        str = str + ' ' + sys.argv[i]
    i += 1
str = str.upper()
str2= ''
if  all(c.isalnum() or c.isspace() for c in str): 
    for c in str:
        str2 += morse_dict[c] + ' '
else:
    sys.exit("error")
print(str2[:-1:])
     
