import os
from os import listdir

from os.path import isfile, isdir, join, abspath

path_to_input = abspath('../OpenLabeling/main/input')
paths_to_input_dirs = [f for f in listdir(path_to_input) if isdir(join(path_to_input, f))]
path_to_output = abspath('../OpenLabeling/main/output/YOLO_darknet')
paths_to_output_dirs = [f for f in listdir(path_to_output) if isdir(join(path_to_output, f))]

paths_to_jpgs = [join(path_to_input, p, f) for p in paths_to_input_dirs for f in listdir(join(path_to_input, p))]
paths_to_labels = [join(path_to_input, p, f) for p in paths_to_output_dirs for f in listdir(join(path_to_output, p))]

with open('volen/train.txt', 'w') as file:
    file.write('\n'.join(paths_to_jpgs))
    file.write('\n'.join(paths_to_labels))
