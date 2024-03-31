
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import cross_val_score, train_test_split


def launch_linear_regression(df, X_columns, y_column, fit_intercept, copy_X, n_jobs, positive):
    X = df[X_columns]  # Replace 'target_column' with the name of your target column
    y = df.loc[:,y_column]  # Replace 'target_column' with the name of your target column
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = LinearRegression(fit_intercept=fit_intercept, copy_X=copy_X, n_jobs=n_jobs, positive=positive)
    
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring='neg_mean_absolute_error')
    mean_mae = -scores.mean()  # Negative sign because cross_val_score returns negative MAE
    
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    test_mae = mean_absolute_error(y_test, y_pred)
    
    return mean_mae, test_mae