import pickle
import numpy as np
import pandas as pd
import datetime
from random import shuffle


# use output of PreProcessing.py to create batch

SESSION_COUNT = 5000

PreProcessingOutput = pickle.load(open("/home/hamid/Desktop/javad/research/mll/PreProcessing/PreProcessingOutput.pk",'rb'))

print(type(PreProcessingOutput))

x = 0
for i in PreProcessingOutput:
	if i[0] == 1000 :
		x += 1 

			