import pandas as pd
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
import joblib
import config

df = pd.read_csv("default of credit card clients.csv")

# Remove ID row
df = df.iloc[:, 1:]

cat_feature = list(df.columns)

for col in cat_feature:
    df[col]=le.fit_transform(df[col])

df["SEX"].replace({0 : -1}, inplace=True)
df["default payment next month"].replace({0 : -1}, inplace=True)

col_to_be_predicted = "default payment next month"
X=df.drop([col_to_be_predicted],axis=1)
y=df[col_to_be_predicted]

df.to_csv(path_or_buf="CCClient.csv", index=False)

print(df)