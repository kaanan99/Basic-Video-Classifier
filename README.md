# Basic Video Classifier
A basic video classifier that tries to detect human activities utilizing media pipe and an LSTM. Data is from the UCF11 data set which contains 11 classes of activities.

## Contents
`split_data.py`: Python script for splitting the data into training (60%), validation (20%), and testing splits (20%).
`video_predictor.ipynb`: Notebook for training the model and evaluating

# How to run

## Install dependencies
```
pip install -r requirements.txt
```

## Download data
After cloning the repository, download UCF11 from https://www.crcv.ucf.edu/data/UCF_YouTube_Action.php. Move the rar file into the repository and extract it.

## Order of running
1. Run `split_data.py` to split the data into training, validation, and testing splits
2. Run `video_predictor.ipynb` to run and evaluate the model.
