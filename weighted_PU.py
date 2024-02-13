#To use the weighted method, use the WeightedElkanotoPuClassifier class:

from pulearn import WeightedElkanotoPuClassifier
from sklearn.svm import SVC
svc = SVC(C=10, kernel='rbf', gamma=0.4, probability=True)
pu_estimator = WeightedElkanotoPuClassifier(
estimator=svc, labeled=10, unlabeled=20, hold_out_ratio=0.2)
pu_estimator.fit(X, y)
