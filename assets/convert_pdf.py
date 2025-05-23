'''
Script for converting solution notebooks to PDF files.
'''
import os
import argparse
from subprocess import call


def main(folder, name):
    files = [x for x in os.listdir(folder) if x.endswith('_solu.ipynb')]
    for f in files:
        call(f"jupyter nbconvert --to pdf {os.path.join(folder, f)}", shell=True)

    if name:
        print("Attempting to merge PDFs...")
        from pypdf import PdfWriter
        merger = PdfWriter()
        files = sorted([x for x in os.listdir(folder) if x.endswith('_solu.pdf')])
        for pdf in files:
            merger.append(os.path.join(folder, pdf))
        merger.write(os.path.join(folder, name))
        merger.close()
        print("PDFs successfully merged!")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Available options.")
    parser.add_argument('folder', type=str, help="Enter the folder of the notebooks to process.")
    parser.add_argument('-n', '--name', type=str, default='', \
                        help="Enter the name of the merged PDF. Requires pypdf.")
    args = parser.parse_args()
    main(args.folder, args.name)