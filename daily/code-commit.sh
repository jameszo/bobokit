#!/bin/sh

gitpush(){
    git add ./*
    git commit -m "Save daily." .
    git push origin master
}

cd ~/code
for d in `ls`
do
    if [ -d $d/.git ]; then
        cd $d
        echo $d
        gitpush
        cd ..
    fi
done
