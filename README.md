# createpj
Type `createpj <Your new project name>` in your terminal!!\
Automate all your tasks that are needed to create your new empty project folder with creating empty README and .gitignore, and carry out initial git setup on your local machine.\
Also, create new project remote github repository and push to it.\
Finally, open your project in vscode.

## Prerequisites
Required to use **BASH** or **ZSH**.\
Neccesary to install below and add them to path(named python and pip respectively).
* Python 3
* pip

## Install
```zsh
git clone "git@github.com:makomination/createpj.git"
cd createpj
pip install -r requirements.txt
code .env
# Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.
source .my_commands.sh
```

## Usage
To run the script type in 
```zsh
createpj <name of your new project>
```

## Env File Format
```zsh
GITHUB_USERNAME="Username123"
GITHUB_PASSWORD="Password123"
MYPROJECTS_HOME="/path/to/your/project"
```
## Built With
* Python3.7.3
* zsh
