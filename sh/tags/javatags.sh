#!/bin/bash

find . -name "*.java" | xargs ctags -L -
