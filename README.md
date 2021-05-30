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
r0rt1z2@r0rt1z2: /signimg2img$ python3 signimg2img.py -u recovery-sign.img
signimg2img binary - version: 1.5

[signimg2img-log] Selected image: recovery-sign.img
[signimg2img-log] Image header: b'BFBF'
[signimg2img-log] Image header string: 'recovery' (0x000010)
[signimg2img-log] Removing old files...
[signimg2img-log] Deleting the header...
[signimg2img-log] Done, image extracted as recovery.img

r0rt1z2@r0rt1z2: /signimg2img$
```

## Supported headers
* BFBF
* SSSS

## License
* This program is licensed under the GNU General Public License (v3). See `LICENSE` for details.