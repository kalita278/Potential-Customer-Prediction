# Potential-Customer-Prediction

**DOMAIN:** Banking, Marketing

**CONTEXT:** A bank X is on a massive digital transformation for all its departments. Bank has a growing customer base whee majority of them are liability customers (depositors) vs borrowers (asset customers). The bank is interested in expanding the borrowers base rapidly to bring in more business  via  loan  interests.  A  campaign  that  the  bank  ran  in  last  quarter  showed  an  average  single  digit  conversion  rate.  Digital  transformation being  the  core  strength  of  the  business  strategy,  marketing  department  wants  to  devise  effective  campaigns  with  better  target  marketing  to increase the conversion ratio to double digit with same budget as per last campaign. 

**DATA DICTIONARY:**

1. **ID:** Customer ID
2. **Age:** Customer’s approximate age.
3. **CustomerSince:** Customer of the bank since. [unit is masked]
4. **HighestSpend:** Customer’s highest spend so far in one transaction. [unit is masked]
5. **ZipCode:** Customer’s zip code.
6. **HiddenScore:** A score associated to the customer which is masked by the bank as an IP.
7. **MonthlyAverageSpend:** Customer’s monthly average spend so far. [unit is masked]
8. **Level:** A level associated to the customer which is masked by the bank as an IP.
9. **Mortgage:** Customer’s mortgage. [unit is masked]
10. **Security:** Customer’s security asset with the bank. [unit is masked]
11. **FixedDepositAccount:** Customer’s fixed deposit account with the bank. [unit is masked]
12. **InternetBanking:** if the customer uses internet banking.
13. **CreditCard:** if the customer uses bank’s credit card.
14. **LoanOnCard:** if the customer has a loan on credit card.

**PROJECT  OBJECTIVE:** Build  a  Machine  Learning  model  to  perform  focused  marketing  by  predicting  the  potential  customers  who  will  convert using the historical dataset.


**DATA EXPLORATION AND DATA CLEANING:**

Combined the two files to create a single file with all the relevant variables and perform the necessary data quality checks and cleaning. In data cleaning, identified the missing values/unexpected values in the dataset and since the percentage of missing values is very less, dropped the null values. Also, identified the outliers in the dataset and impute that with the mean value. Also, make sure that the data types of the variables are appropriate as required for our analysis (Here, converted all the categorical variable data types to category and continuous variable data types to int or float).

**DATA ANALYSIS:**

Checked the distribution of data for the continuous (histogram charts) and categorical (pie charts) variables along with the target variable (pie charts). Performed uni-variate, bivariate, and multivariate analysis of the dataset, for example, 5-point summary of the continuous variable, pair plot, correlation matrix plot, and boxplot to detect outliers.

**DATA PREPROCESSING:**

Here, removed the unwanted/irrelevant independent variable/feature based on the above analysis from the dataset. Also, encoded the categorical variable using one-hot encoding and scaled the independent variable using standard scaler. Since the dataset is unbalanced, used SMOTE to balance the dataset.

**MODEL BUILDING, EVALUATION AND IMPROVEMENT:**

Used k nearest neighbour, logistic regression and support vector machine (SVM) algorithm to predict the potential customer and evaluate the model using confusion metrix, accuracy score, recall score, precision score and f1 score. Further tunned the models using GridsearchCV and compared all the models to find the best model.

**Finalize Support vector machine as the final model and achieved an accuracy of 95.02%.**

**MODEL DEPLOYMENT:**

Created a web app using pickle (used to save and load the model) and streamlit (used o create the web app) to predict the potential customer. (refer to "potential_customer_prediction_web_app.py" file)


