# Duke MIDS

Source for [dukemids.com](https://dukemids.com) — a collection of resources for Duke MIDS students.

Built with [MyST Markdown](https://mystmd.org) / Jupyter Book 2 and served via GitHub Pages from the `docs/` folder.

## Setup

```bash
conda env create -f environment.yml
```

## Building the site

```bash
conda activate dukemids
jupyter-book build --html
cp -R _build/html/* docs/
```

Full one-liner with push:

```bash
jupyter-book build --html; cp -R _build/html/* docs; git add .; git commit; git push
```

## Serving locally for debugging

You can run it locally with `jupyter-book start`