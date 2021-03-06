import pandas as pd
import numpy as np
from os import path
import math as m
import sys

import os
def topsis(dfg,wei,val,result):
    if not os.path.isfile(dfg):
        print(f"err : No such file exist")
        exit(1)
    if (os.path.splitext(dfg))[1]!=".csv" :
        print(f"err : wrong file type")
        exit(1)
    if ((os.path.splitext(result))[1])!=".csv":
        print("err : Output file must be .csv")
        exit(1)

    else:
        ds = pd.read_csv(dfg)
        m = len(ds.columns.values)
        if m < 3:
            print("err : file must contain >=3 columns.")
            exit(1)

        try:
            weights = [float(i) for i in wei.split(',')]
        except:
            print("err : Something wrong with weights.")
            exit(1)

        impacts = val.split(',')
        for i in impacts:
            if not (i == '-' or i == '+'):
                print("err : Something wrong with impacts")
                exit(1)

        if m!= len(impacts)+1 or m != len(weights)+1 :
            print("err : Unequal Number of weights,impacts and columns ")
            exit(1)
        
        for i in range(1, m):
            pd.to_numeric(ds.iloc[:, i], errors='coerce')
            ds.iloc[:, i].fillna((ds.iloc[:, i].mean()), inplace=True)

    ds=pd.read_csv('Enter your filename.csv')
    Dataset=ds.iloc[:,1:]
    Dataset

    matrix = Dataset.to_numpy()

    n, m= matrix.shape

    for j in range(m):
        sq = np.sqrt(np.sum(matrix[:, j]**2))
        # print(np.sum(matrix[:,j]**2))
        for i in range(n):
            matrix[i, j] = (matrix[i, j]*weights[j])/sq

    ideal_worst = []
    ideal_best = []
    for i in range(m):
        if impacts[i] == '+':
            ideal_worst.append(min(matrix[:, i]))
            ideal_best.append(max(matrix[:, i]))
        else:
            ideal_worst.append(max(matrix[:, i]))
            ideal_best.append(min(matrix[:, i]))

    score=[]
    for i in range(n):
        ax=0
        bx=0
        for j in range(m):
            ax+=((matrix[i][j]-ideal_best[j])**2)
            bx+=((matrix[i][j]-ideal_worst[j])**2)
        ax=np.sqrt(ax)
        bx=np.sqrt(bx)
        cx=bx/(ax+bx)
        score.append(cx)

    ds['Topsis Score']=score
    ds

    ds['rank']=ds['Topsis Score'].rank(ascending=0)
    ds['rank']=ds['rank'].astype(np.int32)
    ds

    ds.to_csv(result,index=False)
