import os

files = os.listdir(".")
for file in files:
    os.rename(file, file.replace("-min", "")) #params to rename the file