import sys
import os
from github import Github
from dotenv import load_dotenv
from pathlib import Path


def createpj(pjName):
    """
    1. create a new remote git repository on github
    2. make a new project folder
    :param pjName: str new project name
    """
    load_dotenv(dotenv_path=Path(os.getenv('CREATEPJ_HOME'))/'.env')
    user = Github(os.getenv('GITHUB_USERNAME'),
                  os.getenv('GITHUB_PASSWORD')).get_user()
    user.create_repo(pjName)
    print("Successfully created a repository {}".format(pjName))
    pjFolder = Path(os.getenv("MYPROJECTS_HOME")) / pjName
    os.mkdir(pjFolder)
    os.chdir(pjFolder)


if __name__ == "__main__":
    createpj(sys.argv[1])
