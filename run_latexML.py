import sys, os
import glob
import subprocess

file_list = glob.glob('..' + os.path.sep + '..' + os.path.sep + 'source' +
    os.path.sep + '*' + os.path.sep + '*' + sys.argv[1] + os.path.sep + 'main.tex')

with open("runs" + os.path.sep + "run1_" + sys.argv[1] + ".log", 'w+') as log:
    for index, item in enumerate(file_list):
        log.write(str(index) + ":" + item + "\n")
#
# for mainfile in [file_list[0]]:
err_list = []
to_do = file_list[int(sys.argv[2]):]
for index, mainfile in enumerate(to_do):
    with open(mainfile[:-8] + "run1.log", 'w+') as log:
        print(str(index + int(sys.argv[2])) + ":" + mainfile)
        try:
            subprocess.call(["perl", "latexml", "--destination=" + mainfile[:-8] + "run1.xml", mainfile],
            timeout=120, stdout=log, stderr=subprocess.STDOUT)
        except Exception as err:
            print("error with" + mainfile + ": ")
            print(err)
            err_list.append(mainfile)

if err_list:
    with open("runs" + os.path.sep + "errrun1_" + sys.argv[1] + ".log", 'w+') as log:
        for index, item in enumerate(err_list):
            log.write(str(index + int(sys.argv[2])) + ":" + item + "\n")
