#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

files = os.listdir(".")
for file in files:
    os.rename(file, file.replace("before", "after")) #params to rename the file
