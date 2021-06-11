# tatar
usage

Very simple
```
./workflow.sh
```
If you want to check accuracy of language detection, you run
```
python3 inference.py
```

If you want to transliterate,
```
python3 predict_api.py
```
But predict_api.py is only able to russian transliteration now.
If you make tatar transliteration rules,you add it to alphabet/tat.yml, and change transfer.py.