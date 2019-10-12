#!/bin/bash

echo "Merge svn directory:"
read svn_dir
echo "Merge version:"
read check_version
echo "Merge domains:"
read domains

get_branch_commit(){
    url_merge_from=$1
    merge_version=$2

    start_version=`svn log --stop-on-copy $url_merge_from | tail -4 | awk 'NR==1{print $1}'`
    start_version=${start_version//r/}

    echo "svn diff --old=$url_merge_from@${start_version} --new=$url_merge_from" 
    echo "-----------------$url_merge_from-----------------" >> branch_commit
    svn diff --old=$url_merge_from@${start_version} --new=$url_merge_from >> branch_commit
}

if [ "$domains" = "" ];then
    domains=`svn list http://172.16.0.72/svn/$svn_dir/branches/release/release_$check_version`
fi
for line in $domains
do
    line=${line//\//}
    url_merge_from=http://172.16.0.72/svn/$svn_dir/branches/release/release_$check_version/$line
    get_branch_commit $url_merge_from $check_version
done


