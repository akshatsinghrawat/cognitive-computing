import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data={
    'Subject':['Math', 'AI', 'Cognitive', 'DAA', 'DBMS'],
    'Marks':[87, 90, 91, 89, 93]
}
d=pd.DataFrame(data)
plt.figure(figsize=(8,8))
a=sns.barplot(x='Subject', y='Marks', data=d)

plt.title('Scores of subjects: ')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.grid(axis='y', linestyle='-')

plt.show()