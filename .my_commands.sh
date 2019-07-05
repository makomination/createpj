if [[ $SHELL =~ "zsh" ]]; then
    export CREATEPJ_HOME="$( cd "$( dirname "$0" )" && pwd )"
elif [[ $SHELL =~ "bash" ]]; then
    export CREATEPJ_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
else
    export CREATEPJ_HOME="$( cd "$( dirname "$0" )" && pwd )"
fi

function createpj() {
    cd ${CREATEPJ_HOME}
    pjpath=`python createpj.py $1`
    cd $pjpath
    echo "Successfully created a new project \"$1\""
    code .
}
