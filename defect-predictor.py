import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("data\defects.csv")
print(df.columns)

X= df[["Code Changes", "Test Coverage (%)", "Past Defects"]]
Y= df["Severity"]

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

model= RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

print("Model Accuracy:", accuracy_score(Y_test,Y_pred))

new_module = [[8,50,3]]
risk_prediction = model.predict(new_module)
severity_labels= {0:"Low",1:"Medium",2:"High",3:"Critical"}
print("Severity:",severity_labels[risk_prediction[0]])