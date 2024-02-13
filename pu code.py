#prepare data
x_data = the training set
y_data = target var (1for the positive and not-1for the rest)

#fit the classifier and estimate P(s=1|y=1)
classifier, ps1y1 =
        fit_PU_estimator(x_data, y_data, 0.2, Estimator())

#Estimate the prob that x_data is labeled P(s=1|x)

predicted_s = classifier.predict_proba(x_data)

#estimate the actual probabilities that X is positive# by calculating P(s=1|X)/P(s=1|y=1)
predicted_y = estimated_s / ps1y1


#Fit the PU Estimator () Method
pu_estimator, probs1s1 = fit_PU_estimator(
    x_train,
    y_train,
    0.2,
    xgb.XGBClassifier())

predicted_s = pu_estimator.ppredict_proba(x_train)
predicted_s = predicted_s[:,1]
predicted_y = predicted_s/probs1y1


deffit_PU_estimator(X,y, hold_out_ratio, estimator): # The training set will be divideed into a
#fitting-set that will be used # to fit the the estimator P(s=1|X) and a held-out set of positive samples
# that will be used to estimate P(s=1|y=1)# ------# find the indices of the positive /labeled elementsassert
#(type(y) == np.ndarray), "Must pass np.ndarray rathjer than list as y'
    positive = np.where(y == 1.)[0]
    # hold_out_size = the *number* of positives/labeled samples # that we will use later to estimate P(s=1|y=1)
    hold_out = positives[:hold_out_size]
    # the actual positive *elements* that we will keep aside
    X_hold_out = X[hold_out]
    # remove the held out elements from X and Y
    X = np.delete(X, hold_out,0)
    y = np.delete(y, hold_out)
    #We fit the estimator on the unlabeled samples + (part of the) positive and labeled ones.
    # In dorder to estimate P(s=1|X) or what is the probability that an element is *labeled*
    estimator.fit(X, y)
    #We then use the estimator for prediction of the positive held-ouy set # in order to estimate P(s=1|y=1)
    hold_out_predictions = estimator.predict_proba(x_hold_out)
    #take the probability that it is 1
    hold_out_predictions = hold_out_predictions[:,1]
    # save the mean probability
    c = np.mean(hold_out_predictions)
    return estimator, c


defpredict_PU_prob(X, estimator, prob_s1y1):
    prob_pred = estimator.predict_proba(X)
    prob_pred = prob_pred[:,1]
    return prob_pred / prob_s1y1

    
    
