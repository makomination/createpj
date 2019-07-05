export CREATEPJ_HOME="$( cd "$( dirname "$0" )" && pwd )"

#!/usr/local/bin/zsh
function createpj() {
    cd ${CREATEPJ_HOME}
    pjpath=`python createpj.py $1`
    cd $pjpath
    git init
    git remote add origin git@github.com:${GITHUB_USERNAME}/$1.git
    touch README.md
    touch .gitignore
    git add .
    git commit -m 'initial commit'
    git push -u origin master
    code .
}
