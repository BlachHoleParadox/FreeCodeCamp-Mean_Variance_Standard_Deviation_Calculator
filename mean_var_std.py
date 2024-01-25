import numpy as np

# function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.

def calculate(list):
    arr = np.array(list)
    if arr.shape != (9,):
        raise ValueError('List must contain nine numbers.')
    
    mat = arr.reshape(3,3)

    calculations = {
        'mean': [
            mat.mean(axis=0).tolist(),
            mat.mean(axis=1).tolist(),
            np.mean(mat)
        ],
        'variance': [
            mat.var(axis=0).tolist(),
            mat.var(axis=1).tolist(),
            np.var(mat)
        ],
        'standard deviation': [
            mat.std(axis=0).tolist(),
            mat.std(axis=1).tolist(),
            np.std(mat)
        ],
        'max': [
            mat.max(axis=0).tolist(),
            mat.max(axis=1).tolist(),
            np.max(mat)
        ],
        'min': [
            mat.min(axis=0).tolist(),
            mat.min(axis=1).tolist(),
            np.min(mat)
        ],
        'sum': [
            mat.sum(axis=0).tolist(),
            mat.sum(axis=1).tolist(),
            np.sum(mat)
        ],

    }
    return calculations
