from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

X_train, X_test, y_train, y_test = train_test_split(iris_dataset["data"], iris_dataset["target"],
                                                    random_state=0)


kn = KNeighborsClassifier(n_neighbors=1)
kn.fit(X_train, y_train)

# x_new = np.array([[5, 2.9, 1, 0.2]])
# prediction = kn.predict([X_test[0]])
# print("prediction : "+str(prediction)+" Actual : "+str(y_test[0]))

print("\n TEST SCORE[ACCURACY]: {:.2f}\n".format(kn.score(X_test, y_test)))

    