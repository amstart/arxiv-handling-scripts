import sys, os
import ast
from tqdm import tqdm
import glob

with open(sys.argv[1], 'r') as test_collection_file:
    test_collection = {}
    for line in test_collection_file:
        test_collection[line[48:-1]] = line

print(len(test_collection))
file_list = glob.glob('*.tar')

for element in file_list:
    test_collection.pop(element, None)

with open("remaining.txt", 'w') as outfile:
    for value in test_collection.values():
        outfile.write(value)


print(len(test_collection))
