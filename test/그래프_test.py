from matplotlib import pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_blobs
from sklearn.datasets import make_moons
#X, y = make_moons(n_samples=200, noise=0.05, random_state=0)
#print(X)

plt.title("세개의 클러스터를 가진 가상 데이터")
X, y = make_blobs(n_samples=300, n_features=2, centers=3, random_state=1)
print(X)
#plt.scatter(X[:, 0], X[:, 1], marker='o', c=y, s=100,
#            edgecolor="k", linewidth=2)
plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("$X_1$")
plt.ylabel("$X_2$")
plt.show()