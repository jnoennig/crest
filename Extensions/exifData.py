#encoding: utf-8

'''
Shows photo EXIF data
'''

import appex
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    images = appex.get_attachments('public.jpeg')
    if images:
        a = get_exif(images[0])
        if a:
            print('EXIF data:')
            for k, v in a.items():
                print('{0}: {1}'.format(k, v))
            else:
                print('No exif data found')
    else:
        print('No input image found')

if __name__ == '__main__':
    main()