#encoding: utf-8

'''
Hashes files using sha1
'''

import appex
import hashlib
import clipboard


def sha1_hash(file_path):
    try:
        hash_sha1 = hashlib.sha1()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha1.update(chunk)
        return hash_sha1.hexdigest()
    except:
        return "Error the file was not hashed."

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    myfile = appex.get_attachments('public.data')[0]
    if myfile:
        sha1 = sha1_hash(myfile)
        print('sha1: {}\n'.format(sha1))
        clipboard.set(sha1)
        print('The sha1 hash has been copied to the clipboard.')

if __name__ == '__main__':
    main() 