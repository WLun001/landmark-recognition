# -*- coding: utf-8 -*-

# !/usr/bin/python

# Note to Kagglers: This script will not run directly in Kaggle kernels. You
# need to download it and run it on your local machine.

# Downloads images from the Google Landmarks dataset using multiple threads.
# Images that already exist will not be downloaded again, so the script can
# resume a partially completed download. All images will be saved in the JPG
# format with 90% compression quality.

import sys, os, multiprocessing, csv
from urllib import request, error
from PIL import Image
from io import BytesIO


def parse_data(data_file):
    csvfile = open(data_file, 'r')
    csvreader = csv.reader(csvfile)
    data_list = [line[:] for line in csvreader]
    return data_list[1:]  # Chop off header


def download_image(data_list):
    out_dir = sys.argv[2]
    (key, url, landmark) = data_list
    dir_path = out_dir + str(landmark)
    if not os.path.exists(dir_path): 
    	os.makedirs(dir_path)
    filename = os.path.join(dir_path, '{}.jpg'.format(key))

    if os.path.exists(filename):
        print('Image {} already exists. Skipping download.'.format(filename))
        return

    try:
        response = request.urlopen(url)
        image_data = response.read()
    except:
        print('Warning: Could not download image {} from {}'.format(key, url))
        return

    try:
        pil_image = Image.open(BytesIO(image_data))
    except:
        print('Warning: Failed to parse image {}'.format(key))
        return

    try:
        pil_image_rgb = pil_image.convert('RGB')
    except:
        print('Warning: Failed to convert image {} to RGB'.format(key))
        return

    try:
        pil_image_rgb.save(filename, format='JPEG', quality=2)
    except:
        print('Warning: Failed to save image {}'.format(filename))
        return


def loader():
    if len(sys.argv) != 3:
        print('Syntax: {} <data_file.csv> <output_dir/>'.format(sys.argv[0]))
        sys.exit(0)
    (data_file, out_dir) = sys.argv[1:]

    if not os.path.exists(out_dir):
        os.mkdir(out_dir)

    data_list = parse_data(data_file)
    pool = multiprocessing.Pool(processes=4)  # Num of CPUs
    pool.map(download_image, data_list)
    pool.close()
    pool.terminate()


# arg1 : data_file.csv
# arg2 : output_dir
if __name__ == '__main__':
    loader()
