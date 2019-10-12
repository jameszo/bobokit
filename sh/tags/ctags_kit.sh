#!/bin/bash

ctags --totals=yes -f /Users/James/code/tags/kit.tags -R /Users/James/code/kit/py/ --exclude=+.pyc,+.swp,+.md,LISENCE
