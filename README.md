# udacity-data-scientist
[**Udacity Data Scientist NanoDegree Program**](https://www.udacity.com/course/data-scientist-nanodegree--nd025)

`Project 2- Disaster Response Pipeline Project`
## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [File Descriptions](#files)
4. [Instructions](#instructions)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Introduction <a name="introduction"></a>
This is the second project of the [**Udacity Data Scientist NanoDegree Program**](https://www.udacity.com/course/data-scientist-nanodegree--nd025).

For this project, I will analyze disaster data from [Appen](https://www.figure-eight.com/) to build a Natural Language Processing (NLP) model for an API that classifies disaster messages. 

The project contains three components:
1. ETL pipeline - process and clean the messages and categories datasets and store the clean data in a SQLite database
2. ML pipeline - a machine learning pipeline that categorizes disaster events and exports the final model as a pickle file
3. Flask Web App - a web app that displays visualizations of the data and gets classification results in several categories


## Installation <a name="installation"></a>
1. Mac or Windows System
2. [Anaconda Distribution](https://docs.anaconda.com/free/anaconda/index.html)
3. Python 3.5+
4. Libraries:
Numpy, Scipy, Pandas, Scikit-Learn, NLTP, SQLalchemy, Pickle, Flask, Plotly

## File Descriptions <a name="files"></a>
Here's the file structure of the project:
```bash
.
├── README.md
├── app
│   ├── run.py  # Flask file that runs app
│   └── templates
│       ├── go.html  # classification result page of web app
│       └── master.html  # main page of web app
├── data
│   ├── DisasterResponse.db   # database to save clean data to
│   ├── disaster_categories.csv  # data to process 
│   ├── disaster_messages.csv  # data to process 
│   └── process_data.py
├── models
│   ├── classifier.pkl  # saved model 
│   └── train_classifier.py
├── screenshots # results and running process
│   ├── evaluate_model.pdf  
│   ├── graph1.pdf
│   ├── graph2.pdf
│   ├── graph3.pdf
│   ├── model_result.pdf
│   └── train_model.pdf
└── workspace # jupyter notebooks for data analysis and further references
    ├── DisasterResponse.db
    ├── ETL Pipeline Preparation.html
    ├── ETL Pipeline Preparation.ipynb
    ├── ML Pipeline Preparation.html
    ├── ML Pipeline Preparation.ipynb
    ├── Twitter-sentiment-self-drive-DFE.csv
    ├── categories.csv
    └── messages.csv
```


## Instructions <a name='instructions'></a>
1. Run the following commands in the project's root directory to set up your database and model.

- To run ETL pipeline that cleans data and stores in database
  
    `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
  
- To run ML pipeline that trains classifier and saves
  
    `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.

    `python run.py`

4. Go to http://0.0.0.0:3001/


## Results<a name="results"></a>
The examples of the web page are in the **screenshot** folders. 

## Licensing, Authors, Acknowledgements<a name="licensing"></a>
This project is part of the Udacity Data Scientist Nano Degree Program, and I'm using data provided by Appen. :love_you_gesture:
