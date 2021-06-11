import sys
import os
import string

assert len(sys.argv)>1, 'arguments are 2 or more'

for i in range(1,len(sys.argv)):
    word_list=set()
    assert os.path.exists(sys.argv[i]),'{} is not exist'.format(sys.argv[i])
    with open(sys.argv[i], 'r') as src:
        for line in src:
            word_list=word_list | set(line.replace('\n','').split())
        with open(sys.argv[i].rsplit('.',1)[0]+'.word','w') as tgt:
            for word in word_list:
                tgt.write(word+'\n')
