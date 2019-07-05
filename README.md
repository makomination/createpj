### Install: 
```zsh
git clone "git@github.com:makomination/createpj.git"
cd createpj
pip install -r requirements.txt
code .env
Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.
source ./.my_commands.sh
```

### Usage:
```zsh
To run the script type in 'create <name of your folder>'
```

### Env File Format:
```zsh
GITHUB_USERNAME="Username123"
GITHUB_PASSWORD="Password123"
MYPROJECTS_HOME="/path/to/your/project"
```