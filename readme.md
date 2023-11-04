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

Adithya
* Create a new branch from main called 'feature/tree'
* In /experiments create a new directory called 'tree-based-models' and make it a python module by having an empty __init__.py file.
* Create an ipynb notebook which evaluates the following models(the ipynb should be readable like a story - you can refer to the EDA ipynb, so that the thought process is clear):
  - Decision-Tree Regressor 
  - XGBoost Regressor 
  - AdaBoost Regressor 
  - Any other XG (Gradient) based Regressors recommended by ChatGPT 
* For each model, use GridSearchCV to find the best hyperparameters
* For each model there should be a csv output file, which should be directly uploaded on Kaggle.
*  save_test_predictions_in_kaggle_format() - Use this function to save each model's output csv files and keep it handy/committed on git

Parashara
* Use the new cleaned dataset to run vanilla KNN and fix Haversine-KNN's C-Python error
* Verify and Merge everyone's code
* Add a comprehensive readme file which introduces the structure of project, folder, ipynb, and links to ipynbs


Poornima
* Create a new branch from main called 'feature/others'
* In /experiments create a new directory called 'tree-based-models' and make it a python module by having an empty __init__.py file.
* Create an ipynb notebook which evaluates the following models(the ipynb should be readable like a story - you can refer to the EDA ipynb, so that the thought process and code is clear, which makes it easier to prepare final report):
  - Linear Regression 
  - SVM Regressor (use different kernels and read more about RBF Kernels) 
  - Any other Regressors recommended by ChatGPT which has not been covered by our team yet
* For each model, use GridSearchCV to find the best hyperparameters
* For each model there should be a csv output file, which should be directly uploaded on Kaggle.
*  save_test_predictions_in_kaggle_format() - Use this function to save each model's output csv files and keep it handy/committed on git

Sriram
* Story-telling for "X-factor" in the EDA notebook + accommodate normalization of ordinal columns in this notebook
* In data/analysis, create a new ipynb notebook, called Dataset_Analysis_After_EDA
  - Generate report using Pandas Profiling
  - Spearman code
  - in EDA notebook, make a reference to these analysis notebooks
* Add any pics I use under "resources"
* Build an NN - usual stuff - dropout, weight decay, lr etc

Note For Team:
* We will try to finish by Sunday 8pm and have a call to discuss the template for final report - 8 pages

