#!/bin/bash 

echo "# webserver" >> README.md
git init
git add *
git commit -m "first commit"
git remote add origin https://github.com/sairagh/webserver.git
git push -u origin master
