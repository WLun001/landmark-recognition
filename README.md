# Landmark Recognition
Google Landmark Recognition Challenge 

## Explanation
- We use TensorFlow for image recognition. 
We will be using transfer learning, which means we are starting with a model that has been already trained on another problem. 
We will then be retraining it on a similar problem. 
Deep learning from scratch can take days, but transfer learning can be done in short order.
- [MoBileNet](https://research.googleblog.com/2017/06/mobilenets-open-source-models-for.html) will be used, to be small and efficient. 

## Get Started
- Follow tutorial from [codelabs](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets)
- After done the tutorial, replace the label.image.py from this respo to the cloned respo
- copy the run.py to cloned respo and run


## File Explanation
- easy_downloader_training.py for download images for training data
- easy_downloader_testing.py for download images for testing data
- label.image.py for image labelling and prediction
- run.py to run the prediction

## Full datasets
train: 336 GB with 1,220,165 images 
test: 34.9 GB with 116,163 images
