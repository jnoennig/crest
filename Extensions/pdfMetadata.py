#encoding: utf-8

'''
Shows PDF metadata
'''

import appex
import PyPDF2
from PyPDF2 import PdfFileReader

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    pdfs = appex.get_attachments(uti='public.data')
    if pdfs:
        pdf_file = PdfFileReader(open(pdfs[0], "rb"))
        if pdf_file:
            metadata = pdf_file.getDocumentInfo()
            for k, v in metadata.items():
                if type(v) == PyPDF2.generic.IndirectObject:
                    print('{0} - {1}'.format(k, metadata[k]))
                else:
                    print('{0} - {1}'.format(k, v))
        else:
            print('No metadata found')
    else:
        print('No input PDF found')

if __name__ == '__main__':
    main()