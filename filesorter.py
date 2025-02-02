import os
import shutil

from tqdm import tqdm

import time

# Specifying source paths where the unsorted files are
with open("sourcepath.txt") as source_path:
    source = source_path.readline()

source_files = os.listdir(source)

# Specifying where our sorted files will end up
with open("destinationpath.txt") as destination_path:
    destinations = destination_path.readline()

# Separating the destinations into each individual destination
destinations = destinations.split(",")

# Moving files
for file in tqdm(source_files):
    if file.endswith(".pdf"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[0], file))
    elif file.endswith(".exe") or file.endswith(".msi"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[1], file))
    elif file.endswith(".mp3"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[2], file))
    elif file.endswith(".zip"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[3], file))
    elif file.endswith(".txt"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[4], file))
    elif file.endswith(".mp4"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[5], file))
    elif file.endswith(".png"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[6], file))
    
# Adding a little delay so that the Files Sorted! message comes after the 100%
time.sleep(0.1)

print("\nFiles sorted!")