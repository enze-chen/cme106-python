'''
Copied liberally from the tool by Zach del Rosario, https://github.com/zdelrosario/jupyter-authoring
Enze Chen, 2025/05/02
'''
import os 
import nbformat
import re
from time import sleep
from copy import deepcopy

def scrub_folder(dirname):
    files = os.listdir(dirname)
    for f in files:
        if f.endswith('_solu.ipynb'):

            # Process the solution notebook file
            filename_orig = os.path.join(dirname, f)
            filename_blank = filename_orig.replace('solu', 'blank')

            # load the notebook
            nb_orig  = nbformat.read(filename_orig, as_version=4)
            nb_blank = deepcopy(nb_orig)
            nb_solu  = deepcopy(nb_orig)

            for cell_id in range(len(nb_orig['cells'])):
                cell_orig = nb_orig['cells'][cell_id]
                text_blank = cell_orig['source']

                # process markdown and code cells
                if (cell_orig['cell_type'] == 'markdown') or (cell_orig['cell_type'] == 'code'):
                    text_blank = re.sub(
                        '<!-- solution-begin -->(\n|.)*?<!-- solution-end -->\n?',
                        '',
                        text_blank
                    )
                    text_blank = re.sub(
                        '# solution-begin(\n|.)*?# solution-end',
                        '',
                        text_blank
                    )

                else:
                    raise ValueError(f'Unrecognized cell type {cell_orig["cell_type"]}.')

                # write the results
                nb_blank['cells'][cell_id]["source"] = text_blank

                # remove cell outputs from code cells
                if cell_orig['cell_type'] == 'code':
                    nb_blank['cells'][cell_id]["outputs"] = []
                    nb_blank['cells'][cell_id]["execution_count"] = None


            # write blank notebook to file
            nbformat.write(nb_blank, filename_blank)

            # remove cell outputs from blank file
            # call(f"jupyter nbconvert --clear-output --inplace {filename_blank}", shell=True)

            print(f"{filename_orig.split('/')[-1]} successfully scrubbed! Blank notebook created.\n")
            sleep(0.2)


if __name__ == '__main__':
    scrub_folder(os.path.join("cme106-python", "workbook"))
    scrub_folder(os.path.join("cme106-python", "tutorials"))

