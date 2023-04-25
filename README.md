# MT Exercise 3: Pytorch RNN Language Models

This repo shows how to train neural language models using [Pytorch example code](https://github.com/pytorch/examples/tree/master/word_language_model). Thanks to Emma van den Bold, the original author of these scripts. 

# Requirements

- This only works on a Unix-like system, with bash.
- Python 3 must be installed on your system, i.e. the command `python3` must be available
- Make sure virtualenv is installed on your system. To install, e.g.

    `pip install virtualenv`

# Steps

Clone this repository in the desired place:

    git clone https://github.com/moritz-steiner/mt-exercise-03
    cd mt-exercise-03

Create a new virtualenv that uses Python 3. Please make sure to run this command outside of any virtual Python environment:

    ./scripts/make_virtualenv.sh

**Important**: Then activate the env by executing the `source` command that is output by the shell script above.

Download and install required software:

    ./scripts/install_packages.sh

Download and preprocess data:

    ./scripts/download_data.sh

Train a model:

    ./scripts/train.sh

The training process can be interrupted at any time, and the best checkpoint will always be saved.

Generate (sample) some text from a trained model with:

    ./scripts/generate.sh


# Documenting Changes - sebets

In this section I document the changes which I made in this repository.

## Folder "scripts"

### download_data.sh

To download my own data set I duplicated the script and named it "download_data_Alice.sh".
This allowed me to easily compare with the original if needed.
I more or less left all the settings, just changed the link and the naming.
The command to run it just changed to: `./scripts/download_data_Alice.sh`

### train.sh

I added a new argument (which I created in the main.py), named "--save_perp" to specify a text file, my values would be saved to.
Other than that, I just played with the settings and hyperparameters to create different models.

### generate.sh

I adapted it to take my alice data as input and tried my trained models.



## Folder "word_language_model"

### main.py
I adapted it, so it would take one more argument to define where to save the log scores to (there is a default).
For every model, the scores are saved in a new text file.
All the changes I made in the script I commented with my initials "SB".

### dropout_scores_and_plotting folder
I created a new folder to store all my text files with the saved log values, so I wouldn't constantly overwrite them againg by accident
(trust me, that happened a lot...).

Additionally, I created the plot_perplexity.py script to plot the log value files. It creates two graphs, 
one to compare the validation and one for test perplexity scores. 
It saves them as .png images.
The script works without command line arguments, it is adapted specifically for this task.

The command I used to run it is simply:

`$ python3 plot_perplexity.py`

All the text files have to be in the same folder as the script. 
If the text files are changed, the script needs to be adapted too.


