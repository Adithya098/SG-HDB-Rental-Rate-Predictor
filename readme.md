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

**1. ./data**: Contains code related to analyzing the datasets and performing EDA steps.

- **a. ./data/analysis**: Contains IPython notebooks for analyzing the train dataset before and after EDA.
  - `report_profile_generation_before_EDA.ipynb`: Generates pandas profiling reports for the provided datasets, stored under ./resources/before_eda_analysis_reports. These reports aid in understanding the datasets for EDA planning.
  - `report_profile_generation_after_EDA.ipynb`: Generates pandas profiling reports for the final cleaned train dataset after EDA, saved under ./resources/after_eda_analysis_report.

- **b. ./data/auxiliary datasets**: Contains IPython notebooks for analyzing auxiliary datasets.
  - `get_economic_indicators_from_aux_data.ipynb`: Analyzes the sg-coe-prices & sg-stock-prices datasets.
  - `get_location_distances_from_aux_data.ipynb`: Analyzes the sg-mrt-existing-stations & sg-mrt-planned-stations datasets.

- **c. ./data/eda**: Contains code to perform EDA, along with an IPython notebook explaining each step.
  - `EDA.ipynb`: An IPython notebook explaining the rationale behind every EDA step.
  - `process_coe_prices.py`: Extracts information from the coe_prices auxiliary dataset.
  - `process_stock_prices.py`: Extracts information from the stock_prices auxiliary dataset.
  - `process_location_info.py`: Computes distances from each house to the nearest MRT, planned MRT, primary school, and shopping mall.
  - `process_town_importance.py`: Computes town_importance and town_centrality values using datasets in './datasets/additional-town-centrality-data'.
  - `process_main_dataset.py`: Handles the cleaning and normalizing of all columns in the dataset.
  - `process.py`: Orchestrates the EDA steps defined in the other files mentioned above.

**2. ./datasets**: Contains auxiliary datasets and will also contain the final cleaned dataset after running 'process.py'.

- **a. ./datasets/auxiliary-data**: Contains auxiliary datasets downloaded from Kaggle.
  - `sg-coe-prices.csv`: Contains COE prices data.
  - `sg-mrt-existing-stations.csv`: Contains information on existing MRT stations in Singapore.
  - `sg-mrt-planned-stations.csv`: Contains information on planned MRT stations in Singapore.
  - `sg-primary-schools.csv`: Contains information on primary schools in Singapore.
  - `sg-shopping-malls.csv`: Contains information on shopping malls in Singapore.
  - `sg-stock-prices.csv`: Contains stock price information for each company.

- **b. ./datasets/additional-town-centrality-data**: Manually created datasets following the process described in "./data/eda/EDA.ipynb".
  - `town_centroids_radius.csv`: Contains centroid and radius information for each town.
  - `town_importance_centrality.csv`: Contains town importance and centrality values.

- **c. ./datasets/final**: Will contain the final cleaned dataset after running 'process.py'.
  - `train_clean.csv`: The final cleaned train data used for all experiments and models.
  - `test_clean.csv`: The final cleaned test data used for all experiments and models.

- `train.csv`: The original downloaded train dataset from Kaggle.
- `test.csv`: The original downloaded test dataset from Kaggle.

**3. ./experiments**: Contains IPython notebooks for various model experiments conducted.

- **a. ./experiments/KNN**: Regressor using the K-Nearest Neighbor model.
  - `knn.ipynb`: Explains how KNN was used to predict house rental prices.
  - `haversine-knn-submission.csv`: Submission file to Kaggle using a custom KNN model with haversine distances.
  - `vanilla-knn-submission.csv`: Submission file to Kaggle using the vanilla KNN model.

- **b. ./experiments/Neural Network**: Regressor using a Neural Networks model.
  - `neural_network.ipynb`: Explains how a neural networks-based model was used to predict house rental prices.
  - `neural_network_best_model-submission.csv`: Submission file to Kaggle using the best-trained neural networks model.

- **c. ./experiments/Regression**: Using various SkLearn regressors.
  - **./experiments/Regression/LinearRegression**: Regressor using the Linear Regressor model.
    - `linear-regression.ipynb`: Explains how sklearn's linear regressor model was used to predict house rental prices.
    - `linear-regression-submission.csv`: Submission file to Kaggle using the linear regression model.

  - **./experiments/Regression/PolynomialRegression**: Regressor using the Polynomial Regressor model.
    - `polynomial_regression.ipynb`: Explains how sklearn's polynomial regressor model was used to predict house rental prices.
    - `polynomial-regression-submission.csv`: Submission file to Kaggle using the polynomial regression model.

- **d. ./experiments/SVM**: Regressor using the Support Vector Model.
  - `svm.ipynb`: Explains how the SVM model was used to predict house rental prices.
  - `svm-submission.csv`: Submission file to Kaggle using the SVM model.

- **e. ./experiments/Trees**: Using various Tree-based regressors.
  - **./experiments/Trees/DecisionTreeRegressor**: Regressor using the Decision Tree Regressor model.
    - `decision_tree_regressor.ipynb`: Explains how the decision tree regressor model was used to predict house rental prices.
    - `decision-tree-submission.csv`: Submission file to Kaggle using the decision tree regressor model.

  - **./experiments/Trees/ExtraTreeRegressor**: Regressor using the Extra Tree Regressor model.
    - `extra_tree_regressor.ipynb`: Explains how the extra tree regressor model was used to predict house rental prices.
    - `extra-tree-submission.csv`: Submission file to Kaggle using the extra tree regressor model.

  - **./experiments/Trees/RandomForestRegressor**: Regressor using the Random Tree Regressor model.
    - `random_forest.ipynb`: Explains how the random forest regressor model was used to predict house rental prices.
    - `random-forest-submission.csv`: Submission file to Kaggle using the random forest regressor model.

  - **./experiments/Trees/XGBoostRegressor**: Regressor using the XG-Boost Tree Regressor model.
    - `xgboost_regressor.ipynb`: Explains how the XGBoost tree regressor model was used to predict house rental prices.
    - `xgboost-submission.csv`: Submission file to Kaggle using the XGBoost regressor model.

**4. ./resources**: Contains files generated during analysis or referenced in other IPython notebooks.

- **a. ./resources/before_eda_analysis_reports/**: Contains generated pandas profiling reports for the original datasets, aiding in EDA planning.

- **b. ./resources/after_eda_analysis_report/**: Contains the generated pandas profiling report after cleaning the train dataset using EDA steps.

- **c. ./resources/useful_pics/**: Contains pictures used across the various IPython notebooks.

**5. ./utils**: Folder containing util code.

- `constants.py`: Defines constants used in the EDA process.

- `data_utils.py`: Defines modular functions for manipulating data used across the various scripts in the "./data/eda" folder.

**6. report.pdf**: The report describing project