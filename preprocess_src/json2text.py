import sys
import os
import json

assert len(sys.argv)>1, 'arguments are 2 or more'

for i in range(1,len(sys.argv)):
    assert os.path.exists(sys.argv[i]),'{} is not exist'.format(sys.argv[i])
    with open(sys.argv[i], 'r') as json_open:
        json_load = json.load(json_open)['quran']
        with open(sys.argv[i].replace('json','txt'),'w') as txt_open:
            for text in json_load:
                txt_open.write(text['text']+'\n')
                
            
