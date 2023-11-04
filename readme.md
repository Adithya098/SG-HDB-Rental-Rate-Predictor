# <u>Home Sweet Home</u>

## <u>About this project</u>

This is the course project for CS5228 (Knowledge Discovery & Data Mining) @ NUS where the task is to predict the rental rates for HDB flats in Singapore.


## <u>Project Structure</u>

<b>1 ./config</b> : Contains yaml files/json files with hyperparameters for each specific experiment
<br>
<b>2 ./data</b> : Contains code related to loading/manipulating the dataset.
<br>
<b>5 ./experiments</b> : Contains ipynb files for showcasing each model experiment
<br>
<b>3 ./models</b> : For every experiment is a python package(i.e. directory with a init.py file) and contains the specific architectures needed
<br>
<b>4. ./resources: For storing graphs, visualizations and outputs from experiments in its respective folder.
<br>
<b>5 ./scripts</b> : Contains generic scripts for training, testing and visualizations.
<br>
<b>6 ./utils</b> : Contains util functions needed throughout the project (e.g. manipulating google drive from colab/matplotlib code)
<br>

## <u> TODO </u>

1. Pending things to do in EDA: 
- Prof comments:
*  target encoding nominal attributes with a large number of values - Adi will look into this
- Review existing code
- check haversine implementation again
* EDA flow  - normalization -> sklearn min-max?
- look at ordinal type for flat type
- redo the ipynb with step by step explanation for each eda step (X)
- recheck the report generation after eda
- Reformat the "Are Economic Indicators even useful" ipynb into "what columns are useful" using spearman 

2. Find importance of an area or town using Page Rank centrality:
- We are doing two approaches town wise importance, importance to nearest entity

3. Train KNN with new dataset -> vanilla & haversine
4. Train Neural Network with dataset
5. Write TODOs for other teammates
