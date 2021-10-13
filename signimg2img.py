#!/usr/bin/env python3
import pathlib
import sys

if __name__ == '__main__':
    print = lambda s: sys.stderr.write(s+'\n')

    if len(sys.argv) != 3:
        print('                     signimg2img v0.1')
        print('Script for removing FBFB and SSSS headers from Android image files')
        print('          https://github.com/AHOHNMYC/signimg2img')
        print('')
        print('USAGE:   signimg2img.py <signed_image> <raw_image_file>')
        print('EXAMPLE: signimg2img.py image-sign.img image.img')
        print('             take image-sign.img, process, save as image.img')
        print('         signimg2img.py - -')
        print('             take data from stdin, send to stdout')
        exit(1)

    if not sys.argv[1] == '-':
        if not pathlib.Path(sys.argv[1]).exists():
            print('Input file does not exists. Exiting')
            exit(1)

    if not sys.argv[2] == '-':
        if pathlib.Path(sys.argv[2]).exists():
            print('Output file already exists. Exiting')
            exit(1)

    in_file = sys.stdin.buffer if sys.argv[1] == '-' else open(sys.argv[1], 'rb')
    out_file = sys.stdout.buffer if sys.argv[2] == '-' else open(sys.argv[2], 'wb')

    header = in_file.read(4)

    # -4 because we have read those bytes already
    if header == b'BFBF':
        # After 0x4000 BFBF header goes 0x40 SSSS header. Cut 'em both!
        in_file.read(0x4000+0x40 -4)
    elif header == b'SSSS':
        in_file.read(0x40 -4)
    else:
        print(f"Unknown image header: {header.decode(errors='ignore')} ({header})")
        print('Known headers are: BFBF, SSSS')
        print('Try more powerful tool: Android Image Kitchen https://forum.xda-developers.com/t/2073775/')
        exit(1)

    # Copy by 16 MiB chunk
    while out_file.write(in_file.read(16 * 1024 * 1024)):
        pass
    out_file.flush()

    print('Headers removed successfully!')
    print('Now you may desparse *system* image using simg2img tool: https://github.com/anestisb/android-simg2img')
    if sys.platform.startswith('win'):
        print('Unofficial Windows builds: https://github.com/AHOHNMYC/android-simg2img/releases')
