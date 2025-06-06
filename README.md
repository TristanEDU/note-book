# [Note Book](https://tristanedu.github.io/note-book/)

This repository contains my personal wiki built with [MkDocs](https://www.mkdocs.org/) and hosted on [GitHub](https://github.com/TristanEDU/note-book).

**The docs are best read [online](https://tristanedu.github.io/note-book/).**

## Building the documentation

Install the dependencies and start the development server:

```bash
pdm install  # or `pip install -r requirements.txt`
pdm run mkdocs serve
```

Visit <http://127.0.0.1:8000/> to preview the site locally. To generate the static site run:

```bash
pdm run mkdocs build
```

If you add or rename pages, regenerate the navigation in `mkdocs.yml` by running:

```bash
python syncnotes.py
```

## Contributing

Found a mistake or want to add new content? Feel free to open a pull request or [file an issue](https://github.com/TristanEDU/note-book/issues/new).

## Thank you

If you enjoy this project you can also check out my [other projects](https://github.com/TristanEDU).

[![CC0](https://img.shields.io/badge/license-CC0-0a0a0a.svg?style=flat&colorA=0a0a0a)](https://creativecommons.org/publicdomain/zero/1.0/)
