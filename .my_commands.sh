#!/usr/local/bin/zsh
function createpj() {
    cd
    python createpj.py $1
    cd /PATH/TO/YOUR_PROJECT/$1
    git init
    git remote add origin git@github.com:YOUR_USERNAME/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m 'initial commit'
    git push -u origin master
    code .
}
