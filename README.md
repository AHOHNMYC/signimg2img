# signimg2img

Convert signed Android images (-sign.img) into standard Android Images (.img)

## Fork reasons

[Original](https://github.com/R0rt1z2/signimg2img) package once eat all of my memory while copying image.
So I investigated sources and find a bunch of absolutely bad stuff (loading heavy files (2-4 GiB) into memory without need,
dependency on Linux-specific `dd` utility) and absolutely unrelated to script's main purpose (silent file deletion,
silent mounting).  
Then I was killed by literal `Windows is unable to unpack images with SSSS header!`  

So, I removed everything not related to header cutting. Welcome to the sources.  
Also now you may use this tool with pipes. Details inside.

## Requirements
This script requires Python 3.6+ installed on your system.

## Supported headers
* BFBF
* SSSS

## License
* This program is licensed under the GNU General Public License (v3). See `LICENSE` for details.

## Other information
* To sign modified images you can use MediaTek's propietary tools: https://github.com/R0rt1z2/vendor_mediatek_signtool
* There is another utility for same purpose [FbWinTools](http://lenovo-forums.ru/topic/16469--/).
It can pack unpacked images back.
* After removing sing header, you may want to desparse image. Use [simg2img](https://github.com/anestisb/android-simg2img).
My builds for Windows are located [there](https://github.com/AHOHNMYC/android-simg2img/releases).