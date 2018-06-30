from collections import defaultdict
from random import randint

class BatchBuilder():
	selected_User_ID = 0
	output_Minibatch_Number = 1
	source = []
	user_Tags = []
	output = defaultdict(list)
	all_User_Session_Count = []
	MINIBATCH_SESSION_COUNT = 0
	MINIBATCH_USER_COUNT = 0
	userID = 1

# create baskets for identifying user's state 
	not_valid_basket = []
	not_used_basket = []
	using_basket = []
	done_basket = []

	def __init__(self, each_user_sessions, defaultTags, all_User_Session_Count, MINIBATCH_SESSION_COUNT, MINIBATCH_USER_COUNT):

		self.source = each_user_sessions
		self.all_User_Session_Count = all_User_Session_Count
		self.MINIBATCH_SESSION_COUNT = MINIBATCH_SESSION_COUNT
		self.MINIBATCH_USER_COUNT = MINIBATCH_USER_COUNT
		print("Initializing DONE !!")


# separating valid users from invalid ones (default tags is "not used")
	def separate_Valid_User(self):

		for item in self.source:
			if self.all_User_Session_Count[item-1] < 41:
				not_valid_basket.append(item)
				self.user_Tags[item-1][1] = "Not valid"

			else:
				not_used_basket.append(item)

		print("Valid sepataration DONE !!")

	def select_User(self):
		self.selected_User_ID = randint(1, 1000)



	def add_User(self):

		if (self.user_Tags[self.selected_User_ID-1][1] != "Not valid"):
			output[self.MINIBATCH_USER_COUNT].append(self.source[self.selected_User_ID][(self.user_Tags[self.selected_User_ID-1][0]) : ((self.user_Tags[self.selected_User_ID-1][0]) + 41)])
			self.MINIBATCH_USER_COUNT -= 1
			print("Adding DONE !!")

		else




	def update_Tags(self):
		if ((self.user_Tags[self.selected_User_ID-1][0]) + 41) == self.all_User_Session_Count[self.selected_User_ID-1]:
			self.user_Tags[self.selected_User_ID-1][1] = "Done"
			self.user_Tags[self.selected_User_ID-1][0] = 0

		else:
			if self.user_Tags[self.selected_User_ID-1][1] == "Not used":
				self.user_Tags[self.selected_User_ID-1][1] = "Using"

			self.user_Tags[self.selected_User_ID][0] += 1

		print("Updating DONE !!")


	def generate_Output(self):
		with open('Minibatch' + str(self.output_Minibatch_Number) + '.pk', 'wb') as fi:
			# dump your data into the file
			pickle.dump(output, fi)

		self.output_Minibatch_Number += 1
		print("Generating DONE !!")

	def is_Done(self):
		checklist = set([ i[1] for i in self.user_Tags])

		# maybe all checklist is "Done" and doesnt have valid ... so you must change the line below
		if len(checklist == 2) and ("Done" in checklist) and ("Not valid" in checklist):
			return True 
		else
			return False

	def reset(self, MINIBATCH_USER_COUNT):
		output = defaultdict(list)
		self.MINIBATCH_USER_COUNT = MINIBATCH_USER_COUNT