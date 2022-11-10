from sklearn import datasets # To Get iris dataset
from sklearn import svm # To fit the svm classifier
import numpy as np
import matplotlib.pyplot as plt 



def visuvalize_sepal_data():
    iris = datasets.load_iris()
    X = iris.data[:,:2]
    y = iris.target
    plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.coolwarm)
    plt.xlabel("Sepal length")
    plt.ylabel("Sepal width")
    plt.title("Sepal Width & Length")
    plt.show()

visuvalize_sepal_data()


iris = datasets.load_iris()
X = iris.data[:,:2]
y = iris.target
C = 1.0     #SVM regularization parameter

svc = svm.SVC(kernel='linear', C=C).fit(X,y)
h = 0.02
x_min, x_max = X[:,0].min()-1, X[:,0].max()+1
y_min, y_max = X[:,1].min()-1, X[:,1].max()+1

xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max,h))

titles =  ['SVC with linear kernel',
           'LinearSVC (linear kernel)',
           'SVC with RBF kernel',
           'SVC with polynomial (degree 3) kernel']

for i,clf in enumerate((svc,Linear)):
    plt.subplot(2,2, i+1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    
    Z=svm.clf.predict(np,c[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, xy, Z, cmap=plt.cm.coolwarm, alpha=0.8)
    plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.coolwarm)
    plt.xlabel("Sapel length")
    plt.ylabel("Sapel width")
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])
    
plt.show()
    