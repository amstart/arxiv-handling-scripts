import sys, os
import glob
import subprocess
from timeout import timeout

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + sys.argv[1] + os.path.sep + 'run1.xml')

with open("runs" + os.path.sep + "run1POST_" + sys.argv[1] + ".log", 'w+') as log:
    for index, item in enumerate(file_list):
        log.write(str(index) + ":" + item + "\n")

err_list = []
to_do = file_list[int(sys.argv[2]):]
for index, mainfile in enumerate(to_do):
    with open(mainfile[:-8] + "run1TEIcmml.log", 'w+') as log:
        print(str(index + int(sys.argv[2])) + ":" + mainfile)
        try:
            subprocess.call(["perl", "latexmlpost",
            "--destination=" + mainfile[:-8] + "run1cmml.tei", "-format=tei",
            "-cmml", mainfile], stdout=log, stderr=subprocess.STDOUT, timeout=120)
        except Exception as err:
            print("error with" + mainfile + ": ")
            print(err)
            err_list.append(mainfile)

if err_list:
    with open("runs" + os.path.sep + "errrun1POST_" + sys.argv[1] + ".log", 'w+') as log:
        for index, item in enumerate(err_list):
            log.write(str(index + int(sys.argv[2])) + ":" + item + "\n")
