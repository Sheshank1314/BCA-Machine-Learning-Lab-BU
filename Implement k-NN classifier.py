import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Dummy student data: exam score 1, exam score 2, pass/fail (features)
X = np.array([[80, 75], [95, 90], [60, 50], [45, 30], [30, 40], [85, 95], [70, 60], [50, 55], [40, 45], [60, 70]])
y = np.array([1, 1, 0, 0, 0, 1, 1, 0, 0, 1]) # Binary classes for demonstration

# Split the data into trainijng and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the k-NN classifier with k=3
knn = KNeighborsClassifier(n_neighbors=3)

# Train the classifier on the training data
knn.fit(X_train, y_train)

# Evaluate the classfier's performance
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy on the test set: {:.2f}".format(accuracy))

# Take user input for exam scores
exam_score1 = float(input("Enter Exam Score 1: "))
exam_score2 = float(input("Enter Exam Score 2: "))

# Prepare the user input for prediction
user_input = np.array([[exam_score1, exam_score2]])

# Use the trained k-NN classifier to predict the outcome
predicted_outcome = knn.predict(user_input)

if predicted_outcome[0] == 1:
    print("Based on the exam scores provided, the student is predicted to pass.")
else:
    print("Based on the exam scores provided, the student is predicted to fail.")
