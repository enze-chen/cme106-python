# CME 106 Python Workbook

© [Enze Chen](https://mse.stanford.edu/people/enze-chen), 
[Vadim Khayms](https://icme.stanford.edu/people/vadim-khayms)

Python version of MATLAB exercises for CME 106 at Stanford University.

Access it through our [Jupyter Book](https://enze-chen.github.io/cme106-python/)!


## For instructors

Here's what Enze's convoluted process entails (if you don't like it, feel free to use your own):
1. Clone the repo and ask Enze or Vadim for the solution Python notebooks.
1. Move the solution notebooks into their proper folders (workbook or tutorials).
Files ending in `_solu.ipynb` will be ignored by git.
1. Anytime you modify the solutions, update the `_blank` notebooks (what is actually compiled in the Jupyter Book) by running from _above_ the root folder: `python cme106-python/assets/make_blank_nb.py`.
1. Run a full build of the Jupyter Book from above the root folder: `jb build cme106-python --all`.
1. Enter the root folder and publish to GitHub pages: `ghp-import -n -p -f _build/html`.
1. Don't forget to commit+push changes as needed to keep the Github up to date (but this doesn't change what students see).
1. If you want to compile the solution notebooks as PDFs, use the `convert_pdf.py` file: 
```
python convert_pdf.py {path_to_solution_notebooks} -n {merged_pdf_name.pdf}
```

[![CC BY-NC 4.0][cc-by-nc-image]][cc-by-nc]

[cc-by-nc]: http://creativecommons.org/licenses/by-nc/4.0/
[cc-by-nc-image]: https://licensebuttons.net/l/by-nc/4.0/88x31.png
