#Based on the paper A bagging SVM to learn from positive and unlabeled examples (2013) by Mordelet and Vert. The implementation is by Roy Wright (roywright on GitHub), and can be found in his repository.

from pulearn import BaggingPuClassifier
from sklearn.svm import SVC
svc = SVC(C=10, kernel='rbf', gamma=0.4, probability=True)
pu_estimator = BaggingPuClassifier(
base_estimator=svc, n_estimators=15)
pu_estimator.fit(X, y)

    
#Note: Any scikit-learn classifier can be used as the base estimator.
