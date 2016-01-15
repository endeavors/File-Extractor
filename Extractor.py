import time, urllib, sys, datetime, math, os

URL = "http://2a.ucsd.edu/"
EXT = ".pdf"
date = datetime.datetime.now()
offset_date = 2

def extract_prev_yr():

	base_str = URL + "quiz/quiz-Win15/quiz"
	saveToPath = "./Winter15/"

	if not os.path.exists(saveToPath):
		os.makedirs(saveToPath)

	for x in range(9):
		urllib.urlretrieve(base_str + str(x+1) + EXT, saveToPath + "quiz" 
			+ str(x+1) + EXT)
		print "\rDone: %d/9" % (x+1),
		sys.stdout.flush()
		time.sleep(2)

def extract_quiz():

	saveToPath = "./Winter16/Quiz/"

	if not os.path.exists(saveToPath):
		os.makedirs(saveToPath)

	week = math.ceil((date.day - offset_date)/float(7))
	
	urllib.urlretrieve(URL + "quiz/quiz-Win16/quiz" + str(int(week)) + EXT, saveToPath + 
		"quiz" + str(int(week)) + EXT)

def extract_hw():

	base_url = URL + "homework/homework-Win16/HW"
	saveToPath = "./Winter16/HWSol/"

	if not os.path.exists(saveToPath):
		os.makedirs(saveToPath)

	week = math.ceil((date.day - offset_date)/float(7)) 
	urllib.urlretrieve(base_url + str(int(week)) + EXT, saveToPath + "HW" +
		str(int(week)) + EXT)

if __name__ == "__main__":

	extract_prev_yr()
	extract_quiz()
	extract_hw()
