import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def adj_pos(pos):
    if pos in ['SF-SG', 'SF-PF']:
        return 'SF'
    elif pos in ['PF-SF', 'PF-C']:
        return 'PF'
    elif pos in ['C-PF']:
        return 'C'
    elif pos in ['SG-PG', 'SG-SF', 'SG-PF']:
        return 'SG'
    elif pos in ['PG-SG', 'PG-SF']:
        return 'PG'
    else:
        return pos

    
def plot_feat_importance(model, column):
    feat_scores = pd.DataFrame({'Fraction of Samples Affected' : model.feature_importances_},
                           index=column)
    feat_scores = feat_scores.sort_values(by='Fraction of Samples Affected')
    feat_scores.plot(kind='barh', figsize=(12,8))
    plt.legend(loc='lower right')
    
def model_check(model, train_data, test_data, column, plot=False):
    # X and Y for train and test
    X = train_data[column]
    y = train_data['Salary']
    
    XX = test_data[column]
    yy = test_data['Salary']    
    
    # Train and test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Cross val score
    cross_score = -np.mean(cross_val_score(model, 
                                           X_train, 
                                           y_train, 
                                           scoring='neg_root_mean_squared_error'))
    print('Cross Val Score: {}'.format(cross_score))
    
    # Test set
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    test_set = np.sqrt(mean_squared_error(y_test, y_pred))
    print('Test Set Score:  {}'.format(test_set))
    
    # Validation set
    yy_pred = model.predict(XX)
    rmse = np.sqrt(mean_squared_error(yy, yy_pred))
    print('Actual Score:    {}'.format(rmse))
    
    if plot == True and (type(model) == RandomForestRegressor or type(model) == GradientBoostingRegressor or type(model) == AdaBoostRegressor):
        plot_feat_importance(model,column)

        