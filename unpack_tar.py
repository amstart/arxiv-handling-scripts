import sys, os
import tarfile
from tqdm import tqdm
import glob

file_list = glob.glob('*.tar')


with open(sys.argv[1], 'r') as test_collection_file:
    test_collection = {}
    for line in test_collection_file:
        test_collection[line[:-1]] = True


def gz_files(members):
    for tarinfo in members:
        if test_collection.pop(tarinfo.name.split("/")[-1][0:-3], None):
            yield tarinfo

for tarball in tqdm(file_list):
    tar=tarfile.open(tarball)
    tar.extractall(path=".." + os.sep + "source" + os.sep, members=gz_files(tar))
    tar.close()
