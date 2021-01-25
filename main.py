import os
from pdf2image import convert_from_path, convert_from_bytes
import tempfile

from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)


pdf_images = os.listdir('pdf_images')
tiff_images = os.listdir('tiff_images')

def convert_pdf_to_tiff():
    # pdf_images.save('test.Tiff', 'TIFF')
    # images = convert_from_bytes(open(pdf_images, 'rb').read())
    with tempfile.TemporaryDirectory() as path:
        images = convert_from_path('./pdf_images/1.pdf', output_folder='./tiff_images')
        print('pdf converted')
        return images

if __name__ == '__main__':
    convert_pdf_to_tiff()































#
# def convert_pdf_to_tiff(directory_path: str, img_name: str):
#     # convert PDF to TIFF
#     images_from_path = convert_from_path('/pdf_images', output_folder=tiff_images)
#     # save tiff in tiff_images
#     print('pdf converted')
#
# if __name__ == '__main__':
#     convert_pdf_to_tiff('pdf_image', '1.jpeg')
