#!/bin/zsh
index=~/personal-site/www/index.html
layout=~/personal-site/layout
test -f $index && rm $index
touch $index
for h3 in $(ls $layout); do
  echo "<h3>${h3//[-0-9]/}</h3>" >> $index;
    for link in $layout/$h3; do
      for link2 in $(ls $link); do
        echo "<a href="$h3/$link2">${${link2//[0-9]/ }//-/ }</a>" >> $index;
      done;
    done;
done;


orig="AxxBCyyyDEF-zzLMN"
mod=${orig//[-]/ }
echo $mod