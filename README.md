# Moneyball in NBA: Predicting NBA player salary

![Insert Cover Photo]()

## Table of Contents
1. [Introduction](#introduction)
    - [Background](#background)
    - [Data](#data)
        - [Web scrapping](#web-scrapping)
        - [Combining and Cleaning](#combining-and-cleaning)


2. [Exploratory Data Analysis](#exploratory-data-analysis)
    - [Average Salary Overtime](#average-salary-overtime)
    - [Feature Engineering](#feature-engineering)
    - [Salary Distribution](#salary-distribution)

3. [Prediction](#H)
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

I've also extracted the salary cap of each year from basketball reference's [page](https://www.basketball-reference.com/contracts/salary-cap-history.html). 

You can find the code I used for web scrapping [here](Insertcodelink).  



#### Combining and Cleaning

I've joined the 2 datasets on player's name. 

I've cleaned the names from both sources so that it would be as consistant as possible (So that it would join as much as possible)


Some steps I took to clean the name:
- Converted special characters to normal english characters. (Eg. 'Žižić' to 'Zizic')
- Removed: 
    - 'Jr.'
    - 'III'
    - periods
    - spaces
    - '*' (labeled for hall of fame players)

I've also created an id column for each entry with `Player` + `year'`.

However, since the 2 websites had different names for some players (Eg. Lou Williams vs Louis Williams), I could not join on all players. 

On the training set, 370 players (4.2% of data) that failed to join. I've decided to  drop them from my training model.

On the test set, I had 12 players (2.3% of data) that failed to join. Since the count was low, I've decided to manually input the salary so I can predict all the players in the test set.


All the columns in my dataset were string type so I converted them to number format. For `Salary` and `SalaryCap`, I had to replace the commas and dollar sign to convert to numbers. 

I've ended up with 9310 rows and 33 columns after cleaning.
- Train Set: 2000-2018 Seasons (8780 rows, 33 columns)
- Test Set: 2019 Season (530 rows, 33 columns)


---

## Exploratory Data Analysis


### Average Salary Overtime


### Feature Engineering




### Salary Distribution





**Positive correlation with >= 0.5**

| Positive       | Correlation |
| -------------- | ----------- |
| **Goals**      | **0.92**    |
| Half time lead | 0.89        |
| Half time goals| 0.86        |
| Shots          | 0.75        |
| Shots on Target| 0.67        |
| Corner Kicks   | 0.66        |


**No correlation with < 0.5 & > -0.5**

| No correlation  | Correlation |
| -------------- | ------------ |
| Yellow cards   | 0.21         |
| Red cards      | 0.01         |
| Fouls          | -0.16        |


---

## Hypothesis Testing

### Hypothesis Test 1

**Is the average number of games with 0-0 score lower than 8%?**

My first hypothesis test was to see whether the average number of games ending in 0-0 score was lower than 8% (approxi 1/12 odds). I chose this threshold because I wanted to know if I were to watch 1 soccer game a month for a year, how likely is it that I would end up watching a “boring” game. Watching a game with no goals is probably one of the most upsetting parts of being a fan of the game and I want to be confident that the probability would be less than 8%.  

**Null hypothesis:** The average number of games with 0 goal = 8%.
**Alternative hypothesis:** The average number of games with 0 goal < 8%.

**Alpha = 0.05**


#### Model Choice 1

Binomial Distribution

Since I had data that resulted in 0-0 score for the last 10 years I used a binomial distribution to calculate my hypothesis test.

#### Results 1

![HT1](img/HT1.png)

**P-Value Result: 0.021**

The hypothesis test result shows that the P-value resulted in 0.021 and since this is below the 0.05 threshold I could reject the null hypothesis. Therefore, the average number of games with 0 goals being less than 8% with a threshold of 0.05 holds true.


---

### Hypothesis Test 2

**Does the German league, on average have a lower 0-0 resulting games compared to the Italian league?**

Since Germany’s league had the lowest average number of games with 0 goals and Italy had the highest, I wanted to compare those two leagues if that was statistically significant. If I were to watch a soccer game, should I watch the league in Germany over Italy’s?


**Null hypothesis:** The average number of games with 0 goals in Germany = Italy.

**Alternative hypothesis:** The average number of games with 0 goals in Germany < Italy.

**Alpha = 0.05**


#### Model Choice 2

- Welch’s T-Test
- Mann-Whitney U-Test (Two-Sided)

I divided the average number of games with 0 goals over 10 seasons for both leagues in Germany and Italy so that I could have 2 sample distributions to compare each other.  I applied the Welch’s T-Test and Mann-Whitney U-Test using these 2 sample distributions with both sample size with n=10. 




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



