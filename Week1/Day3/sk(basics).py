from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the iris dataset
iris=load_iris()
iris
x=iris.data
y=iris.target

# Split the dataset into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

# Create a logistic regression model
model=LogisticRegression()

#Fit the model to the training data
model.fit(x_train,y_train)

# Make predictions on the test set
y_pred=model.predict(x_test)

# Calculate accuracy
accuracy= accuracy_score(y_test, y_pred)
print(f"Accuracy of the Logistic Regression model: {accuracy:.2f}")

# Perform cross-validation
cross_val_score=cross_val_score(model,x,y,cv=5)
mean=cross_val_score.mean()
print(f"Mean cross-validation score: {mean:.2f}")


