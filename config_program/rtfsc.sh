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

gitclone https://github.com/spring-projects/spring-data-redis.git $dir_rtfsc/spring-data-redis
gitclone https://github.com/spring-projects/spring-integration.git $dir_rtfsc/spring-integration
gitclone https://github.com/spring-projects/spring-batch.git $dir_rtfsc/spring-batch
gitclone https://github.com/spring-projects/spring-boot.git $dir_rtfsc/spring-boot
gitclone https://github.com/spring-projects/spring-data-jpa.git $dir_rtfsc/spring-data-jpa
gitclone https://github.com/Netflix/zuul.git $dir_rtfsc/zuul

gitclone https://github.com/apache/commons-pool.git $dir_rtfsc/commons-pool
gitclone https://github.com/apache/commons-lang.git $dir_rtfsc/commons-lang
gitclone https://github.com/apache/commons-io.git $dir_rtfsc/commons-io
gitclone https://github.com/apache/commons-net.git $dir_rtfsc/commons-net

gitclone https://github.com/quartz-scheduler/quartz.git $dir_rtfsc/quartz
gitclone https://github.com/netty/netty.git $dir_rtfsc/netty
gitclone https://github.com/xetorthio/jedis.git $dir_rtfsc/jedis

gitclone https://github.com/kennethreitz/requests.git $dir_rtfsc/requests
gitclone https://github.com/scrapy/scrapy.git $dir_rtfsc/scrapy
gitclone https://github.com/openresty/openresty.git $dir_rtfsc/openresty
gitclone https://github.com/titansec/OpenWAF.git $dir_rtfsc/OpenWAF
gitclone https://github.com/orlabs/orange.git $dir_rtfsc/orange

gitclone https://github.com/madrobby/zepto.git $dir_rtfsc/zepto
#----------Demo----------
gitclone https://github.com/anxpp/Java-IO.git $dir_rtfsc/example/Java-IO
gitclone https://github.com/362228416/openresty-web-dev.git $dir_rtfsc/example/openresty-web-dev
gitclone https://github.com/apache/incubator-dubbo.git $dir_rtfsc/example/incubator-dubbo
gitclone https://github.com/timboudreau/netty-http-client.git $dir_rtfsc/example/netty-http-client
gitclone https://github.com/michaelliao/learn-javascript.git $dir_rtfsc/example/learn-javascript
gitclone https://gitee.com/zhou666/spring-cloud-7simple.git $dir_rtfsc/example/spring-cloud-7simple
gitclone https://github.com/zhoutaoo/SpringCloud.git $dir_rtfsc/example/SpringCloud
gitclone https://github.com/SeptemberMaples/wechat-weapp-demo.git $dir_rtfsc/example/wechat-weapp-demo
gitclone https://github.com/royrusso/spring-mvc-rest-mockito.git $dir_rtfsc/example/spring-mvc-rest-mockito
gitclone https://github.com/AndreiD/Flask-Easy-Template.git $dir_rtfsc/example/Flask-Easy-Template
gitclone https://github.com/linyongfu2013/springboot-multi-datasource.git $dir_rtfsc/example/springboot-multi-datasource
gitclone https://github.com/spring-cloud-samples/eureka.git $dir_rtfsc/example/eureka
gitclone https://github.com/indeedeng/util.git $dir_rtfsc/example/util
gitclone https://github.com/spekdrum/junit-mockito-springboot.git $dir_rtfsc/example/junit-mockito-springboot
gitclone https://github.com/spring-cloud-samples/authserver.git $dir_rtfsc/example/authserver
gitclone https://github.com/EalenXie/SpringBoot-Quartz.git $dir_rtfsc/example/SpringBoot-Quartz
gitclone https://github.com/jzoric/spring_integration_ftp_example.git $dir_rtfsc/example/spring_integration_ftp_example
gitclone https://github.com/jirawong/Quartz-Example.git $dir_rtfsc/example/Quartz-Example
gitclone https://github.com/callicoder/java-concurrency-examples.git $dir_rtfsc/example/java-concurrency-examples
gitclone https://github.com/spring-cloud-samples/github-eureka.git $dir_rtfsc/example/github-eureka
gitclone https://github.com/spring-cloud-samples/configserver.git $dir_rtfsc/example/configserver
gitclone https://github.com/yomonah/vue-demo.git $dir_rtfsc/example/vue-demo
gitclone https://github.com/spring-cloud-samples/spring-cloud-gateway-sample.git $dir_rtfsc/example/spring-cloud-gateway-sample
gitclone https://github.com/springframeworkguru/springboot_swagger_example.git $dir_rtfsc/example/springboot_swagger_example
gitclone https://github.com/spring-cloud-samples/hystrix-dashboard.git $dir_rtfsc/example/hystrix-dashboard
gitclone https://github.com/bingyang519/wxMiniProgram.git $dir_rtfsc/example/wxMiniProgram
gitclone https://github.com/spring-cloud-samples/sample-zuul-filters.git $dir_rtfsc/example/sample-zuul-filters
gitclone https://github.com/spring-projects/spring-integration-samples.git $dir_rtfsc/example/spring-integration-samples
gitclone https://github.com/yrojha4ever/JavaStud.git $dir_rtfsc/example/JavaStud
gitclone https://github.com/epam-mooc/threadpoolexecutor-demo.git $dir_rtfsc/example/threadpoolexecutor-demo
gitclone https://github.com/AndrewMalitchuk/ftp-client.git $dir_rtfsc/example/ftp-client
gitclone https://github.com/narutom9527/Sprint_Date_JPA_houseDemo.git $dir_rtfsc/example/Sprint_Date_JPA_houseDemo
gitclone https://github.com/ryanhaveson/file-nio-sample.git $dir_rtfsc/example/file-nio-sample
gitclone https://github.com/harveyqing/BearDiary.git $dir_rtfsc/example/BearDiary
gitclone https://github.com/wxiaoqi/Spring-Cloud-Admin.git $dir_rtfsc/example/Spring-Cloud-Admin
gitclone https://github.com/ericzyh/wechat-chat.git $dir_rtfsc/example/wechat-chat
gitclone https://github.com/giscafer/wechat-weapp-mapdemo.git $dir_rtfsc/example/wechat-weapp-mapdemo
gitclone https://github.com/ketzacoatl/explore-openresty.git $dir_rtfsc/example/explore-openresty
gitclone https://github.com/RajeshPerro/FileRearWrite-Java-7.git $dir_rtfsc/example/FileRearWrite-Java-7
gitclone https://github.com/zhangkg/openresty-demo.git $dir_rtfsc/example/openresty-demo
