#%%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score


#%%
ice_cream_sales_df = pd.read_excel(io="IceCream.xlsx", sheet_name="Sales", header=0, )
sales_axes = ice_cream_sales_df.plot.scatter(x="Temperature (celcius)", y="Ice Cream Sales", figsize=(20,10))


#%%
# Create and fit linear regression object
regr = linear_model.LinearRegression()
regr.fit(X=ice_cream_sales_df["Temperature (celcius)"].values.reshape(-1, 1), y=ice_cream_sales_df["Ice Cream Sales"])


#%%
temp_range = np.array([20.0, 36.0])
predicted_sales = regr.predict(X=temp_range.reshape(-1, 1))


#%%
sales_axes = ice_cream_sales_df.plot.scatter(x="Temperature (celcius)", y="Ice Cream Sales", figsize=(20,10))
sales_axes.plot(temp_range, predicted_sales, color="red")


#%%
print(f"Y = {regr.coef_[0]}*X {regr.intercept_}")


