#!/bin/bash

cd ./src/images/favourites
ls

for i in $(ls -r *.jpg)
do
    cat >> ./images.html <<HTML
	    <div href="#img_$i" class="photos-image" style="background-image: url(images/favourites/$i);">
	      <a href="#img_$i" class="photos-cover">
		<p>$(exiftool -s -s -s -Caption "$i")</p>
	      </a>
	    </div>

	    <a href="#_" class="lightbox" id="img_$i">
	      <div class="lightbox-image" style="background-image: url(images/favourites/$i)"></div>
	      <img href="#_" class="lightbox-close" src="svg/close.svg"></svg>
	    </a>

HTML
done

cd -
