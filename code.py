import os, subprocess
from git import Repo

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
print(ROOT_DIR)

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

    Repo.clone_from(link, dir, branch="master")

    print("cloned repository " +repository_name)

    os.chdir(dir)
    os.system("git log --format=format:\'Author name: %an %aN Author adress: %ae %aE  %ce %cE\' | sort | uniq -c | sort -nr | head -50 > log.txt")

    os.chdir(ROOT_DIR)


