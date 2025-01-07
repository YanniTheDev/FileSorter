import os
import shutil

# Specifying source paths where the unsorted files are
with open("sourcepath.txt") as source_path:
    source = source_path.readline()

source_destination = os.listdir(source)

# Specifying where our sorted files will end up
with open("destinationpath.txt") as destination_path:
    destinations = destination_path.readline()

# Separating the destinations into each individual destination
destinations = destinations.split(",")

# Moving files
for file in source_destination:
    if file.endswith(".pdf"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[0], file))
    elif file.endswith(".exe") or file.endswith(".msi"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[1], file))
    elif file.endswith(".mp3"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[2], file))
    elif file.endswith(".zip"):
        shutil.move(os.path.join(source, file), os.path.join(destinations[3], file))