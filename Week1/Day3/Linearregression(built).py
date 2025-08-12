import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

# Load the California housing dataset
data = fetch_california_housing()
X = data.data
y = data.target

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(X_train)
x_test_scaled = scaler.transform(X_test)

# Add bias column
x_train_scaled = np.concatenate((np.ones((x_train_scaled.shape[0], 1)), x_train_scaled), axis=1)
x_test_scaled = np.concatenate((np.ones((x_test_scaled.shape[0], 1)), x_test_scaled), axis=1)

# Linear regression using normal equation
def linear_regression(x, y):
    return np.linalg.inv(x.T @ x) @ x.T @ y

# Train model
weights = linear_regression(x_train_scaled, y_train)

# Predict
y_pred = x_test_scaled @ weights

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Weights:", weights)
print("Mean Squared Error:", mse)
print("R² Score:", r2)
