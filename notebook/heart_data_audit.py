# This folder contains all my Jupyter notebook files. 

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

heart = pd.read_csv(r"dataset/heart-disease.csv")

def audit_dataframe(heart,name):
    print("=" * 70)
    print(name)
    print("=" * 70)
    print("shape: ", heart.shape)
    print("\nData types: ")
    print(heart.dtypes)
    print("\nMissing values: ")
    print(heart.isna().sum())
    print("\nDuplicate rows: ", heart.duplicated().sum())
    print("\n Descriptive statistics: ")
    print(heart.describe(include = 'all').T)

audit_dataframe(heart, "Heart Diseases")


print("Total rows: ", len(heart))
print("Exact Duplaicate Rows:", heart.duplicated().sum())
print("Unique Rows: ", heart. drop_duplicates().shape[0])
heart_unique = heart.drop_duplicates().copy()
print("Raw target distribution:")
print(heart["target"].value_counts())
