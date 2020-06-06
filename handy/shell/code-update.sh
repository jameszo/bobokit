#!/bin/sh

gitpull(){
    git pull origin master
}

traverse(){
    for d in `ls`
    do
        if [ -d $d/.git ]; then
            cd $d
            echo $d
            gitpull
            cd ..
        fi
    done
}

cd ~/code
traverse

cd ~/code/docker-mnt-dev
traverse
