import sys
import os
import git
from github import Github
from dotenv import load_dotenv
from pathlib import Path


def createpj(pjName):
    """
    1. create a new remote git repository on github
    2. make a new project folder
    3. initialize local git repository and push
    :param pjName: str new project name
    :return pjpath: str  path for new project
    """
    load_dotenv(dotenv_path=Path(os.getenv('CREATEPJ_HOME'))/'.env')
    user = Github(os.getenv('GITHUB_USERNAME'),
                  os.getenv('GITHUB_PASSWORD')).get_user()
    user.create_repo(pjName)
    pjpath = Path(os.getenv("MYPROJECTS_HOME")) / pjName
    os.mkdir(pjpath)
    open(pjpath / 'README.md', 'a').close()
    open(pjpath / '.gitignore', 'a').close()
    git.Repo.init(pjpath)
    localRepo = git.Repo(pjpath)
    localRepo.index.add(['README.md', '.gitignore'])
    localRepo.index.commit('initial commit')
    origin = localRepo.create_remote(
        'origin', 'git@github.com:' + os.getenv('GITHUB_USERNAME') + '/'
        + pjName + '.git')
    origin.push('master', u=True)

    return pjpath


if __name__ == "__main__":
    pjpath = createpj(sys.argv[1])
    print(pjpath)
