import pandas as pd
<<<<<<< HEAD:backend/aequitas/utils.py
from random import seed, shuffle
import backend.aequitas.loss_funcs as lf # our implementation of loss funcs
from scipy.optimize import minimize # for loss func minimization
from multiprocessing import Pool, Process, Queue
from collections import defaultdict
from copy import deepcopy
import matplotlib.pyplot as plt # for plotting stuff
import sys
=======
import os
print("inside utils.py", os.getcwd())
>>>>>>> origin/yunping_packageversion:backend/api/aequitas/utils.py

def get_input_bounds(input_file, sensitive_col_name):
    input_bounds = []
    df=pd.read_csv(f'{input_file}')
    for col in df:
        # exclude the column you're trying to predict
        if col == sensitive_col_name:
            continue
        numUniqueVals = df[col].nunique()
        input_bounds.append([0, numUniqueVals - 1]) # bound is inclusive
    return input_bounds

def get_column_names(input_file):
    df=pd.read_csv(f'{input_file}')
    return list(df.columns)

def get_idx_of_column(input_file, column):
    df=pd.read_csv(f'{input_file}')
    return list(df.columns).index(column)