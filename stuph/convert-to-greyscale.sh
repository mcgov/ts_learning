echo here we go
for j in $( ls );
		## look through the contents of the subfolders...
		do
		echo $j
		
		 extension=`echo "$j" | cut -d'.' -f2`
		 filename=`echo "$j" | cut -d'.' -f1`
		 output=$filename"_gray"
		 echo "$output"
		 if [ "$extension" = "png" ]; then
				convert $filename.png -modulate 100,2,100 -colorspace RGB $output.png ## convert the image to grayscale

			fi
		done	