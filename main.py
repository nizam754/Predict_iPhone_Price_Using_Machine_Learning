import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']], data['price'])
model.predict([[14]])
print(model.predict([[12]]))