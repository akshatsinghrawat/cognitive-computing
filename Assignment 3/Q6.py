import pandas as pd

employees = {
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Edward"],
    "Department": ["HR", "IT", "IT", "Marketing", "Sales"],
    "Age": [29, 34, 41, 28, 38],
    "Salary": [50000, 70000, 65000, 55000, 60000],
    "Years_of_Experience": [4, 8, 10, 3, 12],
    "Joining_Date": ["2020-03-15", "2017-07-19", "2013-06-01", "2021-02-10", "2010-11-25"],
    "Gender": ["Female", "Male", "Male", "Female", "Male"],
    "Bonus": [5000, 7000, 6000, 4500, 5000],
    "Rating": [4.5, 4.0, 3.8, 4.7, 3.5]
}

df = pd.DataFrame(employees)
print("\nEmployee dataset:\n",df)
#A
print("\nShape of DataFrame:",df.shape)
#B
print("\nSummary of DataFrame:\n",df.info())
#C
print("\nDescriptive statistics:\n",df.describe())
#D
print("\nFirst 5 rows:\n", df.head())
print("\nLast 3 rows:\n",df.tail(3))
#E1
print("\nAverage Salary:",df["Salary"].mean())
#E2
print("Total Bonus:",df["Bonus"].sum())
#E3
print("Youngest Age:",df["Age"].min())
#E4
print("Highest Rating:",df["Rating"].max())
#F
sort = df.sort_values(by="Salary", ascending=False)
print("\nSorted by Salary:\n",sort)
#G
def categorize(rating):
    if rating >= 4.5:
        return "Excellent"
    elif rating >= 4.0:
        return "Good"
    else:
        return "Average"
df["Performance"] = df["Rating"].apply(categorize)
print("\nUpdated dataset with Performance categorization:\n",df)
#H
print("\nMissing values:\n",df.isnull().sum())
#I
df.rename(columns={"Employee_ID": "ID"},inplace=True)
print("\nRenamed column:\n",df)
#J1
exp = df[(df["Years_of_Experience"] > 5)]
print("\nEmployees with >5 years experience:\n",exp)
#J2
it = df[(df["Department"] == "IT")]
print("\nEmployees in IT:\n",it)
#K
df["Tax"] = ((df["Salary"])-(df["Salary"] * 0.10))
print("\nAdded Tax column:\n",df)
#L
df.to_csv("employees.csv",index=False)
print("\nModified dataset saved to 'employees.csv'.")
