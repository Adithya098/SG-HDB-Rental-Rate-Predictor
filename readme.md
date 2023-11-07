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
- c. ./data/eda: Contains code to perform the eda along with an ipynb which explains each step
  - EDA.ipynb: A ipynb notebook which explains the rationale behind every EDA step done for this project
  - process_coe_prices.py: A script which reads the coe_prices auxiliary dataset and extracts information from it as described in the get_economic_indicators_from_aux_data.ipynb notebook
  - process_stock_prices.py: A script which reads the stock_prices auxiliary dataset and extracts information from it as described in the get_economic_indicators_from_aux_data.ipynb notebook
  - process_location_info.py: A script which extracts the distances from each house to the nearest mrt, planned mrt, primary school and shopping mall by using the datasets in the auxiliary datasets.
  - process_town_importance.py: A script which computes the town_importance and town_centrality values using the datasets in './datasets/additional-town-centrality-data'.
  - process_main_dataset.py: A script which handles the cleaning and normalizing of all columns in the dataset.
  - process.py: An orchestrator script which combines all the eda steps defined in the other files mentioned above.
<br>

<b>2. ./datasets</b>: This only has the auxilary datasets folder but other folders can be created by running the process.py script mentioned above.
<br>
- a. ./datasets/auxiliary-data: Contains the auxiliary datasets which will have been downloaded from the kaggle link mentioned above
  - sg-coe-prices.csv: Downloaded dataset from kaggle which contains the 
  - sg-mrt-existing-stations.csv: Downloaded dataset from kaggle which contains information on the existing MRT stations in Singapore 
  - sg-mrt-planned-stations.csv: Downloaded dataset from kaggle which contains information on the future MRT stations which will be opened in Singapore 
  - sg-primary-schools.csv: Downloaded dataset from kaggle which contains information on the primary schools present in Singapore 
  - sg-shopping-malls.csv: Downloaded dataset from kaggle which contains information on the shopping malls present in Singapore
  - sg-stock-prices.csv: Downloaded dataset from kaggle which contains the stock price information for each company
<br>
- b. ./datasets/additional-town-centrality-data: These datasets were created manually by following the process described in "./data/eda/EDA.ipynb"
  - town_centroids_radius.csv: A small dataset which contains the centroid and radius information for each town
  - town_importance_centrality.csv: A small dataset which contains the town, its 'importance' (see EDA ipynb for what this means) and its page rank centrality.
<br>
- c. ./datasets/final: Will contain the final cleaned dataset after running the process.py script on the downloaded datasets
  - train_clean.csv: The final cleaned train data used for all the experiments and models.
  - test_clean.csv: The final cleaned test data used for all the experiments and models.
<br>
- d. train.csv: The original downloaded train dataset from the kaggle competition link mentioned above.
- e. test.csv: The original downloaded test dataset from the kaggle competition link mentioned above.
<br>

<b>3. ./experiments</b>: This folder contains ipynb notebooks for various model experiments conducted
- a. ./experiments/KNN: Regressor using the K-Nearest Neighbour model
  - knn.ipynb: ipynb file explaining how knn was used to predict the house rental prices
  - haversine-knn-submission.csv: submission file to kaggle using the custom KNN model which uses haversine distances
  - vanilla-knn-submission.csv: submission file to kaggle using the vanilla KNN model
<br>
- b. ./experiments/Neural Network: Regressor using Neural Networks model
  - neural_network.ipynb: ipynb file explaining how a neural networks based model was used to predict the house rental prices
  - neural_network_best_model-submission.csv: submission file to kaggle using the best trained neural networks model
<br>
- c. ./experiments/Regression: Using various SkLearn regressors
  - ./experiments/Regression/LinearRegression: Regressor using the Linear Regressor model
    - linear-regression.ipynb: ipynb file explaining how sklearn's linear regressor model was used to predict the house rental prices
    - linear-regression-submission.csv: submission file to kaggle using the linear regression model
  - ./experiments/Regression/PolynomialRegression: Regressor using the Polynomial Regressor model
    - polynomial_regression.ipynb: ipynb file explaining how sklearn's polynomial regressor model was used to predict the house rental prices
    - polynomial-regression-submission.csv: submission file to kaggle using the polynomial regression model
<br>
- d. ./experiments/SVM: Regressor using the Support Vector Model
  - svm.ipynb: ipynb file explaining how svm model was used to predict the house rental prices
  - svm-submission.csv: submission file to kaggle using the SVM model
<br>
- c. ./experiments/Trees: Using vairous Tree based regressors
  - ./experiments/Trees/DecisionTreeRegressor: Regressor using the Decision Tree Regressor model
    - decision_tree_regressor.ipynb: ipynb file explaining how decision tree regressor model was used to predict the house rental prices
    - decision-tree-submission.csv: submission file to kaggle using the decision tree regressor model
  - ./experiments/Trees/ExtraTreeRegressor: Regressor using the Extra Tree Regressor model
    - extra_tree_regressor.ipynb: ipynb file explaining how extra tree regressor model was used to predict the house rental prices
    - extra-tree-submission.csv: submission file to kaggle using the extra tree regressor model
  - ./experiments/Trees/RandomForestRegressor: Regressor using the Random Tree Regressor model
    - random_forest.ipynb: ipynb file explaining how random forest regressor model was used to predict the house rental prices
    - random-forest-submission.csv: submission file to kaggle using the random forest regressor model
  - ./experiments/Trees/XGBoostRegressor: Regressor using the XG-Boost Tree Regressor model 
    - xgboost_regressor.ipynb: ipynb file explaining how xgboost tree regressor model was used to predict the house rental prices
    - xgboost-submission.csv: submission file to kaggle using the xgboost regressor model
<br>
  
<b>4. ./resources</b>: Contains files which were either generated during analysis or referenced in other ipynb files
- a. ./resources/before_eda_analysis_reports/*: Contains the generated pandas profiling reports for all the original datasets which were helpful in coming up with the EDA steps performed in this project.
- b. ./resources/after_eda_analysis_report/*: Contains the generated pandas profiling report after cleaning the train dataset using the EDA steps
- c. ./resources/useful_pics/*: Contains pictures which are used across the various ipynb files
<br>

<b>5. ./utils</b>: Folder containing util code
- a. constants.py: defines constants which are used in the EDA process
- a. data_utils.py: defines modular functions for manipulating data which are used across the various scripts in the "./data/eda" folder
<br>
