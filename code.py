import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file = open("in.txt", "r")

in_file = file.read()

splited = in_file.split("\n")
del splited[0]

for link in splited:
	print(link)

	splited_link = link.split("/")
	repository_name = splited_link[4]
	os.mkdir(ROOT_DIR + "/log_" + repository_name)
	print("created dir for " + repository_name)