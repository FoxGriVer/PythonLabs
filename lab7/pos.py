#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Programming for Computational Linguistics 2019/2020
    OOP -- exercises
    Exercise 4
"""

from builder import *

def get_unique_pos(filename, builder):
    result = { }
    for line in open(filename, "r"):
        line = line.strip()
        if line == "":
            continue

        # this is the place where we use the builder
        # the cool part is that we don't care what is the format of the file we read
        tok = builder.buildToken(line)

        if(result.get(tok.pos) == None):
            result[tok.pos] = 1
        else:
            result[tok.pos] += 1 
        
    # let's convert it to list
    return list(result.keys())

def build_builder(filename):
    if filename.endswith("conllu"):
        builder = ConLLUTokenBuilder()
    elif filename.endswith("conll09"):
        builder = ConLL09TokenBuilder()
    else:
        raise RuntimeError("Unknown file format: " + filename)

    return builder


## here the main part starts
filename = "c:/Users/MacPavel/Desktop/pythonLabs/lab7/small_train.conllu"
builder = build_builder(filename)

unique_pos = get_unique_pos(filename, builder)
print("Nr of unique POS (should be 10):", len(unique_pos))
