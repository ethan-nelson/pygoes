# -*- coding: utf-8 -*-
# MIT License (c) 2018 Ethan Nelson

import os
import requests
from io import BytesIO
import xml.etree.cElementTree as ElementTree


def get_filenames(product, year, dayofyear, hour, AWS_URL="https://s3.amazonaws.com/noaa-goes16/"):
    url = "%s?prefix=%s/%s/%s/%s/" % \
            (AWS_URL, str(product), str(year), str(dayofyear).zfill(3), str(hour).zfill(2))
    content = requests.get(url)
    content = BytesIO(content.content)

    return content

def parse_xml(content):
    e = ElementTree.parse(content)
    r = e.getroot()

    filenames = []
    for child in r:
        if child.tag[-8:] == 'Contents':
            for c in child:
                if c.tag[-3:] == 'Key':
                    filenames.append(c.text)

    return filenames

def get_files(filelist, save_path='', AWS_URL="https://s3.amazonaws.com/noaa-goes16/"):
    files = []
    for filename in filelist:
        content = requests.get(AWS_URL + filename)
        c = content.content
        name = os.path.basename(filename)
        print('Saving %s%s' % (save_path, name))
        f = open(save_path + name,'wb')
        f.write(c)
        f.close()
        files.append(save_path + name)

    return files


def example():
    xml = get_filenames('ABI-L1b-RadF', '2018', 1, 4)
    filenames = parse_xml(xml)
    files = get_files(filenames)
