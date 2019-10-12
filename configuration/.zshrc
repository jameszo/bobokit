ZSH_THEME="ys"
export ZSH=$HOME/.oh-my-zsh
source $ZSH/oh-my-zsh.sh
export HOME="/Users/James"

DEFAULT_USER="BoBoBo"

plugins=(git autojump)
bindkey -v

[[ -s ${HOME}/.autojump/etc/profile.d/autojump.sh ]] && source ${HOME}/.autojump/etc/profile.d/autojump.sh
alias tree="find . ! -path '*svn*' ! -path '*lib*' ! -path '*target*' ! -path '*class' ! -path '*pyc' ! -path '*idea*' ! -path '*swp' ! -path '*iml' | sed -e 's;[^/]*/;|____;g;s;____|; |;g'"
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

export LC_ALL=en_US.UTF-8  
export LANG=en_US.UTF-8
export PATH="${HOME}/maven3/bin:${HOME}/code/bobokit/sh:/usr/bin/svn:/usr/local/mysql/bin:/usr/local/sbin:$PATH"

#export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.7.0_79.jdk/Contents/Home
export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_05.jdk/Contents/Home
#export JAVA_OPTS="-Xdebug -Xrunjdwp:transport=dt_socket,address=8008,server=y,suspend=y"
export JRE_HOME=${JAVA_HOME}/jre
export CLASSPATH=.:${JAVA_HOME}/lib:${JRE_HOME}/lib
export MAVEN_OPTS="-Xms1024m -Xmx3024m"

export PYTHONPATH=${HOME}/code

export LDFLAGS="-L/usr/local/opt/node@10/lib"
export CPPFLAGS="-I/usr/local/opt/node@10/include"
export PATH="/usr/local/opt/node@10/bin:$PATH"
