#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  Seraina Betschart
# date: 20.04.2023
# Machine Translation Ex 3 - plot perplexities in a line graph

import matplotlib.pyplot as plt


f = plt.figure()
f.set_figwidth(15)
f.set_figheight(15)


def prep_for_plot(file):
    """Takes a text file as input with one value per line and stores them in a training and a validation list.
    The last value (test perplexity) is separated and all three, the value and the lists, are returned for plotting."""
    text_list=[]
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            ele=line.split("\n")
            ele=ele[0]
            try:
                ele=float(ele)
            except:
                pass
            text_list.append(ele)

    ind=text_list.index("validation perplexities:")
    train_list=text_list[1:ind]
    valid_list=text_list[ind+1:-2]
    test_value=text_list.pop()

    return train_list, valid_list, test_value


def plot_line(score_list, dropout_value, col="grey", xlabel="epoch", ylabel="perplexity",
              x_values=False, show_x_values=False):
    """Takes a list and plots the items as one continuous line in a line graph."""

    if not x_values:
        x = []
        y = []
        for ele in score_list:
            y.append(float(ele))
            x.append(score_list.index(ele)+1)
    else:
        x = x_values
        y = []
        for ele in score_list:
            y.append(float(ele))

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if show_x_values:
        plt.xticks(x)
    plt.plot(x, y, marker='o', color=col, label=dropout_value)


test_list=[]
dropout_list=[0.0, 0.1, 0.2, 0.5, 0.8]
text_file_list=["dropout00.txt", "dropout01.txt", "dropout02.txt", "dropout05.txt", "dropout08.txt"]
color_list=["purple", "blue", "cyan", "green", "yellow", "orange", "red", "brown"]


# create the graph for validation perplexities and prepare the test list
for i, ele in enumerate(text_file_list):
    train_list, valid_list, test_value=prep_for_plot(ele)
    plot_line(train_list, dropout_list[i], color_list[i])
    test_list.append(test_value)

plt.title("Training Perplexities")
plt.legend(loc="upper right", title="Dropout Rate")
plt.show()
plt.savefig("graph_training_perplexities.png")
plt.clf()


# create the graph for training perplexities
for i, ele in enumerate(text_file_list):
    train_list, valid_list, test_value=prep_for_plot(ele)
    plot_line(valid_list, dropout_list[i], color_list[i+1])

plt.title("Validation Perplexities")
plt.legend(loc="upper right", title="Dropout Rate")
plt.show()
plt.savefig("graph_validation_perplexities.png")
plt.clf()


# create the graph for test perplexities
plot_line(test_list, "default", "red",  "dropout value", "perplexity", dropout_list, True)
plt.title("Test Perplexities")
plt.show()
plt.savefig("graph_test_perplexities.png")


