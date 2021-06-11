import sys
import os
import string

assert len(sys.argv)==2, 'argument is 1. Ex) python quran_analysis.py'
assert os.path.exists(sys.argv[1]), '{} is not exist'.format(sys.argv[1])

with open(sys.argv[1]) as f:
    lines=[line.replace('\n','') for line in f.readlines()]

def remove(sentence,lower_case=True):
    words = sentence.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    if lower_case:
        lower = [w.lower() for w in stripped]
    else:
        lower = stripped
    return lower
        
words=set()
count = 0 
for line in lines:
    line = remove(line)
    words = words | set(line)

print(sys.argv[1])
print('lines: {}'.format(len(lines)))
print('words: {}'.format(len(words)))
