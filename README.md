# Duke MIDS

Source for [dukemids.com](https://dukemids.com) — a collection of resources for Duke MIDS students.

Built with [MyST Markdown](https://mystmd.org) / Jupyter Book 2 and served via GitHub Pages from the `docs/` folder.

## Setup

```bash
conda env create -f environment.yml
```

## Building the site

```bash
conda run -n dukemids jupyter-book build --html
cp -R _build/html/* docs/
```

Full one-liner:

```bash
conda run -n dukemids jupyter-book build --html; cp -R _build/html/* docs; git add .; git commit; git push
```
