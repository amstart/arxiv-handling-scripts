import hashlib
import glob
import sys,os
import xml.etree.ElementTree as ET
from tqdm import tqdm

resultdict = {}
file_list = glob.glob('*files.xml')
for file_name in tqdm(file_list):
    tree = ET.ElementTree()
    root = tree.parse(file_name)
    tar_file_xml = root.findall("./file")[0]
    tar_sha1_xml = tar_file_xml.findall("./sha1")[0]
    name = tar_file_xml.attrib['name']
    tar  = open(name, 'rb')
    tardata = tar.read()
    tar.close()
    m = hashlib.sha1()
    m.update(tardata)
    print(file_name)
    resultdict[name] = m.hexdigest() == tar_sha1_xml.text

print(resultdict)
