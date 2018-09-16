#encoding: utf-8

'''
Hashes files using md5
'''

import appex
import hashlib
import clipboard


def md5_hash(file_path):
    try:
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except:
        return "Error the file was not hashed."

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    myfile = appex.get_attachments('public.data')[0]
    if myfile:
        md5 = md5_hash(myfile)
        print('md5: {}\n'.format(md5))
        clipboard.set(md5)
        print('The md5 hash has been copied to the clipboard.')

if __name__ == '__main__':
    main() 