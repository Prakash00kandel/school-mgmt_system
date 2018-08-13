class marksheet():
	subjectlist = []
	#create the function that send the marks and subject list
	def addMarkAndSub(self,subject,mark):
		# create the dictionary from the sub and marks
		#add the distionary on the subject list
		'''
		sample dictionary for the subject
		subject = {'subname': subject[0],'mark': mark[0]}
		subjectlist.append(subject)
		'''
		for i in range(len(subject)):
			subject = {'subname': subject[i],'mark': mark[i]}
		self.subjectlist.append(subject)
	def calculatepercentage(self):
		sum = 0
		#map(lambda subject : sum + int(subject['mark']),self.subjectlist)
		for subject in subjectlist:
			sum = sum + subject['mark']

		self.percentage


			
			