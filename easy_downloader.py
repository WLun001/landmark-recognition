# Copy and Run code in your local machine with your own path. Images will not be resized. Resize later in the challenge part!
# Dataset has 1048575 images(~22GB) close and rerun code anytime to resume download


import numpy as np 
import pandas as pd 
import sys, requests, shutil, os
from urllib import request, error
# Input data files are available in the "./input/" directory.
print(os.listdir("./input"))
data=pd.read_csv('./input/train.csv')
data.head(5)

def fetch_image(path, dir_path):
    url=path
    response=requests.get(url, stream=True)
    with open(dir_path + '/image.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
links=data['url']
landmark_id=data['landmark_id']
i=0

for link in links:              #looping over links to get images
    if os.path.exists('./input/train/' + str(landmark_id[i])):
        i+=1
        continue
    dir_path = './input/train_images/' + str(landmark_id[i])
    if not os.path.exists(dir_path): 
    	os.makedirs(dir_path)
    fetch_image(link, dir_path)
    os.rename(dir_path + '/image.jpg', dir_path + '/' + str(landmark_id[i]) + '_' +str(i)+ '.jpg')
    print('Downloading ' + str(i) +  '/' + str(len(links)))
    i+=1
    if(i==5000):   #uncomment to test in your machine
        break
