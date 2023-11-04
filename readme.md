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

## My Flow

* Recheck the existing code for coe -> create a neat ipynb (X)
* Recheck the existing code for distance -> create a neat ipynb (X)
* Recheck the approach for cleaning -> create a neat ipynb
- here wait for adi's input on flat type
- target encoding
- wait for importance scores
- do spearman


## <u> TODO </u>

1. Pending things to do in EDA: 
- Prof comments:
*  target encoding nominal attributes with a large number of values - basically imputation
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


DATASET EDA TO DO:


X:

Waiting:
town_importance = will be normalized
nearest_mrt_importance = will be normalized
flat_type =  ordinal - adi
flat_model = ordinal - adi

Done:

coe_price_indicator = already normalized X
stock_price = already normalized X
latitude  = nothing X 
longitude = nothing X
elevation = delete (same reason from ipynb)
furnished = delete (same reason from ipynb)
planning_area = delete (same reason from ipynb)
block = delete (not important as we have other details)
street_name = delete (too many to one hot encode)
subzone = delete (because most of the towns have this name)
rent_approval_date = unix time stamp -> normalize
region = one hot encoding
town = one hot encoding


TODO:


lease_commence_date = normalize
floor_area_sqm = normalize
distance_to_nearest_existing_mrt= normalize 
distance_to_nearest_planned_mrt = normalize 
distance_to_nearest_school      = normalize 
distance_to_nearest_mall        = normalize 

Y:

monthly_rent 

