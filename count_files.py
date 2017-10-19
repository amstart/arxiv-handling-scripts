import sys, os
import glob

print("ntcir set:105120")

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*.gz')

print("gz:" + str(len(file_list)))

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + os.path.sep)

print("folders:" + str(len(file_list)))

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + os.path.sep + 'main.tex')

print("tex:" + str(len(file_list)))

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + os.path.sep + 'run1.xml')

print("xml:" + str(len(file_list)))

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + os.path.sep + 'run1cmml.tei')

print("tei:" + str(len(file_list)))
