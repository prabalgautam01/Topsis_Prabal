
# Topsis

Topsis-Prabal-101916102 is a library for calculating topsis score and ranking them according to the score.


## What is Topsis

Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) originated in the 1980s as a multi-criteria decision making method. TOPSIS chooses the alternative of shortest Euclidean distance from the ideal solution, and greatest distance from the negative-ideal solution. More details at wikipedia.
## Installation

pip install Topsis-Prabal-101916102
## In Command Prompt

The package Topsis-Prabal-101916102 can be run though the command line as follows:

 

 
    >> import Topsis-Prabal-101916102
    >> Topsis-Prabal-101916102.topsis("data.csv","1,1,1,1","+,+,-,+","result.csv")                                     

    
## Constraints

Input File:

Input file must contain three or more columns.
First column is the object/variable name (e.g. M1, M2, M3, M4...).
From 2nd to last columns contain numeric values only.

Output File:

Result file contains all the columns of input file and two additional columns having Topsis Score and Rank.
The output is created in the form of csv file and stored and also it is displayed.

The impacts given in the command line should be either + or - depending if you want to maximise the column parameter or minimise it.

    