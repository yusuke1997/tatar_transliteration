mkdir -p data
mkdir -p model

SRC='preprocess_src'
DATA='data'
MODEL='model'

echo $MODEL
echo $DATA
echo $SRC
#prepare datasets
sh download.sh

#parse
#pip install subword-nmt

echo 'prepare to all.txt'
python3 $SRC/json2text.py $DATA/*.json
python3 $SRC/parse.py $DATA/*.txt
python3 $SRC/word_level_separation.py $DATA/*.parse
python3 $SRC/add_labels.py $DATA/*.word

#separate to test / valid
cat $DATA/*.label | shuf > $DATA/all.txt

echo 'apply subword method'
#-sはデフォルトで10000なので多めに見積もって16Kで行った
subword-nmt learn-bpe -s 16000 < $DATA/all.txt > $MODEL/model.bpe
subword-nmt apply-bpe -c $MODEL/model.bpe < $DATA/all.txt > $DATA/all.subword

head -n 100 $DATA/all.subword > $DATA/valid.txt
tail -n +101 $DATA/all.subword > $DATA/train.txt
#https://fasttext.cc/blog/2017/10/02/blog-post.html

if [ ! -d "fastText" ]; then
	git clone https://github.com/facebookresearch/fastText.git
	cd fastText	
	if [ ! -f "fasttext" ]; then
	    make ;
	    pip install .
	fi
	cd ..
fi

./fastText/fasttext supervised -input $DATA/train.txt -output $MODEL/langdetect -dim 16 -minn 2 -maxn 4 -loss hs


