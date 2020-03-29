#!/bin/bash

target=server
if [ "$1" != "" ]; then
    target=$1
fi

# 生成私钥
openssl genrsa -out ${target}.key 1024
# 生成公钥
openssl rsa -in ${target}.key -pubout -out ${target}.pem
