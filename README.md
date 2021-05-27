# signimg2img
![GitHub](https://img.shields.io/github/license/R0rt1z2/signimg2img)
![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/R0rt1z2/signimg2img?include_prereleases)

Convert signed Android images (.img-sign) into standard Android Images (.img)

## Requirements
This binary requires Python 3 or newer installed on your system. 
It currently supports Windows, Linux and MacOS architectures.

## Usage
```
signimg2img.py -u <signed_image>
signimg2img.py -o <signed_image>
signimg2img.py -c
```
- `<signed_image>` = input, image-sign.img

## Example
This is a simple example on a Linux system: 
```
r0rtiz2@r0rtiz2:~/signimg2img$ python3 signimg2img.py -u system-sign.img

signimg2img binary - version: 1.4

[signimg2img-log] Selected: Unpack system-sign.img
[signimg2img-log] Header is SSSS: 1397969747
[signimg2img-log] Removing old files if they're present...
[signimg2img-log] Getting the offset...
[signimg2img-log] Got 1885696592 as offset!
[signimg2img-log] Deleting the header...
[signimg2img-log] Header remove complete!
[signimg2img-log] Converting to ext4 image...
[signimg2img-log] Unpacking system image...
[signimg2img-log] system-sign.img extracted at system_out

r0rtiz2@r0rtiz2:~/signimg2img$ 
```

## Supported headers
* BFBF
* SSSS

## License
* This program is licensed under the GNU General Public License (v3). See `LICENSE` for details.