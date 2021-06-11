# tatar_transliteration
## Demo page is available

If you want to compare the results in the exact same environment as the paper, try please try the demo page (https://yusuke1997.com/tatar) !!

## Usage from github

### Our Environments

- macOS Catalina
- zsh
- Python 3.9.4

### Requirements

This code uses the `shuf` command, so please set it up:

```bash
brew install coreutils # if you use brew as a package manager
or
sudo apt install coreutils # ubuntu,debian,kali linux...
# if you use any other OS, search following url.
https://command-not-found.com/shuf
```

Next, download the python dependencies using pip

```bash
pip install -r requierement.txt
```



### Running the code

Please clone this code.

And then, run the following shell script to complete all the preparations.

```shell
./prepare.sh
```
Next, the transliteration is executed by running the following python file.

```shell
python3 predict.py
```

When you type a Tatar sentence written in Cyrillic, it is processed and dealt with line by line.

If you want to check whether the subwords in each sentence are recognized as Russian or Tatar, run the following python file.

```shell
python3 inference.py
```

 However, inference.py only considers the subwords in the initial state, and in fact we do some processing on the labels of the subwords in the initial state.

If you want to know the probabilities and labels of the final subwords, uncomment-out `print(elm,lang)` at about line 188 of predict.py.

The whole process can be seen in `prepare.sh` and the `predict` function in `predict.py`.

If you want to start the experiment from scratch, just run `./delete.sh` .

If you want to start from the middle, rewrite `. /delete.sh` appropriately.



The data used for the evaluation were kindly provided by the authors and are therefore considered as closed data.

The whole evaluation directory is written in `.gitignore`, so if you want the evaluation script, please contact us!

If there is anything else, please feel free to contact us in any language!



## citation

```
@inproceedings{taguchi-etal-2021-transliteration,
    title = "Transliteration for Low-Resource Code-Switching Texts: Building an Automatic {C}yrillic-to-{L}atin Converter for {T}atar",
    author = "Taguchi, Chihiro  and
      Sakai, Yusuke  and
      Watanabe, Taro",
    booktitle = "Proceedings of the Fifth Workshop on Computational Approaches to Linguistic Code-Switching",
    month = jun,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/2021.calcs-1.18",
    pages = "133--140",
}
```

