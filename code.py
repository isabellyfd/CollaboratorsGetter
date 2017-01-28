import os
from git import Repo

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

file = open("in.txt", "r")

in_file = file.read()

splited = in_file.split("\n")
del splited[0]

for link in splited:
	print(link)

	splited_link = link.split("/")
	repository_name = splited_link[4]

	dir = ROOT_DIR + "/log_" + repository_name

	os.mkdir(dir)
	print("created dir for " + repository_name)
	Repo.clone_from(link, dir)