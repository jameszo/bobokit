#!/bin/bash

uml_path=`pwd`
base_path=$(cd `dirname $0`; pwd)
cd ${uml_path}

java -jar ${base_path}/plantuml.jar -tpng $@  -o .
