#encoding: utf-8

'''
Hashes files using sha256
'''

import appex
import hashlib
import clipboard


def sha256_hash(file_path):
    try:
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    except:
        return "Error the file was not hashed."

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    myfile = appex.get_attachments('public.data')[0]
    if myfile:
        sha256 = sha256_hash(myfile)
        print('sha256: {}\n'.format(sha256))
        clipboard.set(sha256)
        print('The sha256 hash has been copied to the clipboard.')

if __name__ == '__main__':
    main() 