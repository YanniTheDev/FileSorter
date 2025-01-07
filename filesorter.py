import os
import shutil

# Specifying source paths where the unsorted files are
with open("sourcepath.txt") as f:
    lines = f.readline()

source = os.listdir(lines)
