#!/bin/bash

find . -name "*.go" | xargs gotags -L - -f tags
