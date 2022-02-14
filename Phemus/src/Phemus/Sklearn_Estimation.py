import joblib
import time
import random
import numpy as np
from Dataset import Dataset
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

def get_random_input(dataset: Dataset):
    num_params = dataset.num_param
    col_to_be_predicted_idx = dataset.col_to_be_predicted_idx
    sensitive_param_idx = dataset.sensitive_param_idx
    input_bounds = dataset.input_bounds
    x = []
    for i in range(len(input_bounds)):
        random.seed(time.time())
        x.append(random.randint(input_bounds[i][0], input_bounds[i][1]))

    x[sensitive_param_idx] = 0
    return x

def evaluate_input(inp, input_pkl_name, dataset: Dataset):
    sensitive_param_idx = dataset.sensitive_param_idx
    model = joblib.load(input_pkl_name)
    inp0 = [int(i) for i in inp]
    inp1 = [int(i) for i in inp]

    for i in range(dataset.input_bounds[sensitive_param_idx][1] + 1):
        for j in range(dataset.input_bounds[sensitive_param_idx][1] + 1):
            if i != j: 
                inp0 = [int(k) for k in inp]
                inp1 = [int(k) for k in inp]

                inp0[sensitive_param_idx] = i
                inp1[sensitive_param_idx] = j

                inp0 = np.asarray(inp0)
                inp0 = np.reshape(inp0, (1, -1))

                inp1 = np.asarray(inp1)
                inp1 = np.reshape(inp1, (1, -1))
                
                # drop y column here 
                inp0delY = np.delete(inp0, [dataset.col_to_be_predicted_idx])
                inp1delY = np.delete(inp1, [dataset.col_to_be_predicted_idx])
                inp0delY = np.reshape(inp0delY, (1, -1))
                inp1delY = np.reshape(inp1delY, (1, -1))

                out0 = model.predict(inp0delY)
                out1 = model.predict(inp1delY)
            
                if abs(out1 + out0) == 0:
                    return abs(out1 + out0) == 0
    # return (abs(out0 - out1) > threshold)
    # for binary classification, we have found that the
    # following optimization function gives better results
    return False

def get_estimate_array(dataset: Dataset, input_pkl_name, num_trials, samples):
    estimate_array = []
    rolling_average = 0.0
    for i in range(num_trials):
        disc_count = 0
        total_count = 0
        for j in range(samples):
            total_count = total_count + 1
            if(evaluate_input(get_random_input(dataset), input_pkl_name, dataset)):
                disc_count = disc_count + 1

        estimate = float(disc_count)/total_count
        rolling_average = ((rolling_average * i) + estimate)/(i + 1)
        estimate_array.append(estimate)
        print(estimate, rolling_average)
    return estimate_array

def get_fairness_estimation(dataset: Dataset, input_pkl_name, num_trials, samples):
    arr = get_estimate_array(dataset, input_pkl_name, num_trials, samples)
    return str(np.mean(arr) * 100)
