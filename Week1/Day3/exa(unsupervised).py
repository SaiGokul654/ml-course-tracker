# Clustering
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the iris dataset
data = load_iris()
x = data.data

# Scale the features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Number of clusters (Iris has 3 classes)
k = 3

# Create and fit KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(x_scaled)

# Get labels and cluster centers
cluster_labels = kmeans.labels_
cluster_centers = kmeans.cluster_centers_

# Plot the clusters
plt.scatter(x_scaled[:, 0], x_scaled[:, 1], c=cluster_labels, cmap='viridis')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], s=300, c='red', marker='X')
plt.xlabel("Feature 1 (scaled)")
plt.ylabel("Feature 2 (scaled)")
plt.title("KMeans Clustering (Iris)")
plt.show()
