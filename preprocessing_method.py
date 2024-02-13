
import numpy as np

def preprocess_pu(X, y):
    # separate positive and unlabeled data
    X_pos = X[y == 1]
    X_unl = X[y == 0]
    # randomly select a portion of the unlabeled data to be positive
    n_pos = X_pos.shape[0]
    n_unl = X_unl.shape[0]
    n_pu = int(n_pos * (n_unl / (n_pos + n_unl)))
    np.random.shuffle(X_unl)
    X_pu = X_unl[:n_pu]
    y_pu = np.ones(n_pu)
    # concatenate positive and new PU data
    X_pu = np.concatenate((X_pos, X_pu))
    y_pu = np.concatenate((np.ones(n_pos), y_pu))
    return X_pu, y_pu

# Example usage:
X = np.random.randn(100, 10)
y = np.random.randint(0, 2, 100)
X_pu, y_pu = preprocess_pu(X, y)


"""
This code assumes that the input data X and labels y are numpy arrays.
It separates the positive examples (i.e., those with label 1) from the unlabeled examples (i.e., those with label 0) in the input data.
Then, it randomly selects a portion of the unlabeled data to be positive and concatenates it with the original positive data to create the PU dataset.
