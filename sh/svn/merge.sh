#!/bin/bash

echo "Merge svn directory:"
read svn_dir
echo "Merge version:"
read check_version
echo "Merge domains:"
read domains

merge(){
    directory=$1
    url_merge_to=$2
    url_merge_from=$3
    merge_version=$4
    echo "Checking $url_merge_to ..."
    check_result=`svn diff $url_merge_from $url_merge_to | grep @@`
    if [ "$check_result" != "" ];
    then
        echo "Merging $url_merge_from >>>"
        echo ">>> $url_merge_to"

        mkdir ${directory}
        cd ${directory}
        output=`svn co $url_merge_to .`

        start_version=`svn log --stop-on-copy $url_merge_from | tail -4 | awk 'NR==1{print $1}'`
        start_version=${start_version//r/}

        output=`svn merge $url_merge_from@$start_version $url_merge_from .`
        echo "Merged from version: $start_version"
        echo $output > merge_content

        output=`svn commit -m "merge $merge_version" .`

        end_version=`svn log | head -2 | awk 'NR==2{print $1}'`
        end_version=${end_version//r/}
        start_version=`svn log | head -6 | awk 'NR==6{print $1}'`
        start_version=${start_version//r/}
        svn diff -r $end_version:$start_version >> merge_content

        check_result=`svn diff $url_merge_to $url_merge_from | grep @@`
        if [ "$check_result" = "" ];
        then
            echo "Merge Successfully."
        else
            svn diff $url_merge_to $url_merge_from >> ../fail_merge_detail
            echo "Merge $url_merge_from failed!!!"
        fi
        cd ..
    else
        svn diff $url_merge_from $url_merge_to >> skip_merge_detail
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
    merge develop_$line $url_merge_to $url_merge_from $check_version

    url_merge_from=http://172.16.0.72/svn/$svn_dir/branches/develop/$line
    url_merge_to=http://172.16.0.72/svn/$svn_dir/trunk/$line
    merge trunk_$line $url_merge_to $url_merge_from $check_version
done


