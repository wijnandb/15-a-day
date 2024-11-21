#!/bin/bash

while [ -n "$1" ]; do # while loop starts

	case "$1" in

	-a) echo "-a option passed" ;; # Message for -a option

	-b) echo "-b option passed" ;; # Message for -b option

	-c) echo "-c option passed" ;; # Message for -c option

	*) echo "Option $1 not recognized" ;; # In case you typed a different option other than a,b,c

	esac

	shift
# idea of these option was that I could specify for which site I wanted to create a new post
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

year=$(date +%Y)
month=$(date +%m)
timestamp=$(date +%Y-%m-%dT%H:%M:%S%z)
# Define the directory path
directory="content/posts/$year/$month"

# Create the directory if it doesn't exist
mkdir -p "$directory"

filename="${HOME}/sites/15-a-day/content/posts/$year/$month/${slug}.md"

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
cd /${HOME}/sites/15-a-day/ 
hugo server -D --buildDrafts
