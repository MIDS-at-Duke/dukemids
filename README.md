# dukemids

Source for [dukemids.com](https://dukemids.com) — a collection of resources for Duke MIDS students.

Built with [MyST Markdown](https://mystmd.org) and served via GitHub Pages from the `docs/` folder.

## Building the site

```bash
conda run -n jb2 myst build --html
cp -R _build/html/* docs/
```
