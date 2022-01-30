#!/bin/zsh
test -f blurb-list.html && rm blurb-list.html
cat $(ls -r) > blurb-list.htmlls