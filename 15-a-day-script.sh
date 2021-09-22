#!/bin/bash

while [ -n "$1" ]; do # while loop starts

	case "$1" in

	-a) echo "-a option passed" ;; # Message for -a option

	-b) echo "-b option passed" ;; # Message for -b option

	-c) echo "-c option passed" ;; # Message for -c option

	*) echo "Option $1 not recognized" ;; # In case you typed a different option other than a,b,c

	esac

	shift

done
echo "What's the name of todays post?"
read title

echo "Which tags do you want to include?"
echo "(put quotes around indivual tags and seperate with comma's)"
echo "Like this: \"tag1\", \"tag2\", \"tag3\""
read tags

#echo "The downcased title with hyphens is:"
#echo "$title"     | iconv -t ascii//TRANSLIT | sed -r s/[^a-zA-Z0-9]+/-/g | sed -r s/^-+\|-+$//g | tr A-Z a-z
slug="$(echo -n "${title}" | iconv -t ascii//TRANSLIT | sed -r s/[^a-zA-Z0-9]+/-/g | sed -r s/^-+\|-+$//g | tr A-Z a-z)"

echo "Converted title of post is:"
echo "$slug"

#today=`date +%Y-%m-%d`
#echo "Today is:"
#echo "$today"
#echo "And the time today is:"
timestamp=`date +%Y-%m-%dT%T%z`
echo "$timestamp"

#opslaan="${today}-${slug}"
#echo "$opslaan"
filename="${HOME}/sites/github/15-a-day-hugo/content/posts/${slug}.md"

echo "Creating file: ${filename}"

touch $filename


#echo $timestamp

echo "--- " >> $filename
echo "draft: true" >> $filename
echo "title:" \"$title\" >> $filename
echo "date:" \"$timestamp\" >> $filename
echo "layout: post" >> $filename
echo "tags: [$tags]" >> $filename
echo "slug:" \"$slug\" >> $filename
echo "---" >> $filename
echo >> $filename
echo >> $filename

code $filename

# cd into directory where site reides and run hugo 
cd /${HOME}/sites/github/15-a-day-hugo/ 
hugo server -D
xdg-settings set default-web-browser chrome.desktop
chrome "http://localhost:1313/posts"
