"""Practical No 5
Aim: Support vector Machine
Code:"""
# Import necessary libraries
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
# Load the Iris dataset
iris = datasets.load_iris()
# Features (X) and labels (y)
X = iris.data # Using all four features (sepal length, sepal width, petal length, petal width)
y = iris.target # Labels (0, 1, or 2 for the three Iris flower species)
# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create an SVM classifier (using the default RBF kernel)
svm_classifier = SVC()

# Train the classifier with the training data
svm_classifier.fit(X_train, y_train)
# Make predictions on the test data
y_pred = svm_classifier.predict(X_test)
# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
# Output the accuracy
print("RollNo: 2453046\n")
print(f"Accuracy: {accuracy * 100:.2f}")
"""Make sure you have the required libraries installed:
pip install scikit-learn""" 