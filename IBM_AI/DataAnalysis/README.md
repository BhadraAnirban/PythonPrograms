Python Libraries
1. NumPy

NumPy (Numerical Python) is the foundation for scientific computing in Python. It provides fast and efficient multidimensional arrays and mathematical functions for performing numerical operations. Data scientists use NumPy for matrix computations, linear algebra, statistical calculations, and handling large datasets efficiently.

2. Pandas

Pandas is a powerful library for data manipulation and analysis. It introduces data structures such as Series and DataFrames, which make it easy to organize, clean, filter, transform, and analyze structured data. Pandas is widely used for reading data from CSV, Excel, databases, and other sources.

3. Scikit-learn

Scikit-learn is a machine learning library that provides simple tools for building predictive models. It includes algorithms for classification, regression, clustering, dimensionality reduction, and model evaluation. It is commonly used to develop and test machine learning solutions.

**Importing Data Sets**
<u>Learn how to understand dataset characteristics</u>

This involves examining the structure of a dataset, including the number of rows and columns, data types, distributions, missing values, and relationships among variables.

<u>Get an overview of Python packages for analyzing data</u>

Students learn the purpose and use of key libraries such as NumPy, Pandas, Matplotlib, Seaborn, and Scikit-learn for data analysis and visualization.

<u>Learn how to import data and start analyzing it</u>

This covers loading data from various sources such as CSV, Excel, databases, and APIs into Python for further processing and exploration.

**Data Wrangling**
<u>Data Wrangling</u>

Data wrangling is the process of transforming raw data into a clean and usable format for analysis.

<u>Pre-processing</u>

Pre-processing involves preparing data by removing errors, handling inconsistencies, and transforming features to improve analysis or model performance.

<u>Dealing with Missing Values</u>

Missing values can affect analysis accuracy. Common techniques include removing records, replacing missing values with averages, medians, or using advanced imputation methods.

<u>Formatting and Normalization of Your Data</u>

Formatting ensures data types are correct, while normalization scales numerical values to a common range, improving model performance and comparability.

**Exploratory Data Analysis (EDA)**
<u>Exploratory Data Analysis</u>

EDA is the process of investigating datasets to discover patterns, trends, anomalies, and relationships before building models.

<u>Descriptive Statistics</u>

Descriptive statistics summarize data using measures such as mean, median, mode, standard deviation, minimum, and maximum values.

<u>GroupBy</u>

The GroupBy operation in Pandas splits data into groups based on categories and performs aggregations such as sum, average, count, or maximum on each group.

<u>Correlation and Other Important Statistics</u>

Correlation measures the strength and direction of relationships between variables. Other statistical measures help understand variability, significance, and data distribution.

**Model Development**
<u>Linear Regression</u>

A supervised learning technique used to predict continuous values by establishing a linear relationship between input variables and the target variable.

<u>Model Evaluation</u>

Model evaluation assesses how well a machine learning model performs using metrics such as accuracy, precision, recall, RMSE, and R² score.

<u>Polynomial Regression and Pipelines</u>

Polynomial regression extends linear regression to capture non-linear relationships. Pipelines automate preprocessing and model-building steps into a single workflow.

<u>Measures for In-Sample Evaluation</u>

These metrics evaluate model performance on training data to determine how well the model fits the observed data.

<u>Prediction and Decision Making</u>

Once trained, models can predict future outcomes and support informed business or scientific decisions based on data-driven insights.

**Model Evaluation**
<u>Model Evaluation and Refinement</u>

This involves testing, tuning, and improving machine learning models to achieve better accuracy and generalization.

<u>Overfitting</u>

Overfitting occurs when a model learns training data too closely, including noise, resulting in poor performance on new data.

<u>Underfitting</u>

Underfitting happens when a model is too simple to capture underlying patterns in the data, leading to poor performance on both training and testing data.

<u>Model Selection</u>

Model selection is the process of choosing the best algorithm or model based on performance metrics and project requirements.

<u>Ridge Regression</u>

Ridge Regression is a regularized version of linear regression that reduces overfitting by adding a penalty term to large coefficient values.

<u>Grid Search</u>

Grid Search is a technique for finding the optimal hyperparameters of a machine learning model by systematically testing different parameter combinations.

Data Analysis flow ----
Data Source
     │
     ▼
  Pandas
(Data Cleaning & Preparation)
     │
     ▼
   NumPy
(Arrays & Numerical Operations)
     │
     ▼
   SciPy
(Scientific Computing Functions)
     │
     ▼
Scikit-learn
(Machine Learning Algorithms)
     │
     ▼
Matplotlib / Seaborn
(Visualization)

Pandas

Purpose: Data manipulation and analysis.
 Pandas provides DataFrames and Series, making it easy to load, clean, filter, transform, and analyze structured data from sources such as CSV, Excel, and databases.

NumPy

Purpose: Numerical computing.
 NumPy offers fast multidimensional arrays and mathematical functions for performing calculations, matrix operations, statistical analysis, and scientific computing efficiently.

Matplotlib

Purpose: Data visualization.
 Matplotlib is used to create charts and graphs such as line plots, bar charts, histograms, and scatter plots, helping analysts visualize trends and patterns in data.

Seaborn

Purpose: Statistical data visualization.
 Built on top of Matplotlib, Seaborn provides attractive and informative visualizations with less code. It is particularly useful for creating heatmaps, distribution plots, box plots, and correlation analysis charts.