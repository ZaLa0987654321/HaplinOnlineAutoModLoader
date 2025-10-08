from git import Repo
from os import system

repo_url = "https://github.com/ZaLa0987654321/HaplinOnlineAutoModLoader.git"

system('RD /S /Q "./Cloned"')
repo = Repo.clone_from(repo_url, "Cloned")

tree = repo.head.commit.tree

print(tree["README.md"])