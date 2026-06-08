import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('C:\\Users\\shesh\\CAREER\\SBAB\\BCA 3RD YEAR\\BCA 6TH SEM\\Lab Programs\\ML_Programs\\study_data.csv')
data.columns = data.columns.str.strip()
print(data.columns)

# Scatter plot of Study Hours vs. Exam Scores
plt.figure(figsize=(14, 7))
plt.subplot(1, 2, 1) #1 row, 2 columns, 1st subplot
plt.scatter(data['Study Hours'], data['Exam Score'], color='dodgerblue', edgecolor='k', alpha=0.7)
plt.title('Study Hours vs. Exam Scores')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.grid(True)

# Bar chart of Average Exam Score by Study Hour Range
# Creating bins for study hour ranges
bins = [0, 2, 4, 6, 8, 10, 12]
labels = ['0-2', '2-4', '4-6', '6-8', '8-10', '10-12']
data['Study Hour Range'] = pd.cut(data['Study Hours'], bins=bins, labels=labels, right=False)
grouped_data = data.groupby(['Study Hour Range'],observed=True)['Exam Score'].mean()
plt.subplot(1, 2, 2) #1 row, 2 columns, 2nd subplot
grouped_data.plot(kind='bar', color='salmon')
plt.title('Average Exam Score by Study Hour Range')
plt.xlabel('Study Hour Range')
plt.ylabel('Average Exam Score')
plt.xticks(rotation=0) # Keep the category labels horizontal

plt.tight_layout() # Adjust subplots to fit into figure area.
plt.show()
