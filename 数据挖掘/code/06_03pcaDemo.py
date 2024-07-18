from sklearn.decomposition import PCA
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
def mscatter(x, y, ax=None, m=None, **kw):
    import matplotlib.markers as mmarkers
    if not ax: ax = plt.gca()
    sc = ax.scatter(x, y, **kw)
    if (m is not None) and (len(m) == len(x)):
        paths = []
        for marker in m:
            if isinstance(marker, mmarkers.MarkerStyle):
                marker_obj = marker
            else:
                marker_obj = mmarkers.MarkerStyle(marker)
            path = marker_obj.get_path().transformed(
                marker_obj.get_transform())
            paths.append(path)
        sc.set_paths(paths)
    return sc
data_url = "iris_train_shuzhi.csv"
df = pd.read_csv(data_url)
X = df.iloc[:,1:5]
c = df.iloc[:,5]
pca = PCA(n_components=2)
pca.fit(X)
d = np.array(pca.transform(X))
x = pca.transform(X)[:,0]
y = pca.transform(X)[:,1]
m = {1: 's', 2: 'o', 3: 'D', 4: '+'}
cm = list(map(lambda x: m[x], c))
fig, ax = plt.subplots()
scatter = mscatter(x, y, c=c, m=cm, ax=ax, cmap=plt.cm.RdYlBu)
plt.show()
