import sys, os, subprocess
from tqdm import tqdm
import glob
import gzip
import tarfile, io
from pathlib import Path
import shutil

file_list = glob.glob('*' + os.path.sep + '*.gz', recursive=True)

for gzip_path in file_list:
    gzip_file = gzip.open(gzip_path).read()
    newpath = gzip_path[:-3]
    newfilepath = newpath + os.path.sep
    file_like_object = io.BytesIO(gzip_file)
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    try:
        with tarfile.open(fileobj = file_like_object) as tarcandidate:
            tarcandidate.extractall(path=newfilepath)
    except:
        with open(newfilepath + "main.tex", 'wb+') as outfile:
            outfile.write(gzip_file)
    if not os.path.isfile(newfilepath + "main.tex"):
        tex_list = glob.glob(newfilepath + '*.tex', recursive=True)
        for tex in tex_list:
            print(tex)
            if "begin{document}" in open(tex).read():
                p = Path(tex)
                p.rename(Path(p.parent, "main.tex"))



        # newpath = gzip_path[:-3]
        # newfilepath = newpath + os.path.sep + "main.tex"
        # if not os.path.exists(newpath):
        #     os.makedirs(newpath)
        # with open(newfilepath, 'wb') as outfile:
        #     outfile.write(gzip_file)
        #     if tarfile.is_tarfile(newfilepath):
        #         with tarfile.open(newfilepath) as tarcandidate:
        #             print(gzip_path)
        #             tarcandidate.extractall(path=newpath)
        #     # os.remove(newfilepath)
