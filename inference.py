from fasttext import load_model
import string
import codecs
from subword_nmt import apply_bpe

def remove(sentence):
    words = sentence.split()
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    lower = [w.lower() for w in words]
    return ' '.join(lower)


def predict_language(word, model, k=1):
    labels=set()
    subword_elements=[]
    subword=word.split()
    for elm in subword:
        label, prob = model.predict(elm, k)
        subword_elements.append((label,prob))
        if prob>0.8:
            labels.add(label)
    if len(labels)<2:
        return predict_language_word(word,model)
    else:
        return [(elm[0][0].replace("__label__", "").replace('@@ ',''),elm[1]) for elm in subword_elements]

def predict_language_word(text, model, k=1):
    label, prob = model.predict(text, k)
    return list(zip([l.replace("__label__", "") for l in label], prob))

model = load_model("model/langdetect.bin")
codes = codecs.open('model/model.bpe', encoding='utf-8')
bpe=apply_bpe.BPE(codes=codes)

while(True):
    words=input()
    if words in ['\n','']:break
    words=remove(words).split()
    for word in words:
        subword=bpe.process_line(word)
        print(subword.replace('@@','')+': '+str(predict_language(subword,model)))
    #print(predict_language(words,model)[0])
