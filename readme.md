# <u>Home Sweet Home</u>

## <u>About this project</u>

This is the course project for CS5228 (Knowledge Discovery & Data Mining) @ NUS where the task is to predict the rental rates for HDB flats in Singapore.

## <u>Creating the cleaned datasets</u>

In the  folder called 'datasets' create the additional subfolders
1. auxiliary-data
2. final

Use this <a href="https://www.kaggle.com/competitions/cs5228-2310-final-project/data">kaggle competition link</a> to download the following data files:
1. train.csv and the test.csv files & place it in ./datasets
2. files under /auxiliary-dataset/* & place it in under ./datasets/auxiliary-data

Then run the script present in ./data/eda/process.py which will perform these <a href="https://github.com/ParasharaRamesh/Home-sweet-home/blob/main/data/eda/EDA.ipynb">EDA steps</a> in sequence to create the final cleaned datasets "train_clean.csv" & "test_clean.csv" which will be placed in the folder "./datasets/final".

These cleaned datasets were then used to train each regression model which can be found in the ./experiments folder.

## <u>Project Structure & Description</u>

<b>1 ./data</b> : Contains code related to loading/manipulating the dataset.
<br>
- a. ./data/analysis: TODO
<br>
- b. ./data/auxillary datasets: TODO
<br>
- c. ./data/eda: TODO
<br>

<b>2. ./datasets</b>: This is not present in the repo but can be created
- a. mention that this only has the additional town centrality details
<br>

<b>3. ./experiments</b>: This folder contains ipynb notebooks for various model experiments conducted
- a. TODO
<br>

<b>4. ./resources</b>: TODO
- a. TODO
<br>

<b>5. ./utils</b>: TODO
- a. TODO
<br>
