# Moneyball in NBA: Predicting NBA player salary

![Insert Cover Photo]()

## Table of Contents
1. [Introduction](#introduction)
    - [Background](#background)
    - [Data](#data)
        - [Web scrapping](#web-scrapping)
        - [Joining datasets and cleaning](#Joining-datasets-and-cleaning)


2. [Exploratory Data Analysis](#exploratory-data-analysis)
    - [Average Salary Overtime](#average-salary-overtime)
    - [Feature Engineering](#feature-engineering)
    - [Salary Distribution](#salary-distribution)
    - [Correlation](#correlation)

3. [Prediction](#prediction)
    - [Baseline Model](#)
    - [Model Selection](#)
    - [Feature Selection](#)
    - [Dataset Selection](#)
    - [Hyperparameter Tuning](#)
    - [Other attempts to improve prediction](#)
    - [Best Model](#)
        - [Evaluation](#)
        - [Underrated & Overrated Players](#)
4. [Conclusion](#conclusion)
    * [Future works](#future-works)
- [Built with](#built-with)
- [Author](#author)

---

## Introduction

### Background

![Basketball Image]()

### Data

#### Web scrapping

I've scraped my dataset from 2 websites using Python's BeautifulSoup library.

- https://www.basketball-reference.com (For stats)
- https://hoopshype.com/salaries (For salary)

Basketball reference had statistics of every NBA player in a given year. There were 28 different features that included, points perg game, games played, position, age, field goal percentage, and etc.

Hoopshype had a table of every NBA player's salary in a given year. 

I've also extracted the salary cap of each year from basketball reference's [page](https://www.basketball-reference.com/contracts/salary-cap-history.html). Salary cap is the amount of money each team can spend on their entire roster for that given year.


You can find the code I used for web scrapping [here](Insertcodelink).  



#### Joining datasets and cleaning

I've joined the 2 datasets on player's name. 

In order to join properly, I've cleaned the names from both sources so that it would be as consistent as possible (So that it would join as much as possible)


Some steps I took to clean the names:
- Converted special characters to normal english characters. (Eg. 'Žižić' to 'Zizic')
- Removed: 
    - 'Jr.'
    - 'III'
    - periods
    - spaces
    - '*' (labeled for hall of fame players in basketball reference)

However, since the 2 sources had different names for some players, (Eg. Lou Williams vs Louis Williams) I could not join on all players. 

On the training set, 370 players (4.2% of data) failed to join. I've decided to drop them from my training model.

On the test set, I had 12 players (2.3% of data) that failed to join. Since the count was low, I've decided to manually input the salary so I can predict all the players in the test set.


I've created an `id` column with '`Player name` + `year`' for each entry.

All the columns in my dataset were strings so I converted them to number format. For `Salary` and `SalaryCap`, I had to replace the commas and dollar sign to convert to numbers. 

Some players were registered for multiple positions (Eg. SF-SG, PG-SG, etc.). I convereted them to their primary position which was the first entry (Eg. If 'SF-SG', primary position is 'SF').

I've ended up with 9310 rows and 33 columns after cleaning my dataset.
- **Train Set: 2000-2018 Seasons (8780 rows, 33 columns)**
- **Test Set: 2019 Season (530 rows, 33 columns)**


---

## Exploratory Data Analysis

### Average Salary Overtime

While exploring the data, I quickly realized that the average salary and the salary cap had been steadily increasing over time. I observed a huge increase spike in salary cap in 2017 when the NBA decided to increase the salary cap from about $70M to $94M. This was the year when the Golden State Warriors were able to [acquire Kevin Durant](https://www.espn.com/nba/story/_/id/16759826/kevin-durant-announces-sign-golden-state-warriors) in free agency with the additional cap space. 


This could have an effect in my prediction if I don't make any adjustments. 

![Salary cap](img/salarycap.png)

### Feature Engineering

I decided to normalize my salary so that it would be based off of the percentage of that year's salary cap. After normalization, the salary resembled more of a uniform distribution.

![Normalized Salary](img/normalizedsalary.png)


### Salary Distribution

I plotted the normalized salary distribution, but I couldn't observe any anomalies for each year. A large portion of the player's salary were in between 0.0 and 0.1 of the salary cap.

![Salary Distribution](img/salarydistribution.png)

### Correlation

I checked which variables had a positive correlation to salary using Pearson's method. The results are shown below indicating field goals per game as the highest correlation. Many of the positive correlations were related to scoring. I can keep these in my mind when I conduct feature selections on my predictions.

**Correlation with >= 0.5**

| Positive                             | Correlation |
| ------------------------------------ | ----------- |
| Field Goals Per Game                 | 0.61        |
| Points Per Game                      | 0.60        |
| 2-Point Field Goals Per Game         | 0.60        |
| 2-Point Field Goal Attempts Per Game | 0.60        |
| Field Goal Attempts Per Game         | 0.59        |
| Minutes Played Per Game              | 0.58        |
| Free Throw Attempts Per Game         | 0.58        |
| Free Throws Per Game                 | 0.57        |
| Defensive Rebounds Per Game          | 0.56        |
| Turnovers Per Game                   | 0.55        |
| Games Started                        | 0.52        |
| Total Rebounds Per Game              | 0.52        |

![](img/correlations.png)

---

## Prediction

I scored my predictions based on root mean squared error (RMSE). 

### Baseline Model

I started off my prediction with a baseline model using the average salary from my training set (2000-2018 seasons) to predict every player's 2019  NBA salary. With this baseline model, I got a RMSE of **0.0784**. 

The salary cap for the 2019 season was $101.9M so this RMSE would be equivalent to about $8M in error per prediction.

Based on the residual plot, I was over overpredicting many of the low paid players by 0.08 and underpredicting the top players. This does align with the distriubution of the player's salary.

![Base model residual plot](img/basemodel_residual.png)

### Model Selection

My first step in improving the RMSE was choosing the prediction model. I've tested using all variables with default parameters for 5 different models; Linear Regression, Random Forest, Gradient Boosting, Ada Boost, and XG Boost. 

I decided to proceed with Gradient Boosting since it consistently performed the best out of the 5 with a RMSE of **0.04681**. 

![model results](img/modelselection.png)

### Feature Selection

For feature selection, I tested out various combinations based off of the feature importance. After many trials and errors (testing with positive correlation features as well), my predictions were consistently performing the best with 6 features; Age, games played, total rebounds per game, minutes played per game, free throw attempts per game, and year. 

I decided to proceed with these 6 variables that lowered my RMSE to **0.04653**.

![](img/featureimportance.png)

*I've saved my predictions results with different features in the `prediction results` file for reference.

### Dataset Selection



### Hyperparameter Tuning

### Other attempts to improve prediction

### Best Model
- Evaluation
- Underrated & Overrated Players

---

## Conclusion

### Take Away


### Future works


---


## Built With

* **Software Packages:**  [Python](https://www.python.org/),  [Pandas](https://pandas.pydata.org/docs/), [Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Scipy](https://docs.scipy.org/doc/), [Seaborn](https://seaborn.pydata.org/)
* **Hypothesis Methods:** 
## Author

* **Takeshi Sugiyama** - *Data Scientist*
  * [Linkedin](https://www.linkedin.com/in/takeshi-sugiyama/)
  * [Tableau](https://public.tableau.com/profile/takeshi.sugiyama)



