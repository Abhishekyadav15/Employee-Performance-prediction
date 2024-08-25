# Machine Learning Approach for Employee Performance Prediction
The Machine Learning Approach for Employee Performance Prediction with a comprehensive system designed to analyze various data points related to employees' work performance and use machine learning algorithms, leveraging ML technology stack, to predict and evaluate their future performance. By incorporating factors such as past performance metrics, training data, feedback, and external factors, the system aims to provide insights that can aid in talent management, resource allocation, and workforce optimization strategies.

Scenario 1: Talent Retention
HR departments can use the machine learning predictions to identify high-performing employees at risk of attrition. By analyzing factors contributing to employee turnover and predicting performance trends, HR can implement targeted retention strategies, such as personalized career development plans or incentive programs, to retain top talent.

Scenario 2: Performance Improvement
Managers and team leaders can leverage the predictions to identify areas where employees may need additional support or training. By understanding performance patterns and potential challenges, managers can provide timely coaching, resources, or skill development opportunities to enhance employee performance and productivity.

Scenario 3: Resource Allocation
Organizations can optimize resource allocation by using machine learning predictions to match employees with projects or tasks that align with their strengths and capabilities. This ensures efficient utilization of talent, improves project outcomes, and enhances overall organizational performance.

# project structure
	
 ```project_folder/
├── app.py
├── model.pkl
├── requirements.txt
├── templates/
│   ├── home.html
│   ├── predict.html
│   └── result.html
└── static/
    ├── style.css
    └── images.png
```


# Productivity Prediction of Garment Employees : 
With the help of this dataset, we will predict the performance of employees based on the various parameter given in the dataset.

# Visualizing and analyzing the data
As the dataset is downloaded. Let us read and understand the data properly with the help of some visualization techniques and some analysing techniques.
Note: There are n number of techniques for understanding the data. But here we have used some of it. In an additional way, you can use multiple techniques.
### Importing the libraries
Import the necessary libraries such as pandas , matplotlib, seaborn , sklearn ,xgboost,pickle,labelEncoder.

### Read the Dataset
Our dataset format might be in .csv, excel files, .txt, .json, etc. We can read the dataset with the help of pandas.
In pandas we have a function called read_csv() to read the dataset. As a parameter we have to give the directory of csv file.

### Correlation analysis
In simple words, A correlation matrix is simply a table which displays the correlation coefficients for different variables. The matrix depicts the correlation between all the possible pairs of values in a table. It is a powerful tool to summarize a large dataset and to identify and visualize patterns in the given data.
### Descriptive analysis
Descriptive analysis is to study the basic features of data with the statistical process. Here pandas has a worthy function called describe. With this describe function we can understand the unique, top and frequent values of categorical features. And we can find mean, std, min, max and percentile values of continuous features.


# Data Pre-processing
As we have understood how the data is lets pre-process the collected data.

The download data set is not suitable for training the machine learning model as it might have so much of randomness so we need to clean the dataset properly in order to fetch good results. This activity includes the following steps.

### Handling missing values
For checking the null values, data.isnull() function is used. To sum those null values we use .sum() function to it. From the below image we found that in our dataset there is one feature which has high number of null values. So we drop that feature.


### Handling Date & department column
Here what we are doing is converting the date column into datetime format.
Then converting date column to month (month index) & transferring the values into a new column called month. As we have the month column now we don’t need date, so we will drop it.


### Handling categorical data
As we can see our dataset has categorical data we must convert the categorical data to integer encoding or binary encoding.
To convert the categorical features into numerical features we use encoding techniques. There are several techniques but in our project we are using LabelEncoder.


### Splitting dataset into training and test set
Now let’s split the Dataset into train and test sets. First split the dataset into x and y and then split the data set. After that x is converted into array format then passed into a new variable called X.
Here X and y variables are created. On X variable, data is passed with dropping the target variable. And on y target variable is passed. For splitting training and testing data we are using train_test_split() function from sklearn. As parameters, we are passing X, y, test_size, random_state.


# Model Building
Now our data is cleaned and it’s time to build the model. We can train our data on different algorithms. For this project we are applying three Regression algorithms. The best model is saved based on its performance.

## Linear Regression model
Linear Regression has been initialized with the name lr. Then predictions are taken from x_test given to a variable named pred_test. After that Mean absolute error, mean squared error & r2_scrores are obtained.

## Random Forest model
Random Forest has been initialized with the name rf. Then predictions are taken from x_test given to a variable named pred. After that Mean absolute error, mean squared error & r2_scrores are obtained.

## Xgboost model
XGBoost has been initialized with the name model_xgb. Then predictions are taken from x_test given to a variable named pred3. After that Mean absolute error, mean squared error & r2_scrores are obtained

## Compare the model
For comparing the above three models MSE, MAE & r2_scroes are used. 
After calling the function, the results of models are displayed as output. among the three model xgboost is performing well. 

# Application building
In this section, we will be building a web application that is integrated to the model we built. A UI is provided for the uses where he has to enter the values for predictions. The enter values are given to the saved model and prediction is showcased on the UI.

This section has the following tasks
Building HTML Pages
Building server side script

## Building Html Pages

### For this project create three HTML files namely

about.html
home.html
predict.html
submit.html

## Build Python code
Load the saved model. Importing flask module in the project is mandatory. An object of Flask class is our WSGI application. Flask constructor takes the name of the current module (__name__) as argument.

we will be using declared constructor to route to the HTML page which we have created earlier.

when the home page of the web server is opened in browser, the html page will be rendered. Whenever you enter the values from the html page the values can be retrieved using POST Method.

we are routing our app to pred () function. This function retrieves all the values from the HTML page using Post request. That is stored in an array. This array is passed to the model.predict() function. This function returns the prediction. And this prediction value will rendered to the text that we have mentioned in the home.html page earlier.

# Running the application

we run the application using following commond 

set flask_app = app.py

 flask run

# input and output
![Screenshot (307)](https://github.com/user-attachments/assets/422f70a0-0296-4d83-b563-8dab64baf4dd)
![Screenshot (308)](https://github.com/user-attachments/assets/d86bc7ff-3c76-4109-b2bc-0df236690a26)
![Screenshot (309)](https://github.com/user-attachments/assets/0ccb11ef-1df3-4a1b-b598-4d2ba3e60248)





 #  google cloud skillboost course badges

 ![Screenshot (306)](https://github.com/user-attachments/assets/b613657e-1284-4cd0-87ac-418d04271c46)
![Screenshot_20-8-2024_14417_www cloudskillsboost google](https://github.com/user-attachments/assets/1928451a-a9f0-4054-b2ca-2c12204d80ee)
![Screenshot_20-8-2024_143935_www cloudskillsboost google](https://github.com/user-attachments/assets/4abe3cdc-5d3f-404c-8186-66cb637418b2)



 


