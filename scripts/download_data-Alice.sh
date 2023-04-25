#! /bin/bash

scripts=$(dirname "$0")
base=$scripts/..

data=$base/data

mkdir -p $data

tools=$base/tools

# link default training data for easier access

mkdir -p $data/wikitext-2

for corpus in train valid test; do
    absolute_path=$(realpath $tools/pytorch-examples/word_language_model/data/wikitext-2/$corpus.txt)
    ln -snf $absolute_path $data/wikitext-2/$corpus.txt
done

# download a different interesting data set!

mkdir -p $data/alice

mkdir -p $data/alice/raw

wget https://www.gutenberg.org/cache/epub/11/pg11.txt
mv pg11.txt $data/alice/raw/wonderland.txt

# preprocess slightly

cat $data/alice/raw/wonderland.txt | python $base/scripts/preprocess_raw.py > $data/alice/raw/wonderland.cleaned.txt

# tokenize, fix vocabulary upper bound

cat $data/alice/raw/wonderland.cleaned.txt | python $base/scripts/preprocess.py --vocab-size 5000 --tokenize --lang "en" --sent-tokenize > \
    $data/alice/raw/wonderland.preprocessed.txt

# split into train, valid and test

head -n 440 $data/alice/raw/wonderland.preprocessed.txt | tail -n 400 > $data/alice/valid.txt
head -n 840 $data/alice/raw/wonderland.preprocessed.txt | tail -n 400 > $data/alice/test.txt
tail -n 3075 $data/alice/raw/wonderland.preprocessed.txt | head -n 2955 > $data/alice/train.txt
