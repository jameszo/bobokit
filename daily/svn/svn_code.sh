#!/bin/bash

usage(){
    echo "usage: ./svn_code.sh -s [svn url] -n [project name] -v [svn version]"
    exit 1
}

svn_version=HEAD
project_name=app_code
base_dir=./code
while getopts "s:n:v:" opt
do
    case $opt in
        s) svn_url=$OPTARG
            ;;
        n) project_name=$OPTARG
            ;;
        v) svn_version=$OPTARG
            ;;
        ?) usage ;;
    esac
done

if [ ! -d $base_dir ]; then
    mkdir -p $base_dir
fi

cd $base_dir
if [ -d $project_name ]; then
    rm -rf $project_name
fi
echo no | svn export --username abc --password 123  -r $svn_version $svn_url $project_name

cd $project_name
