#!/bin/sh

dir_rtfsc=~/code/rtfsc

gitclone(){
    if [ -d $2 ]; then
        echo $2 exists.
    else
        git clone $1 $2
    fi
}

gitclone https://github.com/pallets/flask.git $dir_rtfsc/flask
gitclone https://github.com/openjdk/jdk.git $dir_rtfsc/openjdk
gitclone https://github.com/loveveryday/linux0.11.git $dir_rtfsc/linux0.11
gitclone https://github.com/nginx/nginx.git $dir_rtfsc/nginx
gitclone https://github.com/kennethreitz/requests.git $dir_rtfsc/requests
gitclone https://github.com/madrobby/zepto.git $dir_rtfsc/zepto
gitclone https://github.com/titansec/OpenWAF.git $dir_rtfsc/OpenWAF
gitclone https://github.com/openresty/openresty.git $dir_rtfsc/openresty
gitclone https://github.com/ethereum/go-ethereum.git $dir_rtfsc/go-ethereum

gitclone https://github.com/spring-projects/spring-framework.git $dir_rtfsc/spring-framework
gitclone https://github.com/spring-projects/spring-boot.git $dir_rtfsc/spring-boot

#gitclone https://github.com/spring-projects/spring-data-redis.git $dir_rtfsc/spring-data-redis
#gitclone https://github.com/spring-projects/spring-batch.git $dir_rtfsc/spring-batch
#gitclone https://github.com/spring-projects/spring-data-jpa.git $dir_rtfsc/spring-data-jpa
#gitclone https://github.com/spring-projects/spring-integration.git $dir_rtfsc/spring-integration

#gitclone https://github.com/apache/commons-pool.git $dir_rtfsc/commons-pool
#gitclone https://github.com/apache/commons-lang.git $dir_rtfsc/commons-lang
#gitclone https://github.com/apache/commons-io.git $dir_rtfsc/commons-io
#gitclone https://github.com/apache/commons-net.git $dir_rtfsc/commons-net

#gitclone https://github.com/Netflix/zuul.git $dir_rtfsc/zuul
#gitclone https://github.com/quartz-scheduler/quartz.git $dir_rtfsc/quartz
#gitclone https://github.com/netty/netty.git $dir_rtfsc/netty
#gitclone https://github.com/xetorthio/jedis.git $dir_rtfsc/jedis
#gitclone https://github.com/scrapy/scrapy.git $dir_rtfsc/scrapy

gitclone https://github.com/lingthio/Flask-User.git $dir_rtfsc/example/Flask-User
gitclone https://github.com/Alexmod/Flask-User-and-Flask-admin.git $dir_rtfsc/example/Flask-User-and-Flask-admin
