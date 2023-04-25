#! /bin/bash

scripts=$(dirname "$0")
base=$(realpath $scripts/..)

models=$base/models
data=$base/data
tools=$base/tools

echo "test dropout 0.95"

mkdir -p $models

num_threads=4
device=""

SECONDS=0

(cd $tools/pytorch-examples/word_language_model &&
    CUDA_VISIBLE_DEVICES=$device OMP_NUM_THREADS=$num_threads python main.py --data $data/alice \
        --epochs 40 \
        --log-interval 100 \
        --emsize 200 --nhid 200 --dropout 0.95 --tied \
        --save $models/model_dropout095.pt \
        --save_perp dropout095.txt
)

echo "time taken:"
echo "$SECONDS seconds"
