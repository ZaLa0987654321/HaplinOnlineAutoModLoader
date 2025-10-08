from git import Repo
from os import system
import os

repo_url = "https://github.com/ZaLa0987654321/HaplinOnlineAutoModLoader.git"

system('RD /S /Q "./Cloned"')
repo = Repo.clone_from(repo_url, "Cloned")

tree = repo.head.commit.tree

for f in tree["mods"]:
	print(os.path.splitext(f.path))