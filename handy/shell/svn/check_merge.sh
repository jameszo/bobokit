#!/bin/bash

echo "Merge svn directory:"
read svn_dir
echo "Merge version:"
read check_version
echo "Merge domain:"
read domains

check_merge(){
    dst=$1
    url_merge_to=$2
    url_merge_from=$3
    merge_version=$4
    echo "Checking $url_merge_to ..."
    check_result=`svn diff $url_merge_from $url_merge_to | grep @@`
    if [ "$check_result" != "" ];
    then
        echo "Diff !!!"
        svn diff $url_merge_from $url_merge_to >> check_diff_$dst
    else
        echo "No need to merge $url_merge_from"
    fi
}

if [ "$domains" = "" ];then
    domains=`svn list http://172.16.0.72/svn/$svn_dir/branches/release/release_$check_version`
fi
for line in $domains
do
    line=${line//\//}
    url_merge_to=http://172.16.0.72/svn/$svn_dir/branches/develop/$line
    url_merge_from=http://172.16.0.72/svn/$svn_dir/branches/release/release_$check_version/$line
    check_merge develop_$line $url_merge_to $url_merge_from $check_version

    url_merge_from=http://172.16.0.72/svn/$svn_dir/branches/develop/$line
    url_merge_to=http://172.16.0.72/svn/$svn_dir/trunk/$line
    check_merge trunk_$line $url_merge_to $url_merge_from $check_version
done


