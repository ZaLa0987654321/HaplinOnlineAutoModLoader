from git import Repo
import git
from os import system
import os

repo_url = "https://github.com/ZaLa0987654321/HaplinOnlineAutoModLoader.git"
repo = None

if not os.path.isdir('Cloned'):
	repo = Repo.clone_from(repo_url, "Cloned")
else:
	repo = Repo("Cloned")

tree = repo.head.commit.tree

remote = git.remote.Remote(repo, "origin")

added_files = []
deleted_files = []

for i in remote.fetch():
	[added_files.append(f.a_blob) for f in i.commit.diff(repo.head.commit)]
	[deleted_files.append(f.b_blob) for f in i.commit.diff(repo.head.commit)]

print("Added:", added_files)
print("Deleted:", deleted_files)

for f in added_files:
	if f is not None:
		with open("Cloned\\" + f.path, "wb") as af:
			af.write(f.data_stream.read())
			print(" + " + f.path)

for f in deleted_files:
	if f is not None:
		os.remove("Cloned\\" + f.path)
		print(" - " + f.path)

repo.head.reset(str(remote.fetch()[0].commit), index=True, working_tree=True)
tree = repo.head.commit.tree

print("-"*10 + "Current Local Repo Mods" + "-"*10)

for f in tree["mods"]:
	_, ext = os.path.splitext(f.path)
	if ext == ".jar":
		print(" = " + f.path)