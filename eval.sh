python3 cy2lt.py < metrics/tatar_web_corpus_1000cyrillic.txt > metrics/inference.txt
python3 predict_api.py < metrics/tatar_web_corpus_1000cyrillic.txt > metrics/inference_hybrid.txt
echo 'hybrid'
python3 metrics/evaluate.py metrics/inference_hybrid.txt metrics/tatar_web_corpus_1000latin.txt
echo 'only tatar'
python3 metrics/evaluate.py metrics/inference.txt metrics/tatar_web_corpus_1000latin.txt
