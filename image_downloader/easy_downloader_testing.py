# Copy and Run code in your local machine with your own path. Images will not be resized. Resize later in the challenge part!
# Dataset has 1048575 images(~22GB) close and rerun code anytime to resume download


import numpy as np 
import pandas as pd 
import sys, requests, shutil, os
from urllib import request, error
# Input data files are available in the "./input/" directory.
print(os.listdir("./input"))
data=pd.read_csv('./input/test.csv')
data.head(5)

def fetch_image(path, dir_path):
    url=path
    response=requests.get(url, stream=True)
    with open(dir_path + '/image.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
links=data['url']
id=data['id']
i=0

# seperate images into follwing format
# image name = id.jpg
for link in links:              #looping over links to get images
    dir_path = './input/test_images/'
    if not os.path.exists(dir_path): 
    	os.makedirs(dir_path)
    fetch_image(link, dir_path)
    os.rename(dir_path + '/image.jpg', dir_path + '/' +  str(id[i]) + '.jpg')
    print('Downloading ' + str(i) +  '/' + str(len(links)))
    i+=1
    if(i==500):   #uncomment to test in your machine
        break
