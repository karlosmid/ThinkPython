for line in $(cat $1)
do
	chromium-browser --new-tab $line
done
