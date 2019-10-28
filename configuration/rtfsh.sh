#!/bin/sh

dir_rtfsc=~/code/rtfsc

gitclone(){
    if [ -d $2 ]; then
        echo $2 exists.
    else
        git clone $1 $2
    fi
}


gitclone https://github.com/yomonah/vue-demo.git $dir_rtfsc/example/vue-demo
gitclone https://github.com/AndreiD/Flask-Easy-Template.git $dir_rtfsc/example/Flask-Easy-Template

gitclone https://github.com/spring-projects/spring-data-redis.git $dir_rtfsc/spring-data-redis
gitclone https://github.com/netty/netty.git $dir_rtfsc/netty
gitclone https://github.com/scrapy/scrapy.git $dir_rtfsc/scrapy
gitclone https://github.com/openresty/openresty.git $dir_rtfsc/openresty
gitclone https://github.com/nginx/nginx.git $dir_rtfsc/nginx

gitclone https://github.com/titansec/OpenWAF.git $dir_rtfsc/OpenWAF
gitclone https://github.com/orlabs/orange.git $dir_rtfsc/orange
