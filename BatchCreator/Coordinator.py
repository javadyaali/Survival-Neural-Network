from collections import defaultdict

class BatchBuilder():
	output_Minibatch_Number = 1
	source = []
	user_Tags = []
	output = defaultdict(list)
	all_User_Session_Count = []
	MINIBATCH_SESSION_COUNT = 0
	MINIBATCH_USER_COUNT = 0
	userID = 1
	using_count = 0
	not_used_count = 1000
	not_valid_count = 0

	def __init__(self, each_user_sessions, defaultTags, all_User_Session_Count, MINIBATCH_SESSION_COUNT, MINIBATCH_USER_COUNT):

		self.source = each_user_sessions
		self.user_Tags = defaultTags
		self.all_User_Session_Count = all_User_Session_Count
		self.MINIBATCH_SESSION_COUNT = MINIBATCH_SESSION_COUNT
		self.MINIBATCH_USER_COUNT = MINIBATCH_USER_COUNT
		print("Initializing DONE !!")

	def isValid(self):

		status = "start searching to find valid user"

		while status != "valid user found":
			if (self.all_User_Session_Count[userID-1] < self.MINIBATCH_SESSION_COUNT) or (self.user_Tags[userID-1][1] == "NOT VALID"):
				self.user_Tags[userID-1][1] = "NOT VALID"
				self.not_valid_count += 1
				self.not_used_count -= 1
				self.userID += 1
			else:
				if self.user_Tags[userID-1][1] == "Using":
					status = "valid user found"

				if self.user_Tags[userID-1][1] == "not used":
					self.user_Tags[userID-1][1] = "Using"
					status = "valid user found"
					self.using_count += 1
					self.not_used_count -= 1

				if self.user_Tags[userID-1][1] == "Done":
					if ((self.using_count > 0) or (self.not_used_count > 0)):
						self.userID += 1
					if ((self.using_count == 0) and (self.not_used_count == 0)):
						status = "valid user found"


			if self.userID >= 1000:
				self.userID = 1

		print("Validating DONE !!")

	def addUser(self):
		output[self.MINIBATCH_USER_COUNT].append(self.source[self.userID][(self.user_Tags[self.userID-1][0]) : ((self.user_Tags[self.userID-1][0]) + 41)])
		print("Adding DONE !!")


	def updateTags(self):
		if ((self.user_Tags[self.userID-1][0]) + 41) == self.all_User_Session_Count[self.userID-1]:
			self.user_Tags[self.userID-1][1] = "Done"
			self.user_Tags[self.userID-1][0] = 0

		self.user_Tags[userID-1][1] = "Using"
		self.user_Tags[self.userID][0] += 1
		print("Updating DONE !!")


	def generateOutput(self):
		with open('Minibatch' + str(output_Minibatch_Number) + '.pk', 'wb') as fi:
			# dump your data into the file
			pickle.dump(output, fi)
		print("Generating DONE !!")

	def isDone(self):
		checklist = set([ i[1] for i in self.user_Tags])

		# maybe all checklist is "Done" and doesnt have valid ... so you must change the line below
		if len(checklist == 2) and ("Done" in checklist) and ("NOT VALID" in checklist):
			return True 
		else
			return False

	def reset(self):
		output = defaultdict(list)
		userID = 1


















