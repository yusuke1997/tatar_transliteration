import sys
import os
import string

assert len(sys.argv)>1, 'arguments are 2 or more'

def remove(sentence):
    words = sentence.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    lower = [w.lower() for w in stripped]
    return ' '.join(lower)

for i in range(1,len(sys.argv)):
    assert os.path.exists(sys.argv[i]),'{} is not exist'.format(sys.argv[i])
    with open(sys.argv[i], 'r') as src:
        with open(sys.argv[i].rsplit('.',1)[0]+'.parse','w') as tgt:
            for line in src:
                tgt.write(remove(line)+'\n')   
