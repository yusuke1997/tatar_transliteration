import sys
import os
import string

assert len(sys.argv)>1, 'arguments are 2 or more'

for i in range(1,len(sys.argv)):
    assert os.path.exists(sys.argv[i]),'{} is not exist'.format(sys.argv[i])
    with open(sys.argv[i], 'r') as src:
        with open(sys.argv[i].rsplit('.',1)[0]+'.label','w') as tgt:
            label=sys.argv[i].rsplit('-',1)[0]
            label=label.split('/')[-1]
            for line in src:
                tgt.write('__label__'+label+' '+line)
