#!/bin/sh

gitpull(){
    git pull origin master
}

cd ~/code
for d in `ls`
do
    if [ -d $d/.git ]; then
        cd $d
        echo $d
        gitpull
        cd ..
    fi
done
