import pickle
import numpy as np
import pandas as pd
import datetime
from collections import defaultdict
from Coordinator import BatchBuilder
from random import randint


# use output of PreProcessing.py to create batch

MINIBATCH_SESSION_COUNT = 41 # 40 training session with output
MINIBATCH_USER_COUNT = 32 # each minibatch has 32 users

PreProcessingOutput = pickle.load(open("/Users/javadyaali/Desktop/Home/Research/MLLSoleymani/Survival-Neural-Network/PreProcessingOutput.pk",'rb'))

# create a list that contain session number of each user
all_User_Session_Count = [0] * 1000

# create a dictionary that store sessions of each user, separately
each_user_sessions = defaultdict(list)

userID = 1000
for i in PreProcessingOutput:
	if i[0] == userID:
		all_User_Session_Count[userID-1] += 1
		each_user_sessions[userID].append(i)
	else:
		userID -= 1

# default tag that shows users status in batch creation process that contains 3 elements for each user, [last session number that used, tag, number of usage in batch creation]
default_Tags = [[0,"Not used"]] * 1000
 

# create a builder
batch_Builder = BatchBuilder(each_user_sessions, defaultTags, all_User_Session_Count, MINIBATCH_SESSION_COUNT, MINIBATCH_USER_COUNT)


while 1:

	counter_Minibatch_User = MINIBATCH_USER_COUNT

	while counter_Minibatch_User != 0:
		batch_Builder.separate_Valid_User()
		batch_Builder.add_User()
		batch_Builder.update_Tags()
		counter_Minibatch_User -= 1

	# create output here
	batch_Builder.generateOutput()

	# check if all users used in batch creation process
	if batch_Builder.isDone():
		break
	else:
		batch_Builder.reset(MINIBATCH_USER_COUNT)


print("Create all minibatches successfully !!")