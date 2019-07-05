export CREATEPJ_HOME="$( cd "$( dirname "$0" )" && pwd )"

#!/usr/local/bin/zsh
function createpj() {
    cd ${CREATEPJ_HOME}
    pjpath=`python createpj.py $1`
    cd $pjpath
    echo "Successfully created a new project \"$1\""
    code .
}
