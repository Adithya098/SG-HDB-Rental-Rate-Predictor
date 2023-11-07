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

<b>1 ./data</b> : Contains code related to analyzing the various datasets along with code to perform EDA steps on each dataset.
<br>
- a. ./data/analysis: Contains ipynb files which contain analyze the train dataset before and after EDA
  - report_profile_generation_before_EDA.ipynb: Generates pandas profiling reports for all the provided datasets. These generated reports can be found under ./resources/before_eda_analysis_reports. These reports helped us in understanding the datasets much better in order to come up with EDA steps.
  - report_profile_generation_before_EDA.ipynb: Generates pandas profiling reports for the final cleaned train dataset after EDA. These generated reports can be found under ./resources/after_eda_analysis_report.
<br>
- b. ./data/auxiliary datasets: Contains ipynb files which analyze the given auxilary datasets and what EDA steps can be performed on them.
  - get_economic_indicators_from_aux_data.ipynb: Analyses the EDA steps which can be done on the sg-coe-prices & sg-stock-prices datasets.
  - get_location_distances_from_aux_data.ipynb: Analyses the EDA steps which can be done on the sg-mrt-existing-stations & sg-mrt-planned-stations datasets.
<br>
- c. ./data/eda: 
  - EDA.ipynb: 
  - process_coe_prices.py: 
  - process_stock_prices.py: 
  - process_location_info.py:
  - process_town_importance.py: 
  - process_main_dataset.py: 
  - process.py: 
<br>

<b>2. ./datasets</b>: This only has the auxilary datasets folder but other folders can be created by running the process.py script mentioned above.
<br>
- a. ./datasets/auxiliary-data: Contains the auxiliary datasets which will have been downloaded from the kaggle link mentioned above
  - sg-coe-prices.csv: 
  - sg-mrt-existing-stations.csv: 
  - sg-mrt-planned-stations.csv: 
  - sg-primary-schools.csv: 
  - sg-shopping-malls.csv:
  - sg-stock-prices.csv:
<br>
- b. ./datasets/additional-town-centrality-data: 
  - town_centroids_radius.csv: 
  - town_importance_centrality.csv: 
<br>
- c. ./datasets/final: Will contain the final cleaned dataset after running the process.py script on the downloaded datasets
  - train_clean.csv: The final cleaned train data used for all the experiments and models.
  - test_clean.csv: The final cleaned test data used for all the experiments and models.
<br>
- d. train.csv: The original downloaded train dataset from the kaggle competition link mentioned above.
- e. test.csv: The original downloaded test dataset from the kaggle competition link mentioned above.
<br>

<b>3. ./experiments</b>: This folder contains ipynb notebooks for various model experiments conducted
- a. ./experiments/KNN: 
  - knn.ipynb:
  - haversine-knn-submission.csv:
  - vanilla-knn-submission.csv:
<br>
- b. ./experiments/Neural Network: 
  - neural_network.ipynb: 
  - neural_network_best_model-submission.csv: 
<br>
- c. ./experiments/Regression: 
  - ./experiments/Regression/LinearRegression:
    - linear-regression.ipynb:
    - linear-regression-submission.csv:
  - ./experiments/Regression/PolynomialRegression: 
    - polynomial_regression.ipynb:
    - polynomial-regression-submission.csv:
<br>
- d. ./experiments/SVM: 
  - svm.ipynb:
  - svm-submission.csv:
<br>
- c. ./experiments/Trees: 
  - ./experiments/Trees/DecisionTreeRegressor:
    - decision_tree_regressor.ipynb:
    - decision-tree-submission.csv:
  - ./experiments/Trees/ExtraTreeRegressor: 
    - extra_tree_regressor.ipynb:
    - extra-tree-submission.csv:
  - ./experiments/Trees/RandomForestRegressor:
    - random_forest.ipynb:
    - random-forest-submission.csv:
  - ./experiments/Trees/XGBoostRegressor: 
    - xgboost_regressor.ipynb:
    - xgboost-submission.csv:
<br>
  
<b>4. ./resources</b>: TODO
- a. ./resources/before_eda_analysis_reports/*
- b. ./resources/after_eda_analysis_report/*
- c. ./resources/useful_pics/*
<br>

<b>5. ./utils</b>: TODO
- a. constants.py
- a. data_utils.py
<br>
