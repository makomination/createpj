# createpj

Create your new empty project folder with creating empty README and .gitignore, and do initial git setup on your local machine.\
Also, create new project remote github repository and push to it.\
Finally, open your project in vscode.


## Install: 
```zsh
git clone "git@github.com:makomination/createpj.git"
cd createpj
pip install -r requirements.txt
code .env
# Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.
source .my_commands.sh
```

## Usage:
To run the script type in 
```zsh
createpj <name of your new project>
```

## Env File Format:
```zsh
GITHUB_USERNAME="Username123"
GITHUB_PASSWORD="Password123"
MYPROJECTS_HOME="/path/to/your/project"
```
