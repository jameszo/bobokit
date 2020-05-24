#!/bin/sh

gitpush(){
    git add ./*
    git commit -m "Save daily." .
    git push origin master
}

traverse(){
	for d in `ls`
	do
	    if [ -d $d/.git ]; then
	        cd $d
	        echo $d
	        gitpush
	        cd ..
	    fi
	done
}

cd ~/code
traverse

cd ~/code/docker-mnt-dev
traverse
