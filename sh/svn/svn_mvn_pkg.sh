#!/bin/bash

usage(){
    echo "usage: ./svn_mvn_pkg.sh -s [svn url] -n [project name] -v [svn version] -g [package name] -o [output dir]"
    exit 1
}

svn_version=HEAD
project_name=app_code
base_dir=./tmp
while getopts "s:n:b:v:g:o:" opt
do
    case $opt in
        s) svn_url=$OPTARG
            ;;
        n) project_name=$OPTARG
            ;;
        v) svn_version=$OPTARG
            ;;
        g) pkg_name=$OPTARG
            ;;
        o) output_dir=$OPTARG
            ;;
        ?) usage ;;
    esac
done

if [ '$pkg_name' == '' ]; then
    pkg_name = $project_name;
fi

if [ ! -d $base_dir ]; then
    mkdir -p $base_dir
fi

cd $base_dir
if [ -d $project_name ]; then
    rm -rf $project_name
fi
echo no | svn export --username integrationuser --password integrationp@dswerd  -r $svn_version $svn_url $project_name

cd $project_name
mvn clean package
if [ $? -ne 0 ]; then
    echo "Failed mvn package!!!"
    exit 1
fi
cd ..

pkg_file=`find . -name "${pkg_name}"`

mv ${pkg_file} $output_dir
