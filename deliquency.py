# Logistic Regression Model for Predicting Customer Delinquency

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score, roc_curve
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv("Delinquency_prediction_dataset_cleaned.csv")  # Make sure this file is uploaded

# Step 2: Drop irrelevant or non-numeric columns
df = df.drop(columns=["Customer_ID", "Location", "Credit_Card_Type", 
                      "Month_1", "Month_2", "Month_3", "Month_4", "Month_5", "Month_6"])

# Step 3: Drop rows with missing values (or use imputation if needed)
df.dropna(inplace=True)

# Step 4: Encode categorical variables
df['Employment_Status'] = df['Employment_Status'].astype('category').cat.codes

# Step 5: Define features and target
X = df.drop("Delinquent_Account", axis=1)
y = df["Delinquent_Account"]

# Step 6: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 7: Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 8: Train logistic regression model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 9: Make predictions
y_pred = model.predict(X_test_scaled)
y_prob = model.predict_proba(X_test_scaled)[:, 1]

# Step 10: Evaluate model
print("Classification Report:\n", classification_report(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))

# Step 11: Plot ROC curve
fpr, tpr, _ = roc_curve(y_test, y_prob)
plt.figure(figsize=(6, 4))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_test, y_prob):.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - Logistic Regression")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
