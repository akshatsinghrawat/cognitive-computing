#!/usr/bin/env python
# coding: utf-8

# IMPORTING LIBRARIES:

# In[1]:


import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
from imblearn.over_sampling import SMOTE


# LOADING THE DATASET:

# In[2]:


df = pd.read_csv("creditcard.csv")


# PRINTING THE MISSING VALUES:

# In[3]:


print("Missing values in dataset:\n", df.isnull().sum())


# REMOVING DUPLICATE VALUES:

# In[4]:


df.drop_duplicates(inplace=True)


# DETECTING AND REMOVING OUTLINERS USING INTERQUARTILE RANGE METHOD:

# In[5]:


Q1 = df["Amount"].quantile(0.25)
Q3 = df["Amount"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df["Amount"] >= lower_bound) & (df["Amount"] <= upper_bound)]


# VISUALISING THE DISTRIBUTION OF FRAUD(1) AND LEGITIMATE TRANSACTIONS(0) USING A COUNTPLOT FROM SEABORN LIBRARY:

# In[6]:


plt.figure(figsize=(6,4))
sns.countplot(x="Class", data=df, hue="Class", palette="coolwarm", legend=False)
plt.title("Fraud vs Non-Fraud Transactions (Before SMOTE)")
plt.xlabel("Transaction Type (0 = Legitimate, 1 = Fraud)")
plt.ylabel("Count")
plt.show()


# SEPERATE FEATURES (x) AND TARGET VARIABLE (y) FROM THE DATASET:

# In[8]:


X = df.drop(columns=["Class"])
y = df["Class"]


# STANDARDISING THE FEATURE VALUE IN X USING STANDARDSCALER:

# In[9]:


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# HANDLING IMBALANCED DATA USING SMOTE (Synthetic Minority Over-sampling Technique):

# In[10]:


smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)


# VISUALISING THE DISTRIBUTION AFTER APPLYING SMOTE:

# In[11]:


plt.figure(figsize=(6,4))
sns.countplot(x="Class", data=pd.DataFrame({"Class": y_resampled}), hue="Class", palette="coolwarm", legend=False)
plt.title("Fraud vs Non-Fraud Transactions (After SMOTE)")
plt.xlabel("Transaction Type (0 = Legitimate, 1 = Fraud)")
plt.ylabel("Count")
plt.show()


# SPLITING THE DATASET INTO TRAINING AND TESTING SETS:

# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42, stratify=y_resampled)


# In[13]:


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


# VISUALIZING THE FEATURE IMPORTANCE OF A TRAINED MODEL USING A BAR CHART:

# In[16]:


feature_importances = model.feature_importances_
plt.figure(figsize=(12,6))
sns.barplot(x=X.columns, y=feature_importances, palette="viridis", hue=X.columns, legend=False)
plt.xticks(rotation=90)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.show()


# CREATING A CONFUSION MATRIX TO EVALUATE THE PERFORMANCE OF A CLASSIFICATION MODEL:

# In[17]:


y_pred = model.predict(X_test)
conf_matrix = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(5,4))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=["Legit", "Fraud"], yticklabels=["Legit", "Fraud"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


#  COMPUTING THE ROC CURVE AND AUC SCORE:

# In[18]:


fpr, tpr, _ = roc_curve(y_test, model.predict_proba(X_test)[:,1])
roc_auc = auc(fpr, tpr)


# In[19]:


plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, color="darkorange", label=f"AUC = {roc_auc:.2f}")
plt.plot([0, 1], [0, 1], linestyle="--", color="gray")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.show()


# PRINTING THE CLASSIFICATION REPORT:

# In[20]:


print("Classification Report:\n", classification_report(y_test, y_pred))


# CALCULATING AND PRINTING THE ACCURACY OF MODEL:

# In[21]:


from sklearn.metrics import accuracy_score

# Predict on test set
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2%}")


# LOGISTIC REGRESSION MODEL:

# In[22]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Split dataset into train and test sets (assuming X, y are defined)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling (important for Logistic Regression)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train Logistic Regression Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Predictions
y_pred = model.predict(X_test_scaled)

# Model Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Logistic Regression Model Accuracy: {accuracy:.2%}")

# Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix Visualization
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()


# In[24]:


get_ipython().system('pip install xgboost')


# XGBoost CLASSIFIER:

# In[25]:


import xgboost as xgb
from sklearn.metrics import roc_auc_score

# Train XGBoost Model
xgb_model = xgb.XGBClassifier(use_label_encoder=False, eval_metric='logloss')
xgb_model.fit(X_train, y_train)

# Predictions for XGBoost
y_pred_xgb = xgb_model.predict(X_test)
y_pred_prob_xgb = xgb_model.predict_proba(X_test)[:, 1]

# Model Accuracy
accuracy_xgb = accuracy_score(y_test, y_pred_xgb)
roc_auc_xgb = roc_auc_score(y_test, y_pred_prob_xgb)

print(f"XGBoost Accuracy: {accuracy_xgb:.2%}")
print(f"XGBoost AUC Score: {roc_auc_xgb:.2f}")

# **Confusion Matrix for XGBoost**
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_xgb), annot=True, fmt="d", cmap="Oranges")
plt.title("Confusion Matrix - XGBoost")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# **ROC Curve for XGBoost**
fpr_xgb, tpr_xgb, _ = roc_curve(y_test, y_pred_prob_xgb)

plt.figure(figsize=(6, 4))
plt.plot(fpr_xgb, tpr_xgb, color="purple", lw=2, label=f"XGBoost ROC (AUC = {roc_auc_xgb:.2f})")
plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve - XGBoost")
plt.legend()
plt.show()


# In[ ]:




